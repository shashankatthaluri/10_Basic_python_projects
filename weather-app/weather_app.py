# Simple Python program for a weather app

import requests
from config import API_KEY

def get_weather_data(location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "appid": API_KEY,
        "units": "metric",  # Use "imperial" for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()

        weather_data = response.json()

        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']

        print(f"\nCurrent Weather:")
        print(f"- Temperature: {temperature}°C")
        print(f"- Description: {description}")
        print(f"- Humidity: {humidity}%")
        print(f"- Wind Speed: {wind_speed} m/s")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def main():
    print("Enter the location (city, country):")
    location = input()
    
    get_weather_data(location)

if __name__ == "__main__":
    main()
