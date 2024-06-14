from tkinter import *
from tkinter import ttk
import requests

def data_get():
   city= city_name.get()
   data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=fccbee34028ef4cb0c4c7d3510a5c754").json()
   w_label1.config(text=data["weather"][0]["main"])
   wd_label1.config(text=data["weather"][0]["description"])
   temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
   per_label1.config(text=data["main"]["pressure"])

win= Tk()

win.title("Weather App")
win.config(bg ="#C1FFC1")
win.geometry("500x520")
name_label= Label(win,text=" WEATHER APPLICATION ",font=("Time New Roman",20,"bold"), bg="#8FBC8F")
name_label.place(x=25,y=50,height=50,width=420)


list_name =["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

city_name=StringVar()
com= ttk.Combobox(win,text=" WEATHER APPLICATION ",values=list_name,font=("Time New Roman",14,"bold"),textvariable=city_name)
com.place(x=25,y=120,height=50,width=420)

w_label= Label(win,text=" Weather Climate",font=("Time New Roman",15), bg="#8FBC8F")
w_label.place(x=25,y=260,height=50,width=200)
w_label1= Label(win,text="",font=("Time New Roman",15), bg="#8FBC8F")
w_label1.place(x=255,y=260,height=50,width=200)

wd_label= Label(win,text=" Weather description",font=("Time New Roman",15), bg="#8FBC8F")
wd_label.place(x=25,y=320,height=50,width=200)
wd_label1= Label(win,text="",font=("Time New Roman",15), bg="#8FBC8F")
wd_label1.place(x=255,y=320,height=50,width=200)

temp_label= Label(win,text=" Temperature",font=("Time New Roman",15), bg="#8FBC8F")
temp_label.place(x=25,y=380,height=50,width=200)
temp_label1= Label(win,text="",font=("Time New Roman",15), bg="#8FBC8F")
temp_label1.place(x=255,y=380,height=50,width=200)

per_label= Label(win,text=" Pressure",font=("Time New Roman",15), bg="#8FBC8F")
per_label.place(x=25,y=440,height=50,width=200)
per_label1= Label(win,text="",font=("Time New Roman",15), bg="#8FBC8F")
per_label1.place(x=255,y=440,height=50,width=200)


done_button= Button(win,text="Done",font=("Time New Roman",14,"bold"),command=data_get)
done_button.place(x=200,y=190,height=50,width=100,)



win.mainloop()


