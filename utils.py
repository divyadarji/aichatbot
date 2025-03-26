import requests
from bs4 import BeautifulSoup
import re

def clean_text(text):
    """
    Clean and preprocess scraped text
    
    Args:
        text (str): Raw text to clean
    
    Returns:
        str: Cleaned text
    """
    # Remove extra whitespaces
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Remove special characters and limit length
    text = re.sub(r'[^a-zA-Z0-9\s.,!?]', '', text)
    
    return text[:3000]  # Limit to 3000 characters

def scrape_website(url, max_content_length=3000):
    """
    Scrape website content and extract text and social links
    
    Args:
        url (str): Website URL to scrape
        max_content_length (int): Maximum length of content to return
    
    Returns:
        tuple: (website content, social links)
    """
    try:
        # Add headers to mimic browser request
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # Attempt to get website content
        response = requests.get(url, headers=headers, timeout=10)
        
        # Check if request was successful
        response.raise_for_status()
        
        # Parse HTML
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Remove script, style, and navigation elements
        for script in soup(["script", "style", "nav", "header", "footer"]):
            script.decompose()
        
        # Extract text content from specific tags
        content_tags = ["p", "h1", "h2", "h3", "h4", "article", "section"]
        paragraphs = soup.find_all(content_tags)
        
        # Clean and collect text
        content_list = []
        for p in paragraphs:
            text = p.get_text(strip=True)
            if text and len(text) > 10:  # Ignore very short texts
                content_list.append(clean_text(text))
        
        # Join and truncate content
        full_content = " ".join(content_list)[:max_content_length]
        
        # Extract social media links
        social_platforms = ["linkedin", "twitter", "instagram", "github", "facebook", "youtube"]
        social_links = {}
        
        for a in soup.find_all('a', href=True):
            link_text = a.text.strip()
            link_url = a['href']
            
            # Match social media links
            for platform in social_platforms:
                if platform in link_url.lower() or platform in link_text.lower():
                    social_links[platform] = f'<a href="{link_url}" target="_blank">{link_text or platform.capitalize()}</a>'
        
        return full_content, social_links
    
    except requests.RequestException as e:
        print(f"Error scraping website: {e}")
        return f"Could not retrieve website data. Error: {str(e)}", {}