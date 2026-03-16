import requests
from bs4 import BeautifulSoup

# Function to scrape data
def scrape_website(url):
    try:
        # Send a GET request to the website
        response = requests.get(url)
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the content with BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            # Extract data (example: all paragraph texts)
            paragraphs = [p.get_text() for p in soup.find_all('p')]
            return paragraphs
        else:
            print(f"Failed to retrieve data: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example use case
if __name__ == "__main__":
    url = "https://example.com"  # Replace with your target URL
    data = scrape_website(url)
    for item in data:
        print(item)