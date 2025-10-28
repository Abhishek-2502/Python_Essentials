# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "flask",
#     "jsonify",
# ]
# ///
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Welcome to the Flask API!"})

@app.route('/basic', methods=['GET'])
def basic():
    return jsonify({"message": "This is a basic endpoint."})

app.run(debug=True, host='127.0.0.1', port=5000)