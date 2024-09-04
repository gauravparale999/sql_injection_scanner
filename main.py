import scanner

def main():
    url = input("Enter the URL of the web application (e.g., http://example.com/page.php?id=1): ")
    if not url:
        print("URL cannot be empty.")
        return
    
    # Scan for SQL Injection vulnerabilities
    vulnerabilities = scanner.scan_sql_injection(url)
    
    # Display results
    if vulnerabilities:
        print("Potential SQL Injection vulnerabilities found with the following payloads:")
        for payload in vulnerabilities:
            print(f"- {payload}")
    else:
        print("No SQL Injection vulnerabilities found.")

if __name__ == "__main__":
    main()
