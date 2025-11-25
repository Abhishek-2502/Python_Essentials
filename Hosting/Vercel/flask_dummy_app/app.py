from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify(message="Hello from Flask on Vercel!")


@app.route("/health")
def health():
    return jsonify(status="ok")


if __name__ == "__main__":
    # Local dev server (not used by Vercel)
    app.run(host="0.0.0.0", port=8000, debug=True)
