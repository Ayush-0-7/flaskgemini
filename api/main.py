from flask import Flask, request, jsonify
import google.generativeai as genai
from config import *

app = Flask(__name__)

# Set up the API key for Google Generative AI
genai.configure(api_key='AIzaSyDZwBpgfvc4rMwbEz0Jhkq6B5ADnJpaJM8')

@app.route('/genai2', methods=['POST'])
def genai2():
    # Extract the prompt from the incoming POST request
    question1 = request.json.get('question1')
    if not question1:
        return jsonify({"error": "No question1 provided"}), 400

    prompt = question1 + 'Hey from the given text extract the product name product price product discount and product link in json format and return the json format only.'

    # Generate content using the Generative AI model
    try:
        # Using generate_text instead of GenerativeModel
        response = genai.generate_text(
            model='gemini-1.5-flash',
            prompt=prompt
        )
        
        generated_text = response.result if response.result else "No result generated"
        return jsonify({"answer": generated_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
