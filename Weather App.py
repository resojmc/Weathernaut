# Imports tkinter and requests modules
import tkinter as tk
import requests
from PIL import ImageTk, Image
import urllib.request

# Initializes main window
root = tk.Tk()

# Title and window dimensions
root.geometry("250x200")
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
    urllib.request.urlretrieve(icon_url, "icon.png")
    icon = ImageTk.PhotoImage(Image.open("icon.png"))
    return icon


def update_weather():
    # Executes all the functions and updates results
    city = city_entry.get()
    desc_label.config(text=f"{weather_desc(city)}")
    temp_label.config(text=f"{get_weather(city)}°F")
    high_data_label.config(text=f"{temp_high(city)}°F")
    low_data_label.config(text=f"{temp_low(city)}°F")
    country_data_label.config(text=f"{get_country(city)}")
    icon_label.config(image=get_icon(city), width=50, height=50)


city_label = tk.Label(root, text="Enter City:", font=("Arial", 13))
city_label.place(x=0, y=2)

city_entry = tk.Entry(root, )
city_entry.place(x=160, y=4.5, width=76.5)

button = tk.Button(root, text="Get Weather", command=update_weather)
button.place(x=160, y=160)

description_label = tk.Label(root, text="Current Status:", font=("Arial", 13))
description_label.place(x=0, y=30)

desc_label = tk.Label(root, text="", font=("Arial", 13))
desc_label.place(x=112, y=42, anchor="w")

temperature_label = tk.Label(
    root, text="Temperature:", font=("Arial", 13)).place(x=0, y=59)

temp_label = tk.Label(root, text="", font=("Arial", 13))
temp_label.place(x=140, y=60)

high_label = tk.Label(root, text="High:", font=("Arial", 13))
high_label.place(x=0, y=88)

high_data_label = tk.Label(root, text="", font=("Arial", 13))
high_data_label.place(x=45, y=89)

low_label = tk.Label(root, text="Low:", font=("Arial", 13))
low_label.place(x=100, y=88)

low_data_label = tk.Label(root, text="", font=("Arial", 13))
low_data_label.place(x=140, y=89)

country_label = tk.Label(root, text="Country:", font=("Arial", 13))
country_label.place(x=0, y=120)

country_data_label = tk.Label(root, text="", font=("Arial", 13))
country_data_label.place(x=70, y=120)

icon_label = tk.Label(root, )
icon_label.place(x=120, y=110)

root.mainloop()
