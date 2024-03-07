# Simple Python program for a basic web scraper
#Before running the code, make sure to install the required libraries using:
#pip install beautifulsoup4 requests
#Once installed, you can run the script and provide the URL of a website you'd like to scrape. 

import requests
from bs4 import BeautifulSoup

def web_scraper():
    print("Enter the URL of the website to scrape:")
    url = input()

    try:
        # Make an HTTP request to the specified URL
        response = requests.get(url)
        response.raise_for_status()

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract and display information
        print(f"\nFetching data from {url}...\n")
        print(f"Extracted Information:")
        print(f"- Title: {soup.title.string}")

        paragraphs = soup.find_all('p')
        print("- Paragraphs:")
        for i, paragraph in enumerate(paragraphs, 1):
            print(f"  {i}. {paragraph.get_text()}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    web_scraper()
