#Add,sub,mul,div values in a textboxes
import tkinter.messagebox
from tkinter import *

call=Tk()
call.geometry("500x400")
call.title("Calculator")
call.configure(bg="gray")

#Performing +,-,*,/ operations
def add():
    x1=num1.get()
    x2=num2.get()
    result=x1+x2
    tkinter.messagebox.showinfo("Result","Answer:"+str(result))

def sub():
    x1=num1.get()
    x2=num2.get()
    result=x1-x2
    tkinter.messagebox.showinfo("Result","Answer:"+str(result))

def mul():
    x1=num1.get()
    x2=num2.get()
    result=x1*x2
    tkinter.messagebox.showinfo("Result","Answer:"+str(result))

def div():
    x1=num1.get()
    x2=num2.get()
    result=x1/x2
    tkinter.messagebox.showinfo("Result","Answer:"+str(result))

def reset():
    num1.set("")
    num2.set("")
    tkinter.messagebox.showinfo("Reset","values are reseted")

#Adding labels
Label(call, text="Enter value A: ", font=("calibri",20), bg="black", fg="white",width=11,height=1).place(x=30,y=50)
Label(call, text="Enter value B: ", font=("calibri",20), bg="black", fg="white",width=11,height=1).place(x=30,y=100)

#Declaring variables for textboxes
num1=IntVar()
num2=IntVar()


#Adding textboxes
Entry(call,textvariable=num1,font=("calibri",20),bg="white",fg="black",width=8).place(x=195,y=50)
Entry(call,textvariable=num2,font=("calibri",20),bg="white",fg="black",width=8).place(x=195,y=100)

#Adding buttons
b1=Button(call,text="+",font=("calibri",15),bg="orange",fg="black",width=3,height=1,command=add)
b1.place(x=30,y=200)

b2=Button(call,text="-",font=("calibri",15),bg="orange",fg="black",width=3,height=1,command=sub)
b2.place(x=100,y=200)

b3=Button(call,text="*",font=("calibri",15),bg="orange",fg="black",width=3,height=1,command=mul)
b3.place(x=170,y=200)

b4=Button(call,text="/",font=("calibri",15),bg="orange",fg="black",width=3,height=1,command=div)
b4.place(x=240,y=200)

Button(call,text="C",font=("calibri",15),bg="red",fg="black",width=3,height=1,command=reset).place(x=300,y=200)


call.mainloop()
