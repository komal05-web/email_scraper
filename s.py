import re
import pandas as pd
from bs4 import BeautifulSoup

def scrape_local_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            soup = BeautifulSoup(content, 'html.parser')
            return soup
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def extract_emails(html_data):
    if html_data:  # Check if html_data is not None
        email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
        emails = re.findall(email_pattern, str(html_data))
        return list(set(emails))  # Remove duplicates
    else:
        return []

def validate_email_list(email_list):
    valid_emails = []
    for email in email_list:
        if "@" in email:  # Simple validation for testing purposes
            valid_emails.append(email)
    return valid_emails

def apply_filters(email_list, domain=None):
    if domain:
        filtered_emails = [email for email in email_list if email.endswith(domain)]
        return filtered_emails
    return email_list

def export_to_csv(data, file_name):
    try:
        df = pd.DataFrame(data, columns=["Email"])
        df.to_csv(file_name, index=False)
        print(f"Data exported to {file_name}")
    except Exception as e:
        print(f"An error occurred while exporting data: {e}")

def main():
    file_path = r"C:\Users\Komal Pandey\OneDrive\Desktop\email\test.html"  # Update with your actual path!

    # Test the file reading directly:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            print("File read test: File read successfully.")
            print(content)
    except Exception as e:
        print(f"File read test error: {e}")
        return #stops running the script if this test fails.

    html_data = scrape_local_file(file_path)

    if html_data is None: #Handles the error case.
        return

    email_list = extract_emails(html_data)
    print(f"Extracted Emails: {email_list}")

    valid_emails = validate_email_list(email_list)
    print(f"Validated Emails: {valid_emails}")

    filtered_emails = apply_filters(valid_emails, domain="example.com")
    print(f"Filtered Emails: {filtered_emails}")

    export_to_csv(filtered_emails, "emails.csv")

if __name__ == "__main__":
    main()