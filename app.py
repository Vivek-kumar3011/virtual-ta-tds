from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/', methods=['POST'])
def answer_question():
    data = request.get_json()
    question = data.get("question", "")
    
    # Dummy answer for now
    response = {
        "answer": f"You asked: {question}. This is a placeholder answer.",
        "links": []
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

