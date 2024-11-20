Jonathan C | 2024 Weather App Portfolio

The Weather App allows users to check the current weather and forecast for any city. It uses the OpenWeather API to fetch weather data, including temperature, wind speed, humidity, and weather descriptions. The app provides a 5-day forecast with details like temperature, conditions, and corresponding weather icons. It also includes a search feature to find cities by name.
Features

    Weather Search: Search for weather information by city name.
    Current Weather: Displays current temperature, humidity, wind speed, and weather conditions.
    5-Day Forecast: View a 5-day weather forecast with temperature and conditions.
    Weather Icons: Displays corresponding weather icons for each weather condition (clear, rain, snow, etc.).
    Error Handling: Shows error messages if the city is not found or if there are any issues fetching data.

Requirements

    Python 3.11 or higher
    Django 5.1.3
    requests library for making API calls
    python-decouple for managing environment variables

Setup Instructions
Step 1: Clone the Repository

Clone the repository to your local machine:

    git clone https://github.com/M1ster-J/Portfolio
    cd Portfolio

Step 2: Install Dependencies

Install the required Python packages:

    pip install -r requirements.txt

Step 3: Set Up Environment Variables

Create a .env file in the root of your project to store your sensitive information. This file should contain the following variables:

    API_KEY=<your-openweathermap-api-key>
    DEBUG=True   # Set to False in production
    ALLOWED_HOSTS=portfolio-weather-project.onrender.com  # Replace with your domain
    SECRET_KEY=<your-secret-key>
    DATABASE_URL=<your-database-url>  # For PostgreSQL or other database setup

You can get your API_KEY by signing up at OpenWeatherMap.
Step 4: Run Database Migrations

Run the following command to apply any database migrations:

    python manage.py migrate

Step 5: Start the Development Server

To run the app locally, use the following command:

    python manage.py runserver

Then access the app in your web browser by navigating to http://127.0.0.1:8000.
API Overview

The app uses the OpenWeatherMap API to fetch the current weather and forecast data. Here’s how it works:

    Geocode API: Converts city names into geographic coordinates (latitude and longitude).
    Weather API: Retrieves the current weather based on city coordinates or name.
    Forecast API: Fetches a 5-day forecast for the selected city.

The URLs used to access these APIs are:

    Current Weather: http://api.openweathermap.org/data/2.5/weather
    5-Day Forecast: http://api.openweathermap.org/data/2.5/forecast
    Geocoding: https://nominatim.openstreetmap.org/search

Weather Conditions and Icons

The weather conditions are mapped to corresponding weather icons:

    weather_icon_map = {
     "clear": "cloudy-1-day.svg",
    "clouds": "cloudy.svg",
    "rain": "rainy-1.svg",
    "snow": "snowy-1.svg",
    "drizzle": "rainy-2.svg",
    "thunderstorm": "thunderstorms.svg",
    "fog": "fog.svg",
}

Project Structure

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

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request with your changes. Please ensure your changes are well-documented and tested.
License

This project is licensed under the MIT License – see the LICENSE file for details.

Feel free to make any additional adjustments or let me know if you'd like to add anything else!
