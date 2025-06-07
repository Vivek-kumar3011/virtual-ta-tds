from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
# CORS fix for frontend on Vercel
CORS(app, resources={r"/api/*": {"origins": "https://virtual-ta-tds.vercel.app"}})

@app.route("/")
def index():
    return "Virtual TA API is running! Use POST /api/ to ask questions."

@app.route("/api/", methods=["POST"])
def api():
    data = request.json
    question = data.get("question", "")
    if "deadline" in question.lower():
        answer = "The Project 1 deadline is June 15."
    else:
        answer = f"Sorry, I can't answer: '{question}' yet."
    return jsonify({"answer": answer})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
