import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    # Google Generative AI Configuration
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    
    # Model selection
    DEFAULT_MODEL = 'gemini-1.5-flash'
    
    # Chatbot settings
    CHATBOT_NAME = "AI Assistant"
    INITIAL_CONTEXT = """You are a helpful AI assistant. 
    Your goal is to provide accurate, concise, and helpful responses 
    to user queries across various topics."""