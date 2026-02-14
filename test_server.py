from flask import Flask, jsonify, request
import json

try:
    with open('get_server_config.json', 'r') as file:
        data = json.load(file)
    print("File data =", data)
    
except FileNotFoundError:
    print("Error: Het bestand 'get_server_config.json' bestaat niet.")

app = Flask(__name__)

@app.route('/get/', methods=['GET'])
def main_get():
    if not data:
        return 404
    return jsonify(data)

@app.route("/get/<number>", methods=["GET"])
def get_params(number):
    try:
        number = int(number)
    except ValueError:
        return 400

    return jsonify({"number": number**number})

@app.route("/get/headers", methods=["GET"])
def get_read_request_headers():
    request_headers = {}
    request_headers["user-agent"] = request.headers.get("user-agent")
    request_headers["host"] = request.headers.get("host")
    request_headers["accept-encoding"] = request.headers.getlist("accept-encoding")
    request_headers["accept"] = request.headers.get("accept")
    request_headers["connection"] = request.headers.get("connection")
    request_headers["accept-language"] = request.headers.getlist("Accept-Language")
    request_headers["referer"] = request.headers.get("Referer")
    request_headers["connection"] = request.headers.get("Connection")
    request_headers["if-modified-since"] = request.headers.get("If-Modified-Since")
    request_headers["If-None-Match"] = request.headers.get("If-None-Match")
    request_headers["cache-control"] = request.headers.get("Cache-Control")

    return jsonify(request_headers), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)