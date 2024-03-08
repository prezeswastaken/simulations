from flask import Flask, jsonify, request
from flask_cors import CORS

from one import AlgorithmOne
from two import AlgorithmTwo

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000", "https://example.com"])


@app.route("/api/one", methods=["POST"])
def get_one():
    data = request.get_json()
    a = int(data.get("a", 0))
    m = int(data.get("m", 0))
    x0 = float(data.get("x0", 0.0))
    n = int(data.get("n", 0))

    calc = AlgorithmOne(a=a, m=m, x0=x0)
    results = calc.run(n)

    return jsonify(list(results))


@app.route("/api/two", methods=["POST"])
def get_two():
    data = request.get_json()
    m = int(data.get("m", 0))
    x0 = float(data.get("x0", 0.0))
    n = int(data.get("n", 0))

    calc = AlgorithmTwo(m=m, x0=x0)
    results = calc.run(100)

    return jsonify(list(results))


if __name__ == "__main__":
    app.run(debug=True, port=8000)
