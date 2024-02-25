from tkinter import *
from tkinter import ttk
import requests

def data_set():
    city = city_name.get()
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=20a01944eda34a13f4a4dcecfff77197"
    data = requests.get(url).json()
    w_label1.config(text=data["weather"][0]['main'])
    wb_label1.config(text=data['weather'][0]['description'])
    temp_label1.config(text=round((data['main']["temp"]-273.15),2))
    per_label1.config(text=data['main']["pressure"])



win = Tk()
win.title("CHECK WEATHER")
win.config(bg='blue')
win.geometry("500x600")

name_label = Label(win,text="SkyCast App", font=('Time New Roman',30,'bold'))
name_label.place(x=25,y=50,height=50,width=450)

list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry",'Kolkata']
list_name.sort()


city_name = StringVar()
com = ttk.Combobox(win,text="SkyCast App", font=('Time New Roman',20,'bold'),values=list_name,textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)



w_label = Label(win,text="Weather Climate", font=('Time New Roman',15))
w_label.place(x=30,y=270,height=50,width=210)
w_label1 = Label(win,text="", font=('Time New Roman',15))
w_label1.place(x=250,y=270,height=50,width=210)



wb_label = Label(win,text="Weather Description", font=('Time New Roman',15))
wb_label.place(x=30,y=340,height=50,width=210)
wb_label1 = Label(win,text="", font=('Time New Roman',15))
wb_label1.place(x=250,y=340,height=50,width=210)



temp_label = Label(win,text="Temperature", font=('Time New Roman',15))
temp_label.place(x=30,y=410,height=50,width=210)
temp_label1 = Label(win,text="", font=('Time New Roman',15))
temp_label1.place(x=250,y=410,height=50,width=210)



per_label = Label(win,text="Pressure", font=('Time New Roman',15))
per_label.place(x=30,y=480,height=50,width=210)
per_label1 = Label(win,text="", font=('Time New Roman',15))
per_label1.place(x=250,y=480,height=50,width=210)


done_button = Button(win,text="Done", font=('Time New Roman',20,'bold'),command=data_set)
done_button.place(x=180,y=200,height=40,width=150)


win.mainloop()
