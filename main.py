from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/hello")
def hello():
    return jsonify({"message": "Hello from Flask! ;)"})

@app.route("/sumvalues", methods=["POST"])
def sum_values():
    data = request.get_json()

    if not data or "values" not in data or not isinstance(data["values"], list):
        return jsonify(error="Missing or invalid 'values' list in body"), 400

    try:
        result = sum(data["values"])
        return jsonify(result=result), 200
    except TypeError:
        return jsonify(error="All elements in 'values' must be numbers"), 400

if __name__ == "__main__":
    app.run(debug=True)