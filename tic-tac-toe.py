#XOXO Game
import tkinter.messagebox
from tkinter import *

Play=Tk()
Play.geometry("700x600")
Play.title("TIC-TAC-TOE")
Play.configure(bg="lightblue")

p1=StringVar()
p2=StringVar()
bclick=True
buttons=StringVar()
turns=0

def btnclick(buttons):
    global bclick,turns
    if buttons["text"]==" " and bclick==True:
        buttons["text"]="X"
        bclick=False
        possibilities()
        turns +=1

    elif buttons["text"]==" " and bclick==False:
        buttons["text"]="O"
        bclick=True
        possibilities()
        turns +=1

    else:
        tkinter.messagebox.showerror("TIC-TAC-TOE","Buttons already clicked!...")

def possibilities():
    if(b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X" or
       b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X" or
       b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X" or
       b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X" or
       b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X" or
       b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X" or
       b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X" or
       b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X"):
        
        tkinter.messagebox.showinfo("TIC-TAC-TOE",p1.get()+"Wins!...")

    elif(b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O" or
       b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O" or
       b7["text"]=="O" and b8["text"]=="O" and b9["text"]=="O" or
       b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O" or
       b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O" or
       b3["text"]=="O" and b6["text"]=="O" and b9["text"]=="O" or
       b1["text"]=="O" and b5["text"]=="O" and b9["text"]=="O" or
       b3["text"]=="O" and b5["text"]=="O" and b7["text"]=="O"):
        
        tkinter.messagebox.showinfo("TIC-TAC-TOE",p2.get()+"Wins!...")

    elif turns==8:
        tkinter.messagebox.showwarning("TIC-TAC-TOE","Match Draw")

def resetbutton(*buttons):
    buttons=[b1,b2,b3,b4,b5,b6,b7,b8,b9]
    for button in buttons:
        button["text"]=" "

    tkinter.messagebox.showinfo("TIC-TAC-TOE","Game Reseted!")
        
        
Label(Play, text="TIC-TAC-TOE",font=("calibri",30),fg="blue").place(x=250,y=10)

Label(Play, text="Player 1 Name: ",font=("calibri",20),bg="lightblue").place(x=110,y=70)
Label(Play, text="Player 2 Name: ",font=("calibri",20),bg="lightblue").place(x=110,y=110)

Entry(Play, textvariable=p1, font=("calibri",17)).place(x=300,y=70)
Entry(Play, textvariable=p2, font=("calibri",17)).place(x=300,y=120)

b1=Button(Play, text=" ",font=("calibri",20,"bold"),bg="blue",fg="white",width="8",height="2",command=lambda:btnclick(b1))
b1.place(x=120,y=200)

b2=Button(Play, text=" ",font=("calibri",20,"bold"),bg="blue",fg="white",width="8",height="2",command=lambda:btnclick(b2))
b2.place(x=252,y=200)

b3=Button(Play, text=" ",font=("calibri",20,"bold"),bg="blue",fg="white",width="8",height="2",command=lambda:btnclick(b3))
b3.place(x=384,y=200)

b4=Button(Play, text=" ",font=("calibri",20,"bold"),bg="blue",fg="white",width="8",height="2",command=lambda:btnclick(b4))
b4.place(x=120,y=300)

b5=Button(Play, text=" ",font=("calibri",20,"bold"),bg="blue",fg="white",width="8",height="2",command=lambda:btnclick(b5))
b5.place(x=252,y=300)

b6=Button(Play, text=" ",font=("calibri",20,"bold"),bg="blue",fg="white",width="8",height="2",command=lambda:btnclick(b6))
b6.place(x=384,y=300)

b7=Button(Play, text=" ",font=("calibri",20,"bold"),bg="blue",fg="white",width="8",height="2",command=lambda:btnclick(b7))
b7.place(x=120,y=400)

b8=Button(Play, text=" ",font=("calibri",20,"bold"),bg="blue",fg="white",width="8",height="2",command=lambda:btnclick(b8))
b8.place(x=252,y=400)

b9=Button(Play, text=" ",font=("calibri",20,"bold"),bg="blue",fg="white",width="8",height="2",command=lambda:btnclick(b9))
b9.place(x=384,y=400)

Button(Play,text="Reset",font=("calibri",10),bg="gray",fg="black",width="10",height="1",command=resetbutton).place(x=550,y=150)

Play.mainloop()

