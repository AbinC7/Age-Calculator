from datetime import date
import customtkinter as tk
from tkinter import *

tk.set_appearance_mode("dark")
tk.set_default_color_theme("green")

root = tk.CTk()
root.geometry("500*350")
root.title("Age calculator")

def age():
    d1 = int(D.get())
    m1 = int(M.get())
    y1 = int(Y.get())
    month = [31,28,31,30,31,30,31,31,30,31,30,31]
    today = date.today()
    d2 = today.day
    m2 =  today.month
    y2 = today.year

    if (d1 > d2):
        d2 = d2 + month[m2-1]
        m2 = m2 - 1
    if (m1 > m2):
        m2 = m2 +12
        y2 = y2 - 1
      
    d = d2 - d1
    m = m2 - m1
    y = y2 - y1
    age = (y,"Years",m,"Months",d,"Days")
    label3.configure(text=age)

    
    
    
D = StringVar()
M = StringVar()
Y = StringVar()

frame = tk.CTkFrame(master = root)
frame.pack(pady= 20, padx= 60, fill="both", expand= True)

f1 = tk.CTkFrame(master = frame)
f1.pack(side = BOTTOM,pady=20,padx= 60, fill ="both",expand =True)

f2 = tk.CTkFrame(master= root)
f2.pack(pady = 20, padx = 30, fill= "both")

label = tk.CTkLabel(master= frame, text= "Age Calculator",font=("Roboto",24))
label.pack(pady =12, padx =10)

label2 = tk.CTkLabel(master= frame, text= "Enter your birth date here",font=("Roboto",12))
label2.pack(pady =4, padx =2)

entry1 = tk.CTkEntry(master = f1, placeholder_text="Day",textvariable = D,height = 4,width = 25)
entry1.pack(side = LEFT,pady =20, padx =15)

entry2 = tk.CTkEntry(master = f1, placeholder_text="Month",textvariable = M,height= 4, width = 25)
entry2.pack(side= LEFT,pady =12, padx =10)

entry3 = tk.CTkEntry(master = f1, placeholder_text="Year",textvariable = Y,height = 4, width =40)
entry3.pack(side = LEFT,pady =20, padx =15)

button = tk.CTkButton(master = f1, text= "Age",command= age)
button.pack(side= BOTTOM,pady =12, padx =10)

label3 = tk.CTkLabel(master = f2,text="")
label3.pack(side= BOTTOM)

if __name__=='__main__':
    root.mainloop()
    