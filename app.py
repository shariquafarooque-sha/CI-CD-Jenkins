from flask import Flask, jsonify
import datetime
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "service": "order-service",
        "version": "1.0.0",
        "environment": os.getenv("APP_ENV", "production"),
        "status": "running",
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "order-service"
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)