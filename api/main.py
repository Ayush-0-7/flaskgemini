from flask import Flask, request, jsonify
import google.generativeai as genai
from config import *
app = Flask(__name__)

# Set up the API key for Google Generative AI
genai.configure(api_key='AIzaSyDZwBpgfvc4rMwbEz0Jhkq6B5ADnJpaJM8')

@app.route('/genai2', methods=['POST'])
def genai2():
    # Extract the prompt from the incoming POST request
    prompt = request.json.get('question1')+'Hey from the given text extract the product name product price product discount product link(the link is masked in the buy now on amazon text) and product image in json format and return the json format only.'
    
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    # Generate content using the Generative AI model
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content(prompt)

    # Extract and return the text response
    generated_text = response.text
    return jsonify({"answer": generated_text})

