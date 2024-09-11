#traffic light-automatic
from tkinter import *
from time import sleep
play=Tk()
play.title("Traffic light automatic")
play.geometry("250x400")

count=30
def start():
    counter(count)
    
def intervals(c):
    if c>20:
        timerdata.place(x=20,y=130)
        red()
    elif c>15 and c<=20:
        timerdata.place(x=20,y=230)
        yellow()
    elif c>=0 and c<=15:
        timerdata.place(x=20,y=330)
        green()
    elif c==0:
        red()
    
    timerdata.config(text=c)
    play.update()
    play.after(1000,counter,c)
        
def counter(data):
    if data>0:
        data=data-1
        intervals(data)
    else:
        counter(30)

def red():
    canvas1.create_oval(35,35,65,65,fill="red")
    canvas2.create_oval(35,35,65,65,fill="black")
    canvas3.create_oval(35,35,65,65,fill="black")
    
    
def yellow():
    canvas1.create_oval(35,35,65,65,fill="black")
    canvas2.create_oval(35,35,65,65,fill="yellow")
    canvas3.create_oval(35,35,65,65,fill="black")

def green():
    canvas1.create_oval(35,35,65,65,fill="black")
    canvas2.create_oval(35,35,65,65,fill="black")
    canvas3.create_oval(35,35,65,65,fill="green")
    
    

Button(play,text="start",font=("calibri,15"),bg="gray",fg="white",width="10",height="1",command=start).place(x=80,y=30)

timerdata=Label(play,font=("calibri",25),bg="black",fg="white")
#timerdata.place(x=20,y=250)

canvas1=Canvas(play,width=100,height=100,bg="black")
canvas1.place(x=80,y=100)
canvas2=Canvas(play,width=100,height=100,bg="black")
canvas2.place(x=80,y=200)
canvas3=Canvas(play,width=100,height=100,bg="black")
canvas3.place(x=80,y=300)

play.mainloop()