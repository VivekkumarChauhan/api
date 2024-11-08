from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample endpoint
@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify(message="Hello, World!")

# Endpoint with query parameter
@app.route('/api/greet', methods=['GET'])
def greet():
    name = request.args.get("name", "Guest")
    return jsonify(message=f"Hello, {name}!")

if __name__ == '__main__':
    app.run(debug=True)
