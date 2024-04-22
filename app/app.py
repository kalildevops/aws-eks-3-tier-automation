from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route("/")
def index():
    return "Default path"

@app.route("/path1")
def path1():
    return "path1"

@app.route("/path2")
def path2():
    return "path2"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)