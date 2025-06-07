from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Virtual TA API is running! Use POST /api/ to ask questions."

@app.route("/api/", methods=["POST"])
def answer_question():
    data = request.get_json()
    question = data.get("question", "")
    answer = f"Sorry, I can't answer: '{question}' yet."
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
