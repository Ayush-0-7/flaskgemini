from flask import Flask, request, jsonify
import google.generativeai as genai
from config import *

app = Flask(__name__)

# Set up the API key for Google Generative AI
genai.configure(api_key='AIzaSyDZwBpgfvc4rMwbEz0Jhkq6B5ADnJpaJM8')

@app.route('/genai2', methods=['POST'])
def genai2():
    # Extract the prompt from the incoming POST request
    prompt = request.json.get('question1') + ' Hey, from the given text, extract the product name, product price, product discount, and product link in JSON format and return the JSON format only.'
    
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    # Generate content using the Generative AI model
    response = genai.generate_text(model='gemini-1.5-flash', prompt=prompt)

    # Extract and return the generated text response
    generated_text = response['text']
    return jsonify({"answer": generated_text})

if __name__ == "__main__":
    app.run(debug=True)
