#Authentication
import tkinter.messagebox
from tkinter import *
import mysql.connector

db=mysql.connector.connect(host="localhost",user="root",password="arunkumar14",database="authentication")
cursor=db.cursor()

def admin():
    global admin_frame,admin_username,admin_password
    admin_frame=Frame(homepage, width=350, height=200)
    admin_frame.place(x=50,y=140)

    Label(admin_frame, text="Username", font=("calibri",15)).place(x=30,y=30)
    Label(admin_frame, text="Password", font=("calibri",15)).place(x=30,y=80)
    admin_username=StringVar()
    admin_password=StringVar()

    Entry(admin_frame, textvariable=admin_username, font=("calibri",13),bg="lightblue").place(x=145,y=30)
    Entry(admin_frame, textvariable=admin_password, font=("calibri",13),bg="lightblue").place(x=145,y=80)

    Button(admin_frame, text="login", font=("calibri",13),bg="brown",fg="white",width="10",height="1").place(x=220,y=140)


def user():
    global user_frame,user_username,user_password
    user_frame=Frame(homepage, width=350, height=200)
    user_frame.place(x=450,y=140)

    Label(user_frame, text="Username", font=("calibri",15)).place(x=30,y=30)
    Label(user_frame, text="Password", font=("calibri",15)).place(x=30,y=80)
    user_username=StringVar()
    user_password=StringVar()

    Entry(user_frame, textvariable=user_username, font=("calibri",13),bg="lightblue").place(x=145,y=30)
    Entry(user_frame, textvariable=user_password, font=("calibri",13),bg="lightblue").place(x=145,y=80)

    Button(user_frame, text="Signup", font=("calibri",13),bg="brown",fg="white",width="10",height="1",command=register).place(x=30,y=140)
    Button(user_frame, text="login", font=("calibri",13),bg="brown",fg="white",width="10",height="1",command=user_login).place(x=220,y=140)

def register():
    global register_frame, register_username, register_password
    global register_name, register_mail, register_gender,register_address

    register_frame=Frame(homepage, width=350, height=450)
    register_frame.place(x=850,y=140)

    Label(register_frame, text="Name", font=("calibri",15)).place(x=30,y=30)
    Label(register_frame, text="Mail", font=("calibri",15)).place(x=30,y=80)
    Label(register_frame, text="Gender", font=("calibri",15)).place(x=30,y=130)
    Label(register_frame, text="Address", font=("calibri",15)).place(x=30,y=180)
    Label(register_frame, text="Username", font=("calibri",15)).place(x=30,y=230)
    Label(register_frame, text="Password", font=("calibri",15)).place(x=30,y=280)

    register_name=StringVar()
    register_mail=StringVar()
    register_gender=StringVar()
    register_address=StringVar()
    register_username=StringVar()
    register_password=StringVar()

    Entry(register_frame, textvariable=register_name, font=("calibri",13),bg="lightblue").place(x=145,y=30)
    Entry(register_frame, textvariable=register_mail, font=("calibri",13),bg="lightblue").place(x=145,y=80)
    Radiobutton(register_frame, text="Male",variable=register_gender,value="Male",font=("calibri",13)).place(x=145,y=130)
    Radiobutton(register_frame, text="Female",variable=register_gender,value="Female",font=("calibri",13)).place(x=225,y=130)
    Entry(register_frame, textvariable=register_address, font=("calibri",13),bg="lightblue").place(x=145,y=180)
    Entry(register_frame, textvariable=register_username, font=("calibri",13),bg="lightblue").place(x=145,y=230)
    Entry(register_frame, textvariable=register_password, font=("calibri",13),bg="lightblue").place(x=145,y=280)
    
    Button(register_frame,text="Submit",font=("calibri",12),bg="brown",fg="white",width="18",height="1",command=store_data).place(x=150,y=330)

def user_login():
    username=user_username.get()
    password=user_password.get()
    cursor.execute("select * from logindetails where Username=%s and Password=%s",[username,password])
    data=cursor.fetchone()
    if data!= None:
        tkinter.messagebox.showinfo("Authenticate","Welcome User")
    else:
        tkinter.messagebox.showwarning("Authenticate","Invalid User") 

def store_data():
    name=register_name.get()
    mail=register_mail.get()
    gender=register_gender.get()
    address=register_address.get()
    username=register_username.get()
    password=register_password.get()

    cursor.execute("insert into logindetails(Name,Email,Gender,Address,Username,Password)values(%s,%s,%s,%s,%s,%s)",[name,mail,gender,address,username,password])
    db.commit()
    tkinter.messagebox.showinfo("Authenticate","Registered Successfully")

def startpage():
    global homepage
    homepage=Tk()
    homepage.geometry("1300x600")
    homepage.title("Authentication")
    homepage.configure(bg="lightblue")

    Label(homepage, text="Welcome to login page",font=("calibri",30),fg="blue").place(x=430,y=10)

    Button(homepage, text="Admin", font=("calibri",20),bg="brown",fg="white",width="12",height="1",command=admin).place(x=70,y=70)
    Button(homepage, text="User", font=("calibri",20),bg="brown",fg="white",width="12",height="1",command=user).place(x=1000,y=70)
    homepage.mainloop()
startpage()




    