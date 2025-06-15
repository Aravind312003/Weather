import tkinter as tk
import requests


API_KEY = '1b2a907ece97955b8b7d2803334786d1'

def get_weather():
    city = city_entry.get()
    if not city:
        result_label.config(text="Please enter a city name.")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            result_label.config(text=data["message"].capitalize())
            return

        weather = data["weather"][0]["description"].title()
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]

        result = (
            f"Weather: {weather}\n"
            f"Temperature: {temp}°C\n"
            f"Feels like: {feels_like}°C\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind} m/s"
        )

        result_label.config(text=result)

    except Exception as e:
        result_label.config(text="Error retrieving data")
        
root = tk.Tk()
root.title("Weather App")
root.geometry("300x350")
root.resizable(False, False)

tk.Label(root, text="Enter City Name:", font=("Helvetica", 12)).pack(pady=10)

city_entry = tk.Entry(root, width=25, font=("Helvetica", 12))
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", command=get_weather, font=("Helvetica", 12)).pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 11), justify="left")
result_label.pack(pady=10)

root.mainloop()