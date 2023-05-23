from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    return jsonify({"message": "This is the index"})

@app.route('/v2/orders/{id}', methods=['POST'])
def index():
    return jsonify({"message": "this is the orders route"})

@app.route('/v2/accounts/{id}', methods=['POST'])
def index():
    return jsonify({"message": "this is the accounts route"})

@app.route('/v2/status/{id}', methods=['POST'])
def index():
    return jsonify({"message": "this is the status route"})

@app.route('/v2/claims', methods=['POST'])
def index():
    return jsonify({"message": "this is the claims route"})

@app.route('/cool')
def cool():
    return jsonify({"message": "this is the cool route"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
