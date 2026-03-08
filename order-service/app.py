from flask import Flask, jsonify

app = Flask(__name__)

orders = [
    {"id": 101, "product": "Laptop"},
    {"id": 102, "product": "Phone"}
]

@app.route("/orders")
def get_orders():
    return jsonify(orders)

@app.route("/health")
def health():
    return {"status": "order service running"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
