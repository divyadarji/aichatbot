# AI CHATBOT 

## Overview
This is a Flask-based chatbot service that integrates with Google's Gemini AI to generate responses based on website content. The chatbot dynamically extracts relevant information from a website to provide accurate answers.

## Features
- Uses Google's Gemini API for AI-powered responses
- Scrapes website content dynamically to provide relevant answers
- Supports handling social media link requests
- Flask-based API with CORS enabled for easy integration

## Installation

### Prerequisites
Ensure you have Python installed along with the required dependencies.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/divyadarji/aichatbot.git
   cd aichatbot
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables by creating a `.env` file:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## Usage

### Running the Application
Start the Flask app:
```bash
python app.py
```
By default, the application runs on `http://127.0.0.1:5000/`

### API Endpoints

#### 1. **Chat API**
   - **Endpoint:** `/api/chat`
   - **Method:** `POST`
   - **Request Body:**
     ```json
     {
       "message": "What services do you provide?"
     }
     ```
   - **Response:**
     ```json
     {
       "response": "We provide AI/ML engineering services, API development, and more."
     }
     ```

## File Structure
```
/aichatbot
│── app.py             # Main Flask application
│── chatbot.py         # Chatbot logic
│── config.py          # Configuration settings
│── utils.py           # Helper functions (web scraping, text cleaning)
│── requirements.txt   # Dependencies
│── .env               # API keys and environment variables
```

## Future Improvements
- Implement better error handling for web scraping failures
- Improve chatbot's contextual understanding using memory
- Add authentication for API requests

## Contributors
- **Divya Kumar Darji** - AI/ML Engineer

## License
This project is licensed under the MIT License.

