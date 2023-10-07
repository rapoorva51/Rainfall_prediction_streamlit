import tkinter as tk
import requests
import time

canvas = tk.Tk()
canvas.geometry('600x500')
canvas.title("Weather Finder")  # Change the title of the application

# Change the title font and color
canvas.title_font = ("Arial", 20, "bold")
canvas.title("WorldWeather")

# Define font styles and colors
f = ("Arial", 15, "italic")
s = ("Arial", 15, "bold")
t = ("Arial", 35, "bold")
text_color = "#588c73"
background_color = "#f7e0a3"

canvas.configure(bg=background_color)  # Set the background color for the main window

# Label for user to input city name
city_label = tk.Label(canvas, text="Location based weather forecasting.", font=s, fg="#44558f", bg=background_color)
city_label.pack(pady=20)

# Entry field for the city name
textfield = tk.Entry(canvas, justify='center', font=t, fg=text_color, bg=background_color)
textfield.pack()

# Labels with custom colors
label1 = tk.Label(canvas, font=t, fg="#cc7f2a", bg=background_color)
label1.pack()

label2 = tk.Label(canvas, font=s, fg="#d96459", bg=background_color)
label2.pack()


# Function to get weather data and update labels
def getWeather():
    city = textfield.get()
    api = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&APPID=a2629a1542bac83f36f720085be6622b"
    json_data = requests.get(api).json()
    condition = json_data["weather"][0]["main"]
    temp = int(json_data["main"]["temp"] - 273.15)
    min_temp = int(json_data["main"]["temp_min"] - 273.15)
    max_temp = int(json_data["main"]["temp_max"] - 273.15)
    pressure = json_data["main"]["pressure"]
    humidity = json_data['main']['humidity']
    wind = json_data["wind"]["speed"]
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] - 21600))

    final_info = condition + "\n" + str(temp) + "°C"
    final_data = "\n" + "Max Temp : " + str(max_temp) + "°C" + "\n" + "Min Temp : " + str(min_temp) + "°C" + "\n" + "Pressure : " + str(
        pressure) +  "hPa" + "\n" + "Humidity : " + str(humidity) +  "%" + "\n" + "Wind speed : " + str(wind) +  "m/s" + "\n" + "Sunrise : " + str(
        sunrise) + "\n" + "Sunset : " + str(sunset)

    # Configure label text and colors
    label1.config(text=final_info)
    label2.config(text=final_data)

    city_label.grid_remove()
# Bind the Enter key to getWeather
textfield.bind('<Return>', lambda event: getWeather())

canvas.mainloop()