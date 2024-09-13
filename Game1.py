#Rock-paper-scissor
from tkinter import *
import random

Play = Tk()
Play.geometry("750x650")
Play.title("Rock-Paper-Scissor")
Play.configure(bg="lightblue")

choices={"0":"Rock","1":"Paper","2":"Scissor"}

user_score=0
computer_score=0

def player_rock():
    global user_score,computer_score
    selected=choices[str(random.randint(0,2))]
    if selected=="Rock":
        result="Tie!..."
    elif selected=="Paper":
        result="Computer wins!.."
        computer_score+=1
    else:
        result="Player Wins!.."
        user_score+=1
    
    l1.config(text="Rock")
    l2.config(text=selected)
    l3.config(text=result)

    user_score_label.config(text=f"Player Score:{user_score}")
    computer_score_label.config(text=f"Computer Score:{computer_score}")
    btndisable()

def player_paper():
    global user_score,computer_score
    selected=choices[str(random.randint(0,2))]
    if selected=="Rock":
        result="Player Wins!.."
        user_score+=1
    elif selected=="Paper":
        result="Tie!..."
    else:
        result="Computer Wins!.."
        computer_score+=1
    
    l1.config(text="Paper")
    l2.config(text=selected)
    l3.config(text=result)

    user_score_label.config(text=f"Player Score:{user_score}")
    computer_score_label.config(text=f"Computer Score:{computer_score}")
    btndisable()

def player_scissor():
    global user_score,computer_score
    selected=choices[str(random.randint(0,2))]
    if selected=="Rock":
        result="Computer Wins!.."
        computer_score+=1
    elif selected=="Paper":
        result="Player Wins!.."
        user_score+=1
    else:
        result="Tie!.."
    
    l1.config(text="Scissor")
    l2.config(text=selected)
    l3.config(text=result)

    user_score_label.config(text=f"Player Score:{user_score}")
    computer_score_label.config(text=f"Computer Score:{computer_score}")
    btndisable()

def btndisable():
    b1["state"]="disable"
    b2["state"]="disable"
    b3["state"]="disable"

def reset():
    b1["state"]="active"
    b2["state"]="active"
    b3["state"]="active"
    l1.config(text="")
    l2.config(text="")
    l3.config(text="")


Label(Play,text="Rock-Paper-Scissor",font=("calibri",30),fg="blue").place(x=250,y=10)

Label(Play,text="Choose Anyone!...",font=("calibri",30),bg="lightblue",fg="blue").place(x=250,y=100)

b1=Button(Play,text="Rock",font=("calibri",20,"bold"),bg="orange",fg="white",width="12",height="1",command=player_rock)
b1.place(x=100,y=170)

b2=Button(Play,text="Paper",font=("calibri",20,"bold"),bg="orange",fg="white",width="12",height="1",command=player_paper)
b2.place(x=300,y=170)

b3=Button(Play,text="Scissor",font=("calibri",20,"bold"),bg="orange",fg="white",width="12",height="1",command=player_scissor)
b3.place(x=500,y=170)


Label(Play,text="Player Selected: ",font=("calibri",20),bg="lightblue").place(x=100,y=250)

Label(Play,text="Computer Selected: ",font=("calibri",20),bg="lightblue").place(x=450,y=250)

user_score_label=Label(Play,text="Player Score   : ",font=("calibri",20),bg="lightblue")
user_score_label.place(x=50,y=450)
computer_score_label=Label(Play,text="Computer Score : ",font=("calibri",20),bg="lightblue")
computer_score_label.place(x=50,y=500)

l1=Label(Play,font=("calibri",20,"bold"),bg="lightblue",fg="blue")
l1.place(x=200,y=300)

l2=Label(Play,font=("calibri",20,"bold"),bg="lightblue",fg="blue")
l2.place(x=550,y=300)

l3=Label(Play,font=("calibri",20,"bold"),bg="lightblue",relief="solid")
l3.place(x=300,y=350)

b4=Button(Play, text="Reset", font=("calibri",20,"bold"),bg="blue",fg="white",width="10",height="1",command=reset)
b4.place(x=500,y=450)

Play.mainloop()

