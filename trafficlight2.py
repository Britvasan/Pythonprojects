#traffic light Manual
from tkinter import *
show=Tk()
show.geometry("300x450")
show.title("Traffic light manual")
show.configure(bg="pink")

def red():
    canvas1.create_oval(90,90,10,10,width=0,outline="white",fill="red")
    canvas2.create_oval(90,90,10,10,width=0,outline="white",fill="white")
    canvas3.create_oval(90,90,10,10,width=0,outline="white",fill="white")

def yellow():
    canvas1.create_oval(90,90,10,10,width=0,outline="white",fill="white")
    canvas2.create_oval(90,90,10,10,width=0,outline="white",fill="yellow")
    canvas3.create_oval(90,90,10,10,width=0,outline="white",fill="white")
    
def green():
    canvas1.create_oval(90,90,10,10,width=0,outline="white",fill="white")
    canvas2.create_oval(90,90,10,10,width=0,outline="white",fill="white")
    canvas3.create_oval(90,90,10,10,width=0,outline="white",fill="green")

Button(show,text="RED",bg="red",fg="darkblue",width="8",height="2",command=red).place(x=30,y=30)
Button(show,text="YELLOW",bg="yellow",fg="darkblue",width="8",height="2",command=yellow).place(x=30,y=170)
Button(show,text="GREEN",bg="green",fg="darkblue",width="8",height="2",command=green).place(x=30,y=310)


canvas1=Canvas(show,width=100,height=100,bg="black")
canvas1.place(x=150,y=30)
canvas2=Canvas(show,width=100,height=100,bg="black")
canvas2.place(x=150,y=170)
canvas3=Canvas(show,width=100,height=100,bg="black")
canvas3.place(x=150,y=310)


show.mainloop()