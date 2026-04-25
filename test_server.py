#!/usr/bin/env python3
from flask import Flask, jsonify, request, make_response
import json

# laad server config
try:
    with open('get_server_config.json', 'r') as file:
        data = json.load(file)
    
except FileNotFoundError:
    print("Error: Het bestand 'get_server_config.json' bestaat niet.")
    print("Standaard config gaat gebruikt worden.")

    config = {
    "message": "Dit is een test API endpoint",
    "data": {"id": 1, "naam": "Test data"}
}

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
    request_headers = dict(request.headers)

    return jsonify(request_headers), 200

@app.route("/get/set_cookies")
def set_cookies():
    # Initializing response object

    resp = make_response('Setting the cookie') 
    resp.set_cookie(key = "Character_Class", value = 'druid', max_age = None, expires = None, path = '/', domain = None,  secure = None, httponly = False)

    return resp

@app.route('/get/get_cookies')
def get_cookies():
    Character_Class = request.cookies.get('Character_Class')

    return jsonify({"Message":f"You're welcome {Character_Class}"})

@app.route("/get/only_druids")
def check_cookies():
    Character_Class = request.cookies.get("Charachter_Class")

    if Character_Class == "druid":
        return jsonify({"Message": "You're invited my druidic friend."}), 200
    else:
        return jsonify({"Message": "Only druids are allowed here."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)