from flask import Flask, request, jsonify
from google.cloud import firestore
import uuid

app = Flask(__name__)
db = firestore.Client()

@app.route('/add_person', methods=['POST'])
def add_person():
    data = request.get_json()
    if 'name' not in data or 'phones' not in data:
        return jsonify({"error": "Invalid data"}), 400

    for phone in data['phones']:
        if 'number' not in phone or 'type' not in phone:
            return jsonify({"error": "Invalid phone data"}), 400

    record_id = str(uuid.uuid4())
    try:
        db.collection('users').document(record_id).set(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"id": record_id}), 201

@app.route('/get_person/<record_id>', methods=['GET'])
def get_person(record_id):
    try:
        uuid.UUID(record_id)
    except ValueError:
        return jsonify({"error": "Invalid record ID"}), 400

    try:
        doc_ref = db.collection('users').document(record_id)
        doc = doc_ref.get()
        if doc.exists:
            return jsonify(doc.to_dict()), 200
        else:
            return jsonify({"error": "Record not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

