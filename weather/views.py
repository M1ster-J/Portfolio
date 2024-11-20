from django.shortcuts import render
from datetime import datetime
import requests
import re
import os
from dotenv import load_dotenv

load_dotenv()

weather_icon_map = {
    "clear": "cloudy-1-day.svg",
    "clouds": "cloudy.svg",
    "rain": "rainy-1.svg",
    "snow": "snowy-1.svg",
    "drizzle": "rainy-2.svg",
    "thunderstorm": "thunderstorms.svg",
    "fog": "fog.svg",
}

def convert_wind_speed(mps):
    return round(mps * 2.23694)

def capitalize_all_words(text):
    return ' '.join([word.capitalize() for word in text.split()])

def get_weather(request):
    if request.method == "POST":
        city = request.POST.get('city', '').strip()
        if not city:
            return render(request, 'weather/weather.html', {"error_message": "City name cannot be empty."})
        
        api_key = os.getenv("API_KEY")
        current_url = "http://api.openweathermap.org/data/2.5/weather"
        forecast_url = "http://api.openweathermap.org/data/2.5/forecast"
        geocode_url = "https://nominatim.openstreetmap.org/search"

        try:
            geo_response = requests.get(
                geocode_url,
                params={"q": city, "format": "json", "addressdetails": 1, "limit": 1},
                headers={"User-Agent": "weather-app"}
            )
            geo_response.raise_for_status()
            geo_data = geo_response.json()

            if not geo_data:
                return render(request, 'weather/weather.html', {"error_message": "Location not found. Please try again."})

            city_name = geo_data[0]["address"].get("city", city)
            state_name = geo_data[0]["address"].get("state", "")
            country = geo_data[0]["address"].get("country_code", "").upper()

            current_response = requests.get(
                current_url,
                params={"q": city, "appid": api_key, "units": "imperial"}
            )
            current_response.raise_for_status()
            current_data = current_response.json()

            if current_data.get("cod") != 200:
                return render(request, 'weather/weather.html', {"error_message": "City not found. Please try again."})

            temperature = round(current_data["main"]["temp"])
            description = current_data["weather"][0]["description"]
            wind_speed_mps = current_data["wind"]["speed"]
            wind_speed = convert_wind_speed(wind_speed_mps)
            humidity = current_data["main"]["humidity"]
            icon_code = current_data["weather"][0]["icon"]
            condition = current_data["weather"][0]["main"].lower()
            icon_name = weather_icon_map.get(condition, "default.gif")

            forecast_response = requests.get(
                forecast_url,
                params={"q": city, "appid": api_key, "units": "imperial"}
            )
            forecast_response.raise_for_status()
            forecast_data = forecast_response.json()

            forecast_list = []
            for forecast in forecast_data["list"]:
                date = datetime.strptime(forecast["dt_txt"], "%Y-%m-%d %H:%M:%S").strftime("%m/%d/%Y")
                if date not in [f["date"] for f in forecast_list]:
                    condition = forecast["weather"][0]["main"].lower()  
                    icon_name = weather_icon_map.get(condition, "default.gif")  
                    forecast_list.append({
                        "date": date,
                        "temp": round(forecast["main"]["temp"]),
                        "description": forecast["weather"][0]["description"],
                        "icon_name": icon_name  
                    })
                if len(forecast_list) == 5:
                    break

            description = capitalize_all_words(description)

            for forecast in forecast_list:
                forecast["description"] = capitalize_all_words(forecast["description"])

            context = {
                "city_name": city_name,
                "state_name": state_name,
                "country": country,
                "temperature": temperature,
                "temperature_unit": "°F",
                "description": description,
                "wind_speed": wind_speed,
                "humidity": humidity,
                "icon_name": icon_name,
                "forecast_list": forecast_list
            }
            return render(request, 'weather/weather.html', context)

        except requests.exceptions.RequestException:
            return render(request, 'weather/weather.html', {"error_message": "Error fetching weather data. Please try again."})

    return render(request, 'weather/weather.html')
