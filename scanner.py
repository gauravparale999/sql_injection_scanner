import requests
from urllib.parse import urlencode
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_pdf_report(file_path, url, vulnerabilities):
    c = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica", 12)
    c.drawString(72, height - 72, f"SQL Injection Vulnerability Report")
    c.drawString(72, height - 100, f"URL: {url}")
    
    if vulnerabilities:
        c.drawString(72, height - 140, "Vulnerabilities found:")
        y_position = height - 160
        for payload in vulnerabilities:
            c.drawString(72, y_position, f"- {payload}")
            y_position -= 20
    else:
        c.drawString(72, height - 140, "No vulnerabilities found.")

    c.save()

def test_sql_injection(url, payload):
    encoded_payload = urlencode({'param': payload})
    test_url = f"{url}?{encoded_payload}"
    
    try:
        response = requests.get(test_url)
        if "error" in response.text.lower() or "warning" in response.text.lower():
            return True
    except requests.RequestException as e:
        print(f"Request failed: {e}")

    return False

def scan_sql_injection(url):
    payloads = [
        "' OR '1'='1",
        "' OR '1'='1' --",
        "' UNION SELECT NULL, NULL --",
        "' OR 'x'='x"
    ]
    
    found_vulnerabilities = []
    
    for payload in payloads:
        if test_sql_injection(url, payload):
            print(f"Payload detected: {payload}")
            found_vulnerabilities.append(payload)
    
    # Generate the PDF report
    create_pdf_report("sql_injection_report.pdf", url, found_vulnerabilities)
    
    return found_vulnerabilities
