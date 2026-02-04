"""
ALU Regex Data Extraction Assignment

Purpose:
    - Extract structured data from raw text 
    - Validate input and ignore unsafe/malformed content
    - Handle realistic variations in formats
    - Demonstrate awareness of potential hostile input
"""

import re
import json


# ------------------------ Sample Input ------------------------


sample_text_string = """
Hello! Contact John at john.doe@example.com or Jane at jane_doe123@company.co.uk.
Our websites: https://example.com and https://sub.example.co.uk/page?id=1
Call us: (123) 456-7890, 123-456-7890, +1 987 654 3210
Credit cards: 1234-5678-9012-3456, 1234567890123456, 1234 5678 9012 3456
Times: 14:30, 2:30 PM, 02:30 am
HTML example: <div class="content">Hello</div> <p>Paragraph</p>
Hashtags: #coding #Python3 #RegexFun
Currency: $19.99, $1,234.56, $0.99
Malicious text: <script>alert('hack')</script>

"""


# ------------------------ Input Methods ------------------------


def read_text_file(filename):
    """Reads a text file and returns content"""
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"File {filename} not found. Using empty string.")
        return ""

def get_cli_input():
    """Takes user input from CLI"""
    return input("Paste your text here: ")


# ------------------------ Regex Patterns ------------------------


# 1. Emails
email_pattern = re.compile(
    r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b"
)

# 2. URLs
url_pattern = re.compile(
    r"https?://(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[^\s]*)?"
)

# 3. Phone numbers
phone_pattern = re.compile(
    r"\+?\d{0,3}?\s*(?:\(\d{3}\)|\d{3})[-.\s]?\d{3}[-.\s]?\d{4}"
)

# 4. Credit card numbers
cc_pattern = re.compile(
    r"\b(?:\d{4}[-\s]?){3}\d{4}\b"
)

# 5. Times (12-hour and 24-hour)
time_pattern = re.compile(
    r"\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[AaPp][Mm])?\b"
)

# 6. HTML tags
html_pattern = re.compile(
    r"<\/?[a-zA-Z][a-zA-Z0-9]*(?:\s+[a-zA-Z-]+(?:=[\"'][^\"']*[\"'])?)*\s*\/?>"
)

# 7. Hashtags
hashtag_pattern = re.compile(
    r"#\w+"
)

# 8. Currency amounts
currency_pattern = re.compile(
    r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?"
)


# ------------------------ Extraction Function ------------------------


def extract_data(text):
    """
    Extracts 8 data types from text.
    Removes malicious HTML/script tags.
    Returns structured dictionary.
    """
    # Basic sanitization: remove scripts
    safe_text = re.sub(r"<script.*?>.*?</script>", "", text, flags=re.DOTALL)

    data = {
        "emails": email_pattern.findall(safe_text),
        "urls": url_pattern.findall(safe_text),
        "phones": phone_pattern.findall(safe_text),
        "credit_cards": cc_pattern.findall(safe_text),
        "times": time_pattern.findall(safe_text),
        "html_tags": html_pattern.findall(safe_text),
        "hashtags": hashtag_pattern.findall(safe_text),
        "currency_amounts": currency_pattern.findall(safe_text)
    }

    return data


# ------------------------ Main Program ------------------------


def main():
    print("Select input method:")
    print("1 - Direct string (sample)")
    print("2 - Read from file")
    print("3 - Paste input (CLI)")

    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        text = sample_text_string
    elif choice == "2":
        filename = input("Enter file path: ")
        text = read_text_file(filename)
    elif choice == "3":
        text = get_cli_input()
    else:
        print("Invalid choice. Using sample string.")
        text = sample_text_string

    extracted = extract_data(text)

    print("\n--- Extracted Data ---")
    print(json.dumps(extracted, indent=4))


# ------------------------ Run Program ------------------------


if __name__ == "__main__":
    main()
