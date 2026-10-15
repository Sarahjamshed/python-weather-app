# Weather App Using Python

A desktop weather application built with Python and Tkinter that fetches current weather information for any city using the OpenWeather API.

## Features

- Search for weather by city name
- Display temperature in Celsius
- Show weather conditions
- Display humidity and wind speed
- Handle invalid city names and API errors
- Simple graphical user interface

## Technologies Used

- Python
- Tkinter
- Requests library
- OpenWeather API
- JSON

## How It Works

The application sends a request to the OpenWeather API using the city name entered by the user. The API returns weather data in JSON format. Python processes the response and displays the temperature, weather condition, humidity, and wind speed in the application window.

## Installation and Setup

1. Install Python on your computer.
2. Download or clone this repository.
3. Install the required library:

   `pip install -r requirements.txt`

4. Obtain an API key from OpenWeather.
5. Set the `OPENWEATHER_API_KEY` environment variable to your API key.
6. Run the application:

   `python weather.py`

## Project Purpose

This project demonstrates the use of external APIs, JSON data processing, Python libraries, error handling, and GUI development.

## Author

Created as part of a Python programming internship task.
