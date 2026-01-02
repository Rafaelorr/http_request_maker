from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/get', methods=['GET'])
def main_get():
    data = {
        "status": "success",
        "message": "Dit is een test API endpoint",
        "data": {
            "id": 1,
            "naam": "Test data"
        }
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)