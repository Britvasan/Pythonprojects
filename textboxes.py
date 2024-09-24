#adding values in a textboxes
import tkinter.messagebox
from tkinter import *
obj=Tk()
obj.geometry("1000x500")
obj.title("Textbox")
obj.configure(bg="lightblue")

def add():
    a1=num1.get()
    b1=num2.get()
    
    result=a1+b1
    
    tkinter.messagebox.showinfo("Result","Total value:"+str(result))
    
def sub():
    a1=num1.get()
    b1=num2.get()
    
    result=a1-b1
    
    tkinter.messagebox.showinfo("Result","Total value:"+str(result))
    
def mul():
    a1=num1.get()
    b1=num2.get()
    
    result=a1*b1
    
    tkinter.messagebox.showinfo("Result","Total value:"+str(result))
    
def div():
    a1=num1.get()
    b1=num2.get()
    
    result=a1/b1
    
    tkinter.messagebox.showinfo("Result","Total value:"+str(result))
    

#title
Label(obj,text="Calculator",font=("calibri",20),bg="red",fg="black").place(x=400,y=30)


#declaring textvariables
num1=IntVar()
num2=IntVar()
#1st label and textbox
Label(obj,text="Enter no.1:",font=("calibri",15),width="10",height="2",bg="lightblue").place(x=60,y=70)
Entry(obj,textvariable=num1,font=("calibri",15),width="10",bg="white").place(x=170,y=80)

#2st label and textbox
Label(obj,text="Enter no.2:",font=("calibri",15),width="10",height="2",bg="lightblue").place(x=60,y=140)
Entry(obj,textvariable=num2,font=("calibri",15),width="10",bg="white").place(x=170,y=150)

#adding button for add
B1=Button(obj,text="+",font=("calibri",15),width=10,height=1,bg="red",fg="black",command=add)
B1.place(x=400,y=250)

B2=Button(obj,text="-",font=("calibri",15),width=10,height=1,bg="red",fg="black",command=sub)
B2.place(x=400,y=310)

B3=Button(obj,text="*",font=("calibri",15),width=10,height=1,bg="red",fg="black",command=mul)
B3.place(x=400,y=370)

B4=Button(obj,text="/",font=("calibri",15),width=10,height=1,bg="red",fg="black",command=div)
B4.place(x=400,y=430)



obj.mainloop()