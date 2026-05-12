import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = "YOUR_API_KEY_HERE"

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
def get_weather():
    """
    Fetches weather information for the entered city
    and displays it in the GUI.
    """
    city = city_entry.get().strip()
    if city == "":
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        data = response.json()
        if response.status_code == 200:
            city_name = data["name"]
            country = data["sys"]["country"]
            temperature = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]
            pressure = data["main"]["pressure"]
            description = data["weather"][0]["description"].title()
            wind_speed = data["wind"]["speed"]

            result = (
                f"Weather in {city_name}, {country}\n"
                f"{'-' * 40}\n"
                f"Temperature : {temperature} °C\n"
                f"Feels Like  : {feels_like} °C\n"
                f"Humidity    : {humidity}%\n"
                f"Pressure    : {pressure} hPa\n"
                f"Condition   : {description}\n"
                f"Wind Speed  : {wind_speed} m/s"
            )

            result_label.config(text=result)
        elif response.status_code == 401:
            messagebox.showerror(
                "API Error",
                "Invalid API Key.\n"
                "If you created the key recently, wait 10-30 minutes."
            )

        elif response.status_code == 404:
            messagebox.showerror(
                "City Not Found",
                "Please enter a valid city name."
            )
        else:
            error_message = data.get("message", "Unable to fetch weather data.")
            messagebox.showerror("API Error", error_message.title())
    except requests.exceptions.ConnectionError:
        messagebox.showerror(
            "Connection Error",
            "No internet connection.\nPlease check your network."
        )
    except requests.exceptions.Timeout:
        messagebox.showerror(
            "Timeout Error",
            "The request timed out.\nPlease try again."
        )
    except Exception as e:
        messagebox.showerror(
            "Unexpected Error",
            f"An unexpected error occurred:\n{e}"
        )

def clear_data():
    """
    Clears the city input and result display.
    """
    city_entry.delete(0, tk.END)
    result_label.config(text="Weather details will appear here.")
    city_entry.focus()
root = tk.Tk()
root.title("Weather API Integration App")
root.geometry("550x560")
root.resizable(False, False)
root.configure(bg="#EAF6FF")
title_label = tk.Label(
    root,
    text="Weather Information App",
    font=("Arial", 22, "bold"),
    bg="#EAF6FF",
    fg="#003366"
)
title_label.pack(pady=20)
city_label = tk.Label(
    root,
    text="Enter City Name:",
    font=("Arial", 12, "bold"),
    bg="#EAF6FF"
)
city_label.pack()
city_entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=30,
    justify="center"
)
city_entry.pack(pady=10)
city_entry.focus()
search_button = tk.Button(
    root,
    text="Get Weather",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    width=15,
    command=get_weather
)
search_button.pack(pady=5)
clear_button = tk.Button(
    root,
    text="Clear",
    font=("Arial", 12, "bold"),
    bg="#F44336",
    fg="white",
    width=15,
    command=clear_data
)
clear_button.pack(pady=5)
result_label = tk.Label(
    root,
    text="Weather details will appear here.",
    font=("Courier New", 11),
    bg="white",
    fg="black",
    width=48,
    height=12,
    justify="left",
    anchor="nw",
    relief="solid",
    bd=2,
    padx=10,
    pady=10
)
result_label.pack(pady=20)
city_entry.bind("<Return>", lambda event: get_weather())
root.bind("<Escape>", lambda event: clear_data())

root.mainloop()