import re

# Functions for data extraction
def extract_emails(text):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    return re.findall(pattern, text)

def extract_urls(text):
    pattern = r"https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/?[^\s]*"
    return re.findall(pattern, text)

def extract_phone_numbers(text):
    pattern = r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"
    return re.findall(pattern, text)

def extract_hashtags(text):
    pattern = r"#\w+"
    return re.findall(pattern, text)

def extract_currency(text):
    pattern = r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?"
    return re.findall(pattern, text)

# Sample input text
sample_text = """
Emails: user@example.com, firstname.lastname@company.co.uk
URLs: https://www.example.com, http://subdomain.example.org/page
Phone Numbers: (123) 456-7890, 123-456-7890, 123.456.7890
Hashtags: #example, #ThisIsAHashtag
Currency: $19.99, $1,234.56, $50
"""

# Running the functions and printing results
print("Extracted Emails:", extract_emails(sample_text))
print("Extracted URLs:", extract_urls(sample_text))
print("Extracted Phone Numbers:", extract_phone_numbers(sample_text))
print("Extracted Hashtags:", extract_hashtags(sample_text))
print("Extracted Currency Amounts:", extract_currency(sample_text))
