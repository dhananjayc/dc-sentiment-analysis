from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Flask app setup
app = Flask(__name__)
CORS(app)

# Set OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/")
def hello_world():
	return "Hello world! Welcome to DC Sentiment Analysis Tool (AI-powered)!!"

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
	data = request.json
	text = data.get("text", "")
	# print("text::",text )

	if not text:
		return jsonify({"error": "Text is required"}), 400
	try:
		# Call the OpenAI API
		response = openai.ChatCompletion.create(
			model="gpt-3.5-turbo",  # Use GPT model
		messages=[
				{"role": "system", "content": "You are a helpful assistant."},
				{"role": "user", "content": f"Classify the sentiment of the following text as Positive, Negative, or Neutral:\n\n{text}"}
			]
		)
		# Extract the sentiment response
		sentiment = response['choices'][0]['message']['content'].strip()
		return sentiment

	except Exception as e:
		return f"Oops! Error: {str(e)}"


# if __name__ == '__main__':
app.run(host='0.0.0.0', port=5000, debug=True)
