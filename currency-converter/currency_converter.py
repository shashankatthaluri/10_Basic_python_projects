# Simple Python program for a currency converter

import requests

class CurrencyConverter:
    def __init__(self):
        self.exchange_rates = {}

    def fetch_exchange_rates(self):
        # Fetch real-time exchange rates from a currency API (e.g., exchangerate-api.com)
        api_key = "your_api_key"  # Replace with your API key
        base_url = f"https://open.er-api.com/v6/latest/{api_key}"

        try:
            response = requests.get(base_url)
            response.raise_for_status()

            data = response.json()
            self.exchange_rates = data.get("rates", {})
        except requests.exceptions.RequestException as e:
            print(f"Error fetching exchange rates: {e}")

    def convert_currency(self, amount, source_currency, target_currency):
        source_rate = self.exchange_rates.get(source_currency, 1.0)
        target_rate = self.exchange_rates.get(target_currency, 1.0)

        converted_amount = amount / source_rate * target_rate
        return round(converted_amount, 2)

def main():
    print("Welcome to Currency Converter!")

    converter = CurrencyConverter()

    # Fetch real-time exchange rates
    converter.fetch_exchange_rates()

    # Perform currency conversion
    amount = float(input("Enter the amount: "))
    source_currency = input("Enter the source currency code (e.g., USD): ").upper()
    target_currency = input("Enter the target currency code (e.g., EUR): ").upper()

    converted_amount = converter.convert_currency(amount, source_currency, target_currency)

    print(f"\nConverting {amount} {source_currency} to {target_currency}...")
    print(f"Result: {converted_amount} {target_currency}")

if __name__ == "__main__":
    main()
