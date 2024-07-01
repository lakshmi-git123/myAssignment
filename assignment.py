from flask import Flask, request, jsonify
from cerberus import Validator
from google.cloud import bigquery  # Import the BigQuery client library
import os

app = Flask(__name__)


# Define a schema for validation (same as before)
schema = {
    'id': {'type': 'integer', 'required': True},
    'first_name': {'type': 'string', 'required': True},
    'last_name': {'type': 'string', 'required': True},
    'age': {'type': 'integer', 'min': 0},
    'email': {'type': 'string', 'required': True, 'regex': r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'},
    'address': {
        'type': 'dict',
        'schema': {
            'street': {'type': 'string', 'required': True},
            'city': {'type': 'string', 'required': True},
            'state': {'type': 'string', 'required': True},
            'zip': {'type': 'string', 'required': True}
        }
    }
}

@app.route('/person', methods=['POST'])
def create_person():
    try:
        data = request.get_json()
        v = Validator(schema)
        if not v.validate(data):
            return jsonify({"error": "Invalid data format", "validation_errors": v.errors})
        
   # Initialize the BigQuery client with your project ID
        #os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:\\Users\\vishn\\myAssignment\\myassignment-426912-04f2ed64ffc3.json'  # Set the path to your key file
        #print('GOOGLE_APPLICATION_CREDENTIALS:', os.environ.get('GOOGLE_APPLICATION_CREDENTIALS'))

        client = bigquery.Client(project='myassignment-426912')  # Initialize the BigQuery client

        
        # Define your BigQuery dataset and table information
        dataset_id = 'datasetname'
        table_id = 'tablename_json'
        
        # Create a BigQuery row from the validated data
        row = {
            'id': data['id'],
            'first_name': data['first_name'],
            'last_name': data['last_name'],
            'age': data.get('age', None),
            'email': data['email'],
            'address': data['address']
        }
        
        # Insert the row into BigQuery
        table_ref = client.dataset(dataset_id).table(table_id)
        errors = client.insert_rows_json(table_ref, [row])
        if errors:
            return jsonify({"error": "Error inserting data into BigQuery", "details": str(errors)})
        
        # Return a unique identifier (you can customize this based on your use case)
        unique_identifier = f"person_{data['id']}"
        return jsonify({"message": "Person record created successfully", "unique_identifier": unique_identifier})
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4040)
