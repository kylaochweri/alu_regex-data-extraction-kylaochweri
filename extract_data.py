import re

def extract_emails(text):
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(pattern, text)

def extract_urls(text):
    pattern = r'https?://(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/\S*)?'
    return re.findall(pattern, text)

def extract_phone_numbers(text):
    pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
    return re.findall(pattern, text)

def extract_credit_cards(text):
    pattern = r'\b(?:\d{4}[-\s]?){3}\d{4}\b'
    return re.findall(pattern, text)

def extract_hashtags(text):
    pattern = r'#[a-zA-Z0-9_]+'
    return re.findall(pattern, text)

if __name__ == "__main__":
    sample_text = """
        Contact us at support@example.com or admin@website.co.uk.
        Visit https://www.example.com or http://sub.example.org/page.
        Call us at (123) 456-7890 or 123-456-7890.
        Credit card: 1234-5678-9012-3456 or 1234 5678 9012 3456.
        Trending: #regex #Python #DataExtraction
    """
    
    print("Emails:", extract_emails(sample_text))
    print("URLs:", extract_urls(sample_text))
    print("Phone Numbers:", extract_phone_numbers(sample_text))
    print("Credit Cards:", extract_credit_cards(sample_text))
    print("Hashtags:", extract_hashtags(sample_text))