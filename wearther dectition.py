from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city = city_name.get()
    data = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=20a01944eda34a13f4a4dcecfff77197").json()
    print(data)

    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(data["main"]["temp"] - 273.15))
    per_label1.config(text=str(data["main"]["pressure"]))


win = Tk()
win.title("Weather App")
win.config(bg="skyblue")
win.geometry("500x500")

name_label = Label(win, text="Weather Application",
                   font=("poppins", 24, "bold"))
name_label.place(x=25, y=50, height=50, width=450)

list_name = ["Andhra Pradesh", "Arunachal Pradesh ", "Assam", "Bihar", "Chhattisgarh", "Goa",
             "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka",
             "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland",
             "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura",
             "Uttar Pradesh", "Uttarakhand", "West Bengal", "Andaman and Nicobar Islands",
             "Chandigarh", "Dadra and Nagar Haveli", "Daman and Diu", "Lakshadweep",
             "National Capital Territory of Delhi", "Puducherry"]

city_name = StringVar()
com = ttk.Combobox(win, text="Weather Application", values=list_name,
                   font=("poppins", 20, "bold"), textvariable=city_name)

com.place(x=50, y=125, height=50, width=400)

# data
w_label = Label(win, text="Weather Climate",
                font=("poppins", 12))
w_label.place(x=25, y=280, height=35, width=180)

w_label1 = Label(win, text="",
                 font=("poppins", 12))
w_label1.place(x=300, y=280, height=35, width=180)

# label 2
wb_label = Label(win, text="Weather Description",
                 font=("poppins", 12))
wb_label.place(x=25, y=330, height=35, width=180)

wb_label1 = Label(win, text="",
                  font=("poppins", 12))
wb_label1.place(x=300, y=330, height=35, width=180)

# label 3
temp_label = Label(win, text="Temperature",
                   font=("poppins", 12))
temp_label.place(x=25, y=380, height=35, width=180)

temp_label1 = Label(win, text="",
                    font=("poppins", 12))
temp_label1.place(x=300, y=380, height=35, width=180)

# label 4
per_label = Label(win, text="Pressure",
                  font=("poppins", 12))
per_label.place(x=25, y=430, height=35, width=180)

per_label1 = Label(win, text="",
                   font=("poppins", 12))
per_label1.place(x=300, y=430, height=35, width=180)

done_button = Button(win, text="Done", font=("poppins", 16, "bold"), command=data_get)
done_button.place(x=200, y=200, height=50, width=100)

win.mainloop()
