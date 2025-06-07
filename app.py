from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def index():
    return 'Virtual TA API is running! Use POST /api/ to ask questions.'

@app.route('/api/', methods=['POST'])
def answer():
    data = request.get_json()
    question = data.get('question', '')
    
    if "deadline" in question.lower():
        return jsonify({"answer": "The deadline for Project 1 is June 14, 2025."})
    else:
        return jsonify({"answer": f"Sorry, I can't answer: '{question}' yet."})
