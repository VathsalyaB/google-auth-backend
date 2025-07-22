from flask import Flask, request, jsonify
from google.oauth2 import id_token
from google.auth.transport import requests as grequests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/verify-token', methods=['POST'])
def verify_token():
    token = request.json.get('token')
    try:
        id_info = id_token.verify_oauth2_token(token, grequests.Request())
        return jsonify({"message": "Token verified", "user": id_info}), 200
    except Exception as e:
        return jsonify({"error": "Invalid token", "details": str(e)}), 400
