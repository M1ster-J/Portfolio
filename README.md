Jonathan C | 2024
Weather App 
Portfolio

The Weather App allows users to check the current weather and forecast for any city. It uses the OpenWeather API to fetch weather data, including temperature, wind speed, humidity, and weather descriptions. The app provides a 5-day forecast with details like temperature, conditions, and corresponding weather icons. It also includes a search feature to find cities by name.

Requirements

    Python 3.11 or higher
    Django 5.1.3
    requests library for making API calls
    python-decouple 

Setup Instructions
Step 1: Clone the Repository

Step 2: Install Dependencies

Install the required Python packages by running:

pip install -r requirements.txt

Step 3: Set Up Environment Variables

Create a .env file in the root of your project to store your sensitive information. This file should contain the following variables:

API_KEY=<your-openweathermap-api-key>
DEBUG=False DEBUGGING | True / False
ALLOWED_HOSTS=portfolio-weather-project.onrender.com  # Replace with your domain
SECRET_KEY=<your-secret-key>
DATABASE_URL=<your-database-url>  # For PostgreSQL or other database setup

You can get your API key by signing up at OpenWeatherMap.
Step 4: Run Database Migrations

Run the following command to apply any database migrations:

python manage.py migrate

Step 5: Start the Development Server

To run the app locally for development, use the following command:

python manage.py runserver

Access the app in your web browser by navigating to http://127.0.0.1:8000.
API Overview

The app makes use of the OpenWeatherMap API to get the current weather and forecast data. Here's how the weather data is fetched:

    Geocode API: Converts city names into geographic coordinates (latitude and longitude).
    Weather API: Fetches current weather information based on city coordinates or name.
    Forecast API: Retrieves a 5-day forecast for the selected city.

The URLs used in the app to access these APIs are:

    Current Weather: http://api.openweathermap.org/data/2.5/weather
    5-Day Forecast: http://api.openweathermap.org/data/2.5/forecast
    Geocoding: https://nominatim.openstreetmap.org/search

Weather Conditions and Icons:

The weather conditions are mapped to corresponding weather icons as follows:

weather_icon_map = {
    "clear": "cloudy-1-day.svg",
    "clouds": "cloudy.svg",
    "rain": "rainy-1.svg",
    "snow": "snowy-1.svg",
    "drizzle": "rainy-2.svg",
    "thunderstorm": "thunderstorms.svg",
    "fog": "fog.svg",
}

weather_project/
├── weather/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   └── views.py
├── manage.py
├── weather_project/
│   └── settings.py
├── .env
├── requirements.txt
└── README.md

Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request with your changes. Please make sure your changes are well-documented and tested.

Let me know if you'd like to add or adjust anything in this README!