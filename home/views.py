from django.shortcuts import render
from django.utils import timezone
from .utils import get_greeting, get_weather_data


def home_view(request):
    # Get greeting based on the current time
    greeting = get_greeting()

    # Fetch weather data for a specific city
    city = "Kendal"
    weather = get_weather_data(city, "GB")

    # Render template with both greeting and weather data
    return render(request, 'home/home.html', {
        'greeting': greeting,
        'weather': weather
    })


def get_greeting():
    current_hour = timezone.now().hour
    if current_hour < 12:
        return "Good morning!"
    elif 12 <= current_hour < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"
