from datetime import datetime
import requests
import os


def get_weather_data(city, country):
    api_key = os.environ.get("OPENWEATHER_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}&units=metric"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
        icon_code = weather_data['weather'][0]['icon']
        weather_data['icon_code'] = icon_code
        return weather_data
    else:
        return None


def get_greeting():
    current_hour = datetime.now().hour
    if 5 <= current_hour < 12:
        return "Good morning!"
    elif 12 <= current_hour < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"


def home_view(request):
    greeting = get_greeting()
    weather_data = get_weather_data("Kendal", "GB")

    return render(
        request, 'home/home.html',
        {'greeting': greeting, 'weather_data': weather_data})
