from flask import Flask, jsonify

app = Flask(__name__)

users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]

@app.route("/users")
def get_users():
    return jsonify(users)

@app.route("/health")
def health():
    return {"status": "user service running"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
