# Imports tkinter, requests, and json modules
import tkinter as tk
import requests

# Creates 300x600 window with title
root = tk.Tk()
root.title("Weather App")
root.geometry("300x600")

def get_weather(city):
    # A function to get the current weather for a city
    api_key = "6d85d3bf2552548ce1a6d7930c5a3048"
    default_url = "https://api.openweathermap.org/data/2.5/weather?"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    data = requests.get(url).json()
    temp_kelvin = data["main"]["temp"]
    temp_kelvin = temp_kelvin - 273.15
    temp_fahrenheit = (temp_kelvin * 9//5) + 32
    return temp_fahrenheit

def update_temperature():
    # a Function that Updates temperature
    city = city_entry.get()
    temperature = get_weather(city)
    temperature_label.config(text=f"Temperature: {temperature}°F")

# Label to indicate entry box
city_label = tk.Label(root, text="City")
city_label.pack()

# Entry box to input city
city_entry = tk.Entry(root,)
city_entry.pack()

# Button to update weather data
button = tk.Button(root, text="Get Weather", command=update_temperature)
button.pack()

# Label that displays temperature
temperature_label = tk.Label(root, text="Temperature: ")
temperature_label.pack()

# Executes main loop
root.mainloop()