# app/routes.py
from flask import Blueprint, request, jsonify
from .functions import upload_to_api, api_configs

api = Blueprint('api', __name__)

@api.route('/upload', methods=['POST'])
def upload_file():
    url_to_upload = request.json.get('url')
    if not url_to_upload:
        return jsonify({"error": "URL not provided"}), 400

    file_codes = {}
    for api_name, api_config in api_configs.items():
        file_codes[api_name] = upload_to_api(api_config, url_to_upload)

    return jsonify(file_codes)

@api.route('/')
def running():
    return jsonify({"status": "Server is running!"})
