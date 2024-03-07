# Project 6: Weather App ☁️

## Overview

This Python program fetches weather data from an API based on a user-provided location. It uses the OpenWeatherMap API to retrieve and display current weather information.

## Features

- Retrieves and displays weather data for a specified location.
- Utilizes the requests library to make API requests.
- Requires an API key from OpenWeatherMap.

## How to Run 🚀

Clone the repository:

   ```bash
   git clone https://github.com/shashankatthaluri/10_Basic_python_projects/weather-app.git
   ```
Navigate to the project directory:

```bash
cd weather-app
```
Install the required libraries:

```bash
pip install requests
```

Obtain an API key from OpenWeatherMap:

Sign up for a free account: https://openweathermap.org/appid
Copy your API key.
Create a file named config.py in the project directory and add your API key:

```python
# config.py
API_KEY = "your_openweathermap_api_key"
```
Run the Python script:

```bash
python weather_app.py
```

Follow the prompts to enter the location and see the current weather.

Example
```bash
$ python weather_app.py

Enter the location (city, country): London, UK

Fetching weather data for London, UK...

Current Weather:
- Temperature: 14°C
- Description: Light rain
- Humidity: 82%
- Wind Speed: 5.1 m/s
```
