# Simple Python program for a URL shortener

import hashlib

class URLShortener:
    def __init__(self):
        self.url_mapping = {}

    def generate_short_url(self, long_url):
        # Generate a unique short alias using MD5 hash
        hash_object = hashlib.md5(long_url.encode())
        short_url = "http://short.url/" + hash_object.hexdigest()[:6]

        # Store the mapping between short and long URLs
        self.url_mapping[short_url] = long_url

        return short_url

    def access_long_url(self, short_url):
        # Redirect to the original long URL
        return self.url_mapping.get(short_url, None)

def main():
    print("Welcome to URL Shortener!")

    shortener = URLShortener()

    # Shorten a URL
    long_url = input("Enter the long URL: ")
    short_url = shortener.generate_short_url(long_url)
    print(f"\nShortened URL: {short_url}")

    # Access the original URL
    access_url = input("\nEnter the short URL to access the original long URL: ")
    original_url = shortener.access_long_url(access_url)

    if original_url:
        print(f"\nRedirecting to: {original_url}")
    else:
        print("Short URL not found. Please check the entered URL.")

if __name__ == "__main__":
    main()
