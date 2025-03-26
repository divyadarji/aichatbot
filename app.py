from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from chatbot import Chatbot
from utils import scrape_website
import os
import re


app = Flask(__name__, static_folder='.')
# More permissive CORS configuration
CORS(app, resources={r"/*": {"origins": "*"}})

# Initialize chatbot
chatbot = Chatbot()

# Default website to scrape (you can change this)
DEFAULT_WEBSITE = "https://divyadarji.vercel.app/"

@app.route('/', methods=['GET'])
def home():
    """
    Serve the HTML file
    """
    return send_from_directory('.', 'chatbot.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    """
    Main chat endpoint for processing user messages
    """
    try:
        # Get user message
        data = request.get_json()
        user_message = data.get('message', '')

        if not user_message:
            return jsonify({"response": "No message provided"}), 400

        # Determine website to scrape
        website_url = DEFAULT_WEBSITE

        # Optional: Extract custom website from message
        # You can add more sophisticated website detection if needed
        website_match = re.search(r'https?://\S+', user_message)
        if website_match:
            website_url = website_match.group(0)

        # Scrape website for context
        website_content, website_links = scrape_website(website_url)

        # Handle social media link requests first
        social_link_response = chatbot.handle_social_link_request(user_message, website_links)
        if social_link_response:
            return jsonify({"response": social_link_response})

        # Generate AI response with optional website context
        response_text = chatbot.generate_response(
            user_message, 
            additional_context=website_content
        )

        return jsonify({"response": response_text})

    except Exception as e:
        print(f"Error processing chat request: {e}")
        return jsonify({"response": "Sorry, an error occurred while processing your request."}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)