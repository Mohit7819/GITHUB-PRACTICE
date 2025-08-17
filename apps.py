from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import os
app = Flask(__name__)
MONGODB_URI = "mongodb+srv://vikramsingh91870:GctbJt1H2KpOlV1v@cluster0.2psj6fk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGODB_URI)
db = client.formData
collection = db.submissions
@app.route('/', methods=['GET'])
def index():
    return render_template('form.html', error=None)

@app.route('/submittodoitem', methods=['POST'])
def submittodoitem():
    item_name = request.form.get('itemName')
    item_description = request.form.get('itemDescription')

    if item_name and item_description:
        todo_collection.insert_one({
            'name': item_name,
            'description': item_description
        })
        return jsonify({'status': 'success', 'message': 'To-Do item added'}), 200
    else:
        return jsonify({'status': 'error', 'message': 'Missing data'}), 400
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    if not name or not email:
        return render_template('form.html', error="Please fill all fields")
    try:
        collection.insert_one({"name": name, "email": email})
        return redirect(url_for('success'))
    except Exception as e:
        return render_template('form.html', error=str(e))
@app.route('/success')
def success():
    return render_template('success.html')
if __name__ == '__main__':
    app.run(debug=True)
