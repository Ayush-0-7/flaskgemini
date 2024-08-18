from flask import Flask, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# Set up the API key for Google Generative AI (load from environment for better security)
genai.configure(api_key='AIzaSyDZwBpgfvc4rMwbEz0Jhkq6B5ADnJpaJM8')
@app.route('/')
def main():
    return "Hello from Ayush ki duniya."
@app.route('/genai2', methods=['POST'])
def genai2():
    # Extract the prompt from the incoming POST request
    question1 = request.json.get('question1')
    if not question1:
        return jsonify({"error": "No question1 provided"}), 400

    prompt = question1 + 'Hey from the given text extract the product name, product price, product discount, and product link in json format and return the json format only.'

    # Generate content using the Generative AI model
    try:
        # Generate response using the Gemini model
        response = genai.generate_text(
            model='gemini-1.5-turbo',  # 'gemini-1.5-flash' may need to be updated to 'gemini-1.5-turbo' if necessary
            prompt=prompt
        )
        
        # Extract generated text from the response
        if response and response.candidates:
            generated_text = response.candidates[0]['output']  # Get the first candidate's output
        else:
            generated_text = "No result generated"

        return jsonify({"answer": generated_text})
    except Exception as e:
        # Return the error message in case of failure
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
