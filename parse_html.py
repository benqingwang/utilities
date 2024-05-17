from bs4 import BeautifulSoup

# Function to read and parse HTML file
def parse_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'lxml')

    # Extract h1, h2, h3 tags
    headers = soup.find_all(['h1', 'h2', 'h3'])

    # Extract all tables
    tables = soup.find_all('table')

    return headers, tables

# Path to your HTML file
file_path = 'yourfile.html'

# Parse the file
headers, tables = parse_html(file_path)

# Print the extracted headers
print("Headers:")
for header in headers:
    print(header.name, header.get_text(strip=True))

# Print the extracted tables
print("\nTables:")
for i, table in enumerate(tables, start=1):
    print(f"Table {i}:")
    print(table.prettify())
