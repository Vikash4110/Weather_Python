import requests
from tkinter import *
from tkinter import messagebox as mb

def getNotification():
    cityName = place.get()
    baseUrl = "http://api.openweathermap.org/data/2.5/weather?"
    apiKey = "d850f7f52bf19300a9eb4b0aa6b80f0d"
    try:
        url = baseUrl + "appid=" + apiKey + "&q=" + cityName  # complete url to get the weather details of the city
        response = requests.get(url)  # requesting the content of the url
        if response.status_code == 200:
            x = response.json()
            y = x['main']

            # getting the temperature key
            temp = y['temp']  # temp is in kelvin so we convert to Celsius
            temp -= 273.15

            pres = y["pressure"]
            hum = y["humidity"]
            z = x["weather"]

            weather_desc = z[0]['description']

            info = (
                f"Here is the weather description of {cityName}:\n"
                f"Temperature: {temp:.2f} Celsius\n"
                f"Atmospheric pressure = {pres} hPa\n"
                f"Humidity = {hum}%\n"
                f"Description of the weather = {weather_desc}"
            )

            mb.showinfo("Your Weather Report", info)
        else:
            mb.showerror("Error", "City not found or API request failed")

    except Exception as e:
        mb.showerror("Error", str(e))

# Creating a window
wn = Tk()
wn.title("Weather Desktop Notifier")
wn.geometry("700x200")
wn.config(bg='azure')

# Heading the label
Label(wn, text="Weather Desktop Notifier", font=("Courier", 15), fg='white').pack()
Label(wn, text="Enter the location", font=("Courier", 13), bg='blue',fg="white").pack()

place = StringVar(wn)
place_entry = Entry(wn, width=50, textvariable=place)
place_entry.place(relx=0.5, rely=0.3, anchor=CENTER)

btn = Button(wn, text="Get Notification", font=("Courier", 10), fg='grey19', command=getNotification)
btn.place(relx=0.5, rely=0.75, anchor=CENTER)

wn.mainloop()

