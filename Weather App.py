# Imports tkinter and requests modules
import tkinter as tk
import requests
from PIL import ImageTk, Image
import urllib.request
import socket

# Main window properties
root = tk.Tk()
root.geometry("300x500")
root.title("Weather")
root.resizable(False, False)


def get_weather(city):
    # Gets current temp for a given city
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=6d85d3bf2552548ce1a6d7930c5a3048&units=metric"
    data = requests.get(url).json()
    temp = data["main"]["temp"]
    fahrenheit = (temp * 9/5) + 32
    return int(fahrenheit)


def weather_desc(city):
    # Gets current weather description
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=6d85d3bf2552548ce1a6d7930c5a3048&units=metric"
    data = requests.get(url).json()
    desc = data["weather"][0]["description"]
    return desc


def temp_high(city):
    # Gets current temp high for given city
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=6d85d3bf2552548ce1a6d7930c5a3048&units=metric"
    data = requests.get(url).json()
    high = data["main"]["temp_max"]
    high_f = (high * 9/5) + 32
    return int(high_f)


def temp_low(city):
    # Gets current temp low for given city
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=6d85d3bf2552548ce1a6d7930c5a3048&units=metric"
    data = requests.get(url).json()
    low = data["main"]["temp_min"]
    low_f = (low * 9/5) + 32
    return int(low_f)


def get_location(city):
    # Gets City Label for a given city
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=6d85d3bf2552548ce1a6d7930c5a3048&units=metric"
    data = requests.get(url).json()
    city_2 = data["name"]
    return city_2


def get_country(city):
    # Gets Country for a given city
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=6d85d3bf2552548ce1a6d7930c5a3048&units=metric"
    data = requests.get(url).json()
    country = data["sys"]["country"]
    return country


def get_icon(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=6d85d3bf2552548ce1a6d7930c5a3048&units=metric"
    data = requests.get(url).json()
    icon_url = f"https://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png"
    response = requests.get(icon_url)
    with open("icon.png", "wb") as f:
        f.write(response.content)
    icon = ImageTk.PhotoImage(Image.open("icon.png"))
    return icon


def update_weather():
    # Executes all the functions and updates results
    city = city_entry.get().capitalize()
    city_label.config(text=f"{city}", font=("Arial", 13))
    desc_label.config(text=f"{weather_desc(city)}")
    temp_label.config(text=f"{get_weather(city)}°")
    high_data_label.config(text=f"H:{temp_high(city)}°")
    low_data_label.config(text=f"L:{temp_low(city)}°")
    icon = get_icon(city)
    icon_label.config(image=icon)
    icon_label.image = icon


city_label = tk.Label(root, text="", font=("Arial", 13))
city_label.place(x=150, y=15, anchor="center")

city_entry = tk.Entry(root, )
city_entry.place(x=220, y=445, width=76.5)

button = tk.Button(root, text="Get Weather", command=update_weather)
button.place(x=220, y=470)

desc_label = tk.Label(root, text="", font=("Arial", 13))
desc_label.place(x=150, y=85, anchor="center")

temp_label = tk.Label(root, text="", font=("Arial", 30))
temp_label.place(x=150, y=50, anchor="center")

high_label = tk.Label(root, text="", font=("Arial", 13))
high_label.place(x=125, y=110, anchor="center")

high_data_label = tk.Label(root, text="", font=("Arial", 13))
high_data_label.place(x=125, y=110, anchor="center")

low_label = tk.Label(root, text="", font=("Arial", 13))
low_label.place(x=175, y=110, anchor="center")

low_data_label = tk.Label(root, text="", font=("Arial", 13))
low_data_label.place(x=175, y=110, anchor="center")

icon_label = tk.Label(root, )
icon_label.place(x=120, y=200)

root.mainloop()
