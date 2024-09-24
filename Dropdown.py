from tkinter import *
from tkinter import ttk

#binding values in a dropdown
obj=Tk()
obj.geometry("400x300")
obj.title("Dropdownlist")
obj.configure(bg="aqua")

#assigning values in a dropdown
def values(selected):
    dropmenu2.set_menu(*options2.get(selected))
    
#adding label1 and optionmenu1
Label(obj,text="select the state:",font=("calibri",15),bg="aqua").place(x=20,y=30)
dropvar1=StringVar()

options1=["Andhra Pradesh","Goa","Karnataka","Kerala","Tamilnadu"]

dropmenu1=ttk.OptionMenu(obj,dropvar1,"-----select-----",*options1,command=values)
dropmenu1.place(x=200,y=30)

#adding label2 and optionmenu2
Label(obj,text="select the District:",font=("calibri",15),bg="aqua").place(x=20,y=100)

dropvar2=StringVar()

options2={
    "Andhra Pradesh":["Vijayawada","Chitoor","Nellore"],
    "Goa":["North Goa","South Goa"],
    "Karnataka":["Bangalore","Mysore","Kolar"],
    "Kerala":["Ernakulam","Cochin","Azhapuzha"],
    "Tamilnadu":["Chennai","Coimbatore","Madurai"]
    }

dropmenu2=ttk.OptionMenu(obj,dropvar2,"-----select-----")
dropmenu2.place(x=200,y=100)

obj.mainloop()


