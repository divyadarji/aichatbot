import google.generativeai as genai
from config import Config
import re

class Chatbot:
    def __init__(self, api_key=None, model_name=None):
        """
        Initialize the chatbot with Google Generative AI
        """
        api_key = api_key or Config.GEMINI_API_KEY
        model_name = model_name or Config.DEFAULT_MODEL
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name)
        
        self.context = Config.INITIAL_CONTEXT
    
    def clean_response(self, text):
        """
        Clean and format the response
        """
        text = re.sub(r'\*{2,}', '', text)
        text = re.sub(r'\s+', ' ', text).strip()
        
        return text
    
    def generate_response(self, user_message, additional_context=None):
        """
        Generate AI response based on user message and scraped website content.
        """
        try:
            # Combine base context with additional context
            full_prompt = f"""
            You are a chatbot that answers questions based on the extracted website content. 
            Use the website information to provide responses accurately and concisely.

            Website Context:
            {additional_context}

            User: {user_message}
"""

            # Generate response
            response = self.model.generate_content(full_prompt)
            
            # Clean response
            cleaned_response = self.clean_response(response.text)
            
            return cleaned_response
        
        except Exception as e:
            print(f"Error generating response: {e}")
            return "Sorry, I'm having trouble processing your request."
    
    def handle_social_link_request(self, user_message, social_links):
        """
        Handle requests for social media links.
        """
        for platform in social_links.keys():
            if platform in user_message.lower():
                return f"Here is my {platform.capitalize()} link: {social_links[platform]}"
        return None
