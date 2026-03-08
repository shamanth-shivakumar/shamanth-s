from flask import Flask, jsonify

app = Flask(__name__)

payments = [
    {"id": 1, "amount": 500},
    {"id": 2, "amount": 1200}
]

@app.route("/payments")
def get_payments():
    return jsonify(payments)

@app.route("/health")
def health():
    return {"status": "payment service running"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
