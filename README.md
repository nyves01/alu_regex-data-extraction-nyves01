# alu_regex-data-extraction-nyves01

**Course:** Junior Frontend Developer Track   

---

## Overview

This project is a Python program that extracts structured data from raw text using **regular expressions (regex)**.  

The program demonstrates:  
- Extraction of multiple data types from **realistic text input**  
- **Validation and security awareness** (ignoring unsafe or malformed input)  
- Flexible input handling  
- Structured and readable output  

---

## Features

1. **Data Extraction:**  
   Extracts the following data types with realistic variations:  
   - Emails (e.g., `john.doe@example.com`, `jane_doe123@company.co.uk`)  
   - URLs (e.g., `https://example.com`, `https://sub.example.co.uk/page?id=1`)  
   - Phone numbers (e.g., `(123) 456-7890`, `123-456-7890`, `+1 987 654 3210`)  
   - Credit card numbers (e.g., `1234-5678-9012-3456`, `1234567890123456`)  
   - Times (12-hour and 24-hour formats, e.g., `14:30`, `2:30 PM`)  
   - HTML tags (e.g., `<div class="content">`, `<p>Paragraph</p>`)  
   - Hashtags (e.g., `#Python3`, `#RegexFun`)  
   - Currency amounts (e.g., `$19.99`, `$1,234.56`)  

2. **Realistic Variations:**  
   Regex patterns handle multiple real-world variations for each data type, reflecting how data appears in production systems.  

3. **Security Awareness:**  
   - Malicious input such as `<script>` tags is ignored.  
   - Only valid, well-formed data is extracted.  

4. **Input Options:**  
   - **Direct string in code** (sample text included)  
   - **Text file input**  
   - **Command-line input (CLI)**  

5. **Structured Output:**  
   - Extracted data is output in **JSON format**, with each data type clearly separated.  

---

