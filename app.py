from flask import Flask, request, jsonify
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
from base64 import urlsafe_64encode
import json
import os
import httpx

app = Flask(__name__)
redirect_path_upload = "http://62.16.42.64:8888/upload"
redirect_path_key = "http://62.16.42.64:8888/key"

password = b"XVZ!.Q_password"
salt = b"static_salt"
kdf = PBKDF2HMAC(alghorithm=hashes.SHA256(),length=32, salt=salt, iterations=100_000)
key = urlsafe_b64encode(kdf.derive(password))
felnet = Felnet(key)

@app.route('/upload', methods=['POST'])
def transport():
	try:
		body = felnet.decrypt(request.get_data())
		json = json.loads(decrypted_bytes.decode('utf-8))
		response = httpx.post(redirect_path_upload, json=json)
		return jsonify({"status": "ok"}), 200
	except Exception as e:
		app.logger.error(e)
		return jsonify({"status": "err"}), 500

if __name__=='__main__':
	app.run(host='0.0.0.0', port=8080)
