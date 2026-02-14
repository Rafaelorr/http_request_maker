from flask import Flask, jsonify
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)