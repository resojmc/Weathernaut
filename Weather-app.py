import tkinter as tk
import requests, json

def get_weather(city):
    api_key = "6d85d3bf2552548ce1a6d7930c5a3048"
    default_url = "https://api.openweathermap.org/data/2.5/weather?"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    data = response.get(url).json()
    celcius = data["main"]["temp"]
    fahrenheit = (celcius * 1.8) + 32
    return fahrenheit

def update_temperature():
    city = city_entry.get()
    temperature = get_weather(city)
    temperature_label.config(text=f"Temperature: {temperature}°F")
