# Email Scraper Tool

## Overview
This is a Python-based email scraping tool that extracts email addresses from local HTML files, validates them, applies optional filters, and exports the results to a CSV file. It's designed for lead generation or contact management workflows.

This project was created as part of the **AI-Readiness Pre-Screening Challenge**, where the focus is on developing a functional tool within a constrained time frame (5 hours). The tool highlights simplicity, practicality, and ease of use.

---

## Features
- **HTML Parsing**: Reads and processes local HTML files to extract data.
- **Email Extraction**: Utilizes regex to extract all email addresses from the HTML content.
- **Validation**: Performs basic validation of extracted email addresses.
- **Filtering**: Offers the option to filter emails by a specific domain (e.g., `example.com`).
- **CSV Export**: Outputs validated and filtered emails into a CSV file for easy use.

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/email-scraper.git
   ```
2. Navigate to the project directory:
   ```bash
   cd email-scraper
   ```
3. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```
   *(Create a `requirements.txt` file including `beautifulsoup4`, `pandas`, etc.)*

---

## Usage
1. **Prepare a Local HTML File**:
   - Create an HTML file (`test.html`) containing email addresses for testing.
   - Example file:
     ```html
     <!DOCTYPE html>
     <html>
     <head>
         <title>Sample Emails</title>
     </head>
     <body>
         <p>Email: contact@example.com</p>
         <p>Email: info@domain.com</p>
     </body>
     </html>
     ```

2. **Update File Path**:
   - Update the `file_path` variable in `scraper.py` with the full path to your HTML file:
     ```python
     file_path = r"C:\path\to\test.html"
     ```

3. **Run the Tool**:
   - Execute the script:
     ```bash
     python scraper.py
     ```

4. **Output**:
   - Extracted emails will be displayed in the terminal.
   - A CSV file (`emails.csv`) will be created in the same directory.

---

## Example Output
**Terminal Output**:
```
Extracted Emails: ['contact@example.com', 'info@domain.com']
Validated Emails: ['contact@example.com', 'info@domain.com']
Filtered Emails: ['contact@example.com']
Data exported to emails.csv
```

**CSV Output (`emails.csv`)**:
| Email               |
|---------------------|
| contact@example.com |

---

## Project Structure
```
email-scraper/
├── scraper.py          # Main script
├── test.html           # Sample local HTML file
├── emails.csv          # Generated CSV file
└── requirements.txt    # Python dependencies
```

---

## Design Choices
- **Focus on Local Files**: Emphasized processing local files for simplicity and reproducibility.
- **Regex for Extraction**: Used a regular expression to identify email patterns in raw HTML.
- **Validation & Filtering**: Added optional filters to enhance usability.
- **CSV Output**: Chose CSV as it integrates easily with most data workflows.

---

## Limitations
- The tool currently works with local HTML files only; it does not scrape live websites.
- Validation is basic and may not identify all invalid email formats.
- Filtering is limited to domain-level customization.

---

## Contributing
Contributions are welcome! Feel free to submit issues, fork the repository, and create pull requests.

---

