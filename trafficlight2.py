#traffic light automatic
from tkinter import *
from time import sleep
show=Tk()
show.geometry("450x500")
show.title("Traffic light manual")
show.configure(bg="lightblue")

def red():
    #first traffic light
    canvas1.delete("all")
    canvas1.create_oval(40,20,100,80,width=0,outline="white",fill="red")
    canvas1.create_oval(40,100,100,160,width=0,outline="white",fill="white")
    canvas1.create_oval(40,180,100,240,width=0,outline="white",fill="white")
    #second traffic light
    canvas2.delete("all")
    canvas2.create_oval(40,20,100,80,width=0,outline="white",fill="white")
    canvas2.create_oval(40,100,100,160,width=0,outline="white",fill="yellow")
    canvas2.create_oval(40,180,100,240,width=0,outline="white",fill="white")

def yellow():
    #first traffic light
    canvas1.delete("all")
    canvas1.create_oval(40,20,100,80,width=0,outline="white",fill="white")
    canvas1.create_oval(40,100,100,160,width=0,outline="white",fill="yellow")
    canvas1.create_oval(40,180,100,240,width=0,outline="white",fill="white")
    #second traffic light
    canvas2.delete("all")
    canvas2.create_oval(40,20,100,80,width=0,outline="white",fill="white")
    canvas2.create_oval(40,100,100,160,width=0,outline="white",fill="white")
    canvas2.create_oval(40,180,100,240,width=0,outline="white",fill="green")
    
def green():
    #first traffic light
    canvas1.delete("all")
    canvas1.create_oval(40,20,100,80,width=0,outline="white",fill="white")
    canvas1.create_oval(40,100,100,160,width=0,outline="white",fill="white")
    canvas1.create_oval(40,180,100,240,width=0,outline="white",fill="green")
    #second traffic light
    canvas2.delete("all")
    canvas2.create_oval(40,20,100,80,width=0,outline="white",fill="red")
    canvas2.create_oval(40,100,100,160,width=0,outline="white",fill="white")
    canvas2.create_oval(40,180,100,240,width=0,outline="white",fill="white")
    
count=25

def start():
    counter(count)
    
def intervals(c):
    if c>15:
        red()
        timerdata.config(text=c)
        show.update()
        sleep(1)
        counter(c)
    elif c>10 and c<=15:
        yellow()
        timerdata.config(text=c)
        show.update()
        sleep(1)
        counter(c)
    elif c>0 and c<=10:
        green()
        timerdata.config(text=c)
        show.update()
        sleep(1)
        counter(c)
    elif c==0:
        red()
        timerdata.config(text=c)
        show.update()
        sleep(1)
        count=25
        counter(count)
        
def counter(data):
    if data>0:
        data=data-1
        intervals(data)
        
Button(show,text="Start",font=("calibri",15),bg="gray",fg="black",width="6",height="1",command=start).place(x=30,y=30)

timerdata=Label(show,font=("calibri",20,"bold"),bg="black",fg="red")
timerdata.place(x=50,y=150)

canvas1=Canvas(show,width=130,height=260,bg="black")
canvas1.place(x=150,y=30)
canvas2=Canvas(show,width=130,height=260,bg="black")
canvas2.place(x=300,y=30)

show.mainloop()