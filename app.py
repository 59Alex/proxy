from flask import Flask, request, jsonify
import base64
import json
import os
import httpx

app = Flask(__name__)
redirect_path_upload = "http://62.16.42.64:8888/upload"

@app.route('/upload', methods=['POST'])
def transport():
	try:
		body = base64.b64decode(request.get_data().encode('utf-8'))
		json = json.loads(body.decode('utf-8'))
		response = httpx.post(redirect_path_upload, json=json)
		return jsonify({"status": "ok"}), 200
	except Exception as e:
		app.logger.error(e)
		return jsonify({"status": "err"}), 500

if __name__=='__main__':
	app.run(host='0.0.0.0', port=8080)
