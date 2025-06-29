from flask import Flask
import httpx

app = Flask(__name__)
redirect_path = "http://62.16.42.64:8888/upload"

@app.route('/', methods=['POST'])
def transport():
	try:
		body = request.get_json()
		response = httpx.post(redirect_path, json=body)
		return 200
	except Exception as e:
		app.logger.error(e)
		return 500

if __name__=='__main__':
	app.run(host='0.0.0.0', port=8080)
