
import os
import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather():
    city = city_entry.get().strip()

    if not city:
        messagebox.showwarning(
            "Missing City",
            "Please enter a city name."
        )
        return

    if not API_KEY:
        messagebox.showerror(
            "API Key Missing",
            "Please configure your OpenWeather API key."
        )
        return

    search_button.config(state="disabled", text="Loading...")
    root.update_idletasks()

    try:
        response = requests.get(
            BASE_URL,
            params={
                "q": city,
                "appid": API_KEY,
                "units": "metric"
            },
            timeout=10
        )

        if response.status_code == 200:
            data = response.json()

            city_label.config(text=data["name"])
            temp_label.config(
                text=f"{data['main']['temp']:.1f}°C"
            )
            condition_label.config(
                text=data["weather"][0]["description"].title()
            )
            humidity_label.config(
                text=f"Humidity\n{data['main']['humidity']}%"
            )
            wind_label.config(
                text=f"Wind Speed\n{data['wind']['speed']} m/s"
            )

        elif response.status_code == 404:
            messagebox.showerror(
                "City Not Found",
                "Please check the city name and try again."
            )

        elif response.status_code == 401:
            messagebox.showerror(
                "API Error",
                "The API key is invalid or not active yet."
            )

        else:
            messagebox.showerror(
                "Error",
                f"Weather request failed: {response.status_code}"
            )

    except requests.exceptions.Timeout:
        messagebox.showerror(
            "Timeout",
            "The request took too long. Try again."
        )

    except requests.exceptions.RequestException:
        messagebox.showerror(
            "Connection Error",
            "Please check your internet connection."
        )

    finally:
        search_button.config(state="normal", text="Search")


# Create the application window
root = tk.Tk()
root.title("Weather App")
root.geometry("420x540")
root.resizable(False, False)
root.configure(bg="#172554")

# Heading
heading = tk.Label(
    root,
    text="WEATHER APP",
    font=("Arial", 22, "bold"),
    fg="white",
    bg="#172554"
)
heading.pack(pady=(25, 5))

subtitle = tk.Label(
    root,
    text="Discover the weather in any city",
    font=("Arial", 10),
    fg="#bfdbfe",
    bg="#172554"
)
subtitle.pack(pady=(0, 20))

# City search field
search_frame = tk.Frame(root, bg="#172554")
search_frame.pack(padx=20, fill="x")

city_entry = tk.Entry(
    search_frame,
    font=("Arial", 12),
    justify="center"
)
city_entry.pack(fill="x", ipady=8, pady=(0, 10))

search_button = tk.Button(
    search_frame,
    text="Search",
    font=("Arial", 11, "bold"),
    bg="#60a5fa",
    fg="#172554",
    activebackground="#93c5fd",
    relief="flat",
    cursor="hand2",
    command=get_weather
)
search_button.pack(fill="x", ipady=5)

# Weather information
city_label = tk.Label(
    root,
    text="Search for a city",
    font=("Arial", 19, "bold"),
    fg="white",
    bg="#172554"
)
city_label.pack(pady=(25, 0))

temp_label = tk.Label(
    root,
    text="--°C",
    font=("Arial", 42, "bold"),
    fg="white",
    bg="#172554"
)
temp_label.pack(pady=5)

condition_label = tk.Label(
    root,
    text="Weather condition",
    font=("Arial", 13),
    fg="#bfdbfe",
    bg="#172554"
)
condition_label.pack(pady=(0, 20))

# Humidity and wind details
details_frame = tk.Frame(root, bg="#1e3a8a")
details_frame.pack(padx=20, fill="x", ipady=15)

humidity_label = tk.Label(
    details_frame,
    text="Humidity\n--%",
    font=("Arial", 12, "bold"),
    fg="white",
    bg="#1e3a8a",
    width=15
)
humidity_label.pack(side="left", expand=True, pady=12)

wind_label = tk.Label(
    details_frame,
    text="Wind Speed\n-- m/s",
    font=("Arial", 12, "bold"),
    fg="white",
    bg="#1e3a8a",
    width=15
)
wind_label.pack(side="right", expand=True, pady=12)

# Footer
footer = tk.Label(
    root,
    text="Live weather powered by OpenWeather",
    font=("Arial", 9),
    fg="#bfdbfe",
    bg="#172554"
)
footer.pack(side="bottom", pady=15)

# Allow Enter key to search
city_entry.bind("<Return>", lambda event: get_weather())

root.mainloop()



