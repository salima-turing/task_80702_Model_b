
from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load dummy data from CSV
DATA_FILE = 'data.csv'
data = pd.read_csv(DATA_FILE)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_data():
    try:
        # Get user submission data
        site_name = request.form.get('site_name')
        dating_method = request.form.get('dating_method')
        date = request.form.get('date')

        # Add new data to the dataset
        new_data = {'Site Name': site_name, 'Dating Method': dating_method, 'Date': date}
        data.concat(new_data, ignore_index=True)
        data.to_csv(DATA_FILE, index=False)

        return jsonify({'message': 'Data submitted successfully!'}), 200
    except Exception as e:
        return jsonify({'Error': str(e)}), 500

@app.route('/data')
def get_data():
    return jsonify(data.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)