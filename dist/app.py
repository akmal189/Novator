from flask import Flask, request, jsonify, render_template

from chatgpt.RequestCounterDB import RequestCounterDB
from chatgpt.chat_gpt import chat_with_gpt, get_ip_address

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/chat", methods=["POST"])
def chat_api():
    with RequestCounterDB() as db:
        ip_address = get_ip_address()
        request_count = db.get_request_count(ip_address)

        if request_count >= 100:
            return jsonify({"error": "Request limit reached for this IP address today."}), 429

        prompt = request.json.get("prompt")
        if not prompt:
            return jsonify({"error": "No prompt provided."}), 400

        response = chat_with_gpt(prompt)
        if response is not None:
            db.increment_request_count(ip_address)
            return jsonify({"response": response})
        else:
            return jsonify({"error": "No response was generated."}), 500


if __name__ == "__main__":
    app.run(debug=True)

