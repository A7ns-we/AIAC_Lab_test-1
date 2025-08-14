import re

def extract_emails(text):
    # Regular expression for matching email addresses
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    return re.findall(email_pattern, text)

if __name__ == "__main__":
    text = input("Enter a block of text:\n")
    emails = extract_emails(text)
    print("Extracted email addresses:")
    for email in emails:
        print(email)