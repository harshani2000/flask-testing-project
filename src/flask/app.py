from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hello')
def hello():
    return jsonify({"message": "Hello, World!"})

@app.route('/sum/<int:a>/<int:b>')
def sum_numbers(a, b):
    return jsonify({"sum": a + b})
