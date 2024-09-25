#Authentication and Authorisation
import tkinter.messagebox
from tkinter import *
import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="arunkumar14", database="authentication")
cursor = db.cursor()

def admin():
    global admin_frame, admin_username, admin_password
    admin_frame = Frame(homepage, width=350, height=200)
    admin_frame.place(x=50, y=140)

    Label(admin_frame, text="Username", font=("calibri", 15)).place(x=30, y=30)
    Label(admin_frame, text="Password", font=("calibri", 15)).place(x=30, y=80)
    admin_username = StringVar()
    admin_password = StringVar()

    Entry(admin_frame, textvariable=admin_username, font=("calibri", 13), bg="lightblue").place(x=145, y=30)
    Entry(admin_frame, textvariable=admin_password, font=("calibri", 13), bg="lightblue", show="*").place(x=145, y=80)

    Button(admin_frame, text="Login", font=("calibri", 13), bg="brown", fg="white", width="10", height="1", command=adminlogin).place(x=220, y=140)

def adminlogin():
    username = admin_username.get()
    password = admin_password.get()

    if username == "Brit" and password == "Brit12":
        tkinter.messagebox.showinfo("Authenticate", "Welcome Admin")
        adminhome()
    else:
        tkinter.messagebox.showerror("Authenticate", "Invalid credentials")

def adminhome():
    global adminpage
    adminpage = Toplevel(homepage)
    adminpage.geometry("1300x500")
    adminpage.title("Admin home")
    adminpage.configure(bg="lightblue")

    Button(adminpage, text="Pending list", font=("calibri", 15), bg="brown", fg="white", width="12", height="1", command=pending).grid(row=0, column=0)
    Button(adminpage, text="Approved list", font=("calibri", 15), bg="brown", fg="white", width="12", height="1", command=approved).grid(row=0, column=1)

def pending():
    cursor.execute("SELECT * FROM logindetails WHERE Status=False")
    data = cursor.fetchall()

    if len(data) == 0:
        tkinter.messagebox.showinfo("No Pending Users", "There are no pending users.")
        return

    rows = len(data)
    cols = len(data[0])

    Label(adminpage, text="Id", font=("calibri", 13, "bold"), bg="lightblue").grid(row=1, column=0)
    Label(adminpage, text="Name", font=("calibri", 13, "bold"), bg="lightblue").grid(row=1, column=1)
    Label(adminpage, text="Mail", font=("calibri", 13, "bold"), bg="lightblue").grid(row=1, column=2)
    Label(adminpage, text="Gender", font=("calibri", 13, "bold"), bg="lightblue").grid(row=1, column=3)
    Label(adminpage, text="Address", font=("calibri", 13, "bold"), bg="lightblue").grid(row=1, column=4)
    Label(adminpage, text="Username", font=("calibri", 13, "bold"), bg="lightblue").grid(row=1, column=5)
    Label(adminpage, text="Password", font=("calibri", 13, "bold"), bg="lightblue").grid(row=1, column=6)
    Label(adminpage, text="Status", font=("calibri", 13, "bold"), bg="lightblue").grid(row=1, column=7)
    Label(adminpage, text="Action", font=("calibri", 13, "bold"), bg="lightblue").grid(row=1, column=8)

    for i in range(rows):
        for j in range(cols):
            S = Entry(adminpage, font=("calibri", 11))
            S.grid(row=i+2, column=j)
            S.insert(END, data[i][j])

        # Approve button with the current user id
        b1 = Button(adminpage, text="Approve", font=("calibri", 10), bg="brown", fg="white", width="8", height="1",command=lambda i=i: approve(data[i][0]))
        b1.grid(row=i+2, column=cols)

        # Delete button with the current user id
        b2 = Button(adminpage, text="Delete", font=("calibri", 10), bg="brown", fg="white", width="8", height="1",command=lambda i=i: delete(data[i][0]))
        b2.grid(row=i+2, column=cols+1)

def approve(id):
    cursor.execute("UPDATE logindetails SET Status=True WHERE Id=%s", [id])
    db.commit()
    tkinter.messagebox.showinfo("Authorize", "Status Updated")
    pending()

def delete(id):
    cursor.execute("DELETE FROM logindetails WHERE Id=%s", [id])
    db.commit()
    tkinter.messagebox.showinfo("Authorize", "User Deleted")
    pending()

def approved():
    cursor.execute("SELECT * FROM logindetails WHERE Status=True")
    data = cursor.fetchall()

    if len(data) == 0:
        tkinter.messagebox.showinfo("No Approved Users", "There are no approved users.")
        return

    rows = len(data)
    cols = len(data[0])

    Label(adminpage, text="Id", font=("calibri", 13, "bold"), bg="lightblue").grid(row=1, column=0)
    Label(adminpage, text="Name", font=("calibri", 13, "bold"), bg="lightblue").grid(row=1, column=1)
    Label(adminpage, text="Mail", font=("calibri", 13, "bold"), bg="lightblue").grid(row=1, column=2)
    Label(adminpage, text="Gender", font=("calibri", 13, "bold"), bg="lightblue").grid(row=1, column=3)
    Label(adminpage, text="Address", font=("calibri", 13, "bold"), bg="lightblue").grid(row=1, column=4)
    Label(adminpage, text="Username", font=("calibri", 13, "bold"), bg="lightblue").grid(row=1, column=5)
    Label(adminpage, text="Password", font=("calibri", 13, "bold"), bg="lightblue").grid(row=1, column=6)
    Label(adminpage, text="Status", font=("calibri", 13, "bold"), bg="lightblue").grid(row=1, column=7)

    for i in range(rows):
        for j in range(cols):
            S = Entry(adminpage, font=("calibri", 11))
            S.grid(row=i+2, column=j)
            S.insert(END, data[i][j])

def user():
    global user_frame, user_username, user_password
    user_frame = Frame(homepage, width=350, height=200)
    user_frame.place(x=450, y=140)

    Label(user_frame, text="Username", font=("calibri", 15)).place(x=30, y=30)
    Label(user_frame, text="Password", font=("calibri", 15)).place(x=30, y=80)
    user_username = StringVar()
    user_password = StringVar()

    Entry(user_frame, textvariable=user_username, font=("calibri", 13), bg="lightblue").place(x=145, y=30)
    Entry(user_frame, textvariable=user_password, font=("calibri", 13), bg="lightblue", show="*").place(x=145, y=80)

    Button(user_frame, text="Signup", font=("calibri", 13), bg="brown", fg="white", width="10", height="1", command=register).place(x=30, y=140)
    Button(user_frame, text="Login", font=("calibri", 13), bg="brown", fg="white", width="10", height="1", command=user_login).place(x=220, y=140)

def user_login():
    username = user_username.get()
    password = user_password.get()
    cursor.execute("SELECT * FROM logindetails WHERE Username=%s AND Password=%s", [username, password])
    data = cursor.fetchone()

    if data is not None:
        Status = data[7]
        if Status == True:
            tkinter.messagebox.showinfo("Authenticate", "Welcome User")
        else:
            tkinter.messagebox.showerror("Authenticate", "Your account is not yet activated")
    else:
        tkinter.messagebox.showwarning("Authenticate", "Invalid User")

def register():
    global register_frame, register_username, register_password
    global register_name, register_mail, register_gender, register_address

    register_frame = Frame(homepage, width=350, height=450)
    register_frame.place(x=850, y=140)

    Label(register_frame, text="Name", font=("calibri", 15)).place(x=30, y=30)
    Label(register_frame, text="Mail", font=("calibri", 15)).place(x=30, y=80)
    Label(register_frame, text="Gender", font=("calibri", 15)).place(x=30, y=130)
    Label(register_frame, text="Address", font=("calibri", 15)).place(x=30, y=180)
    Label(register_frame, text="Username", font=("calibri", 15)).place(x=30, y=230)
    Label(register_frame, text="Password", font=("calibri", 15)).place(x=30, y=280)

    register_name = StringVar()
    register_mail = StringVar()
    register_gender = StringVar()
    register_address = StringVar()
    register_username = StringVar()
    register_password = StringVar()

    Entry(register_frame, textvariable=register_name, font=("calibri", 13), bg="lightblue").place(x=145, y=30)
    Entry(register_frame, textvariable=register_mail, font=("calibri", 13), bg="lightblue").place(x=145, y=80)
    Radiobutton(register_frame, text="Male",variable=register_gender,value="Male",font=("calibri",13)).place(x=145,y=130)
    Radiobutton(register_frame, text="Female",variable=register_gender,value="Female",font=("calibri",13)).place(x=225,y=130)
    Entry(register_frame, textvariable=register_address, font=("calibri", 13), bg="lightblue").place(x=145, y=180)
    Entry(register_frame, textvariable=register_username, font=("calibri", 13), bg="lightblue").place(x=145, y=230)
    Entry(register_frame, textvariable=register_password, font=("calibri", 13), bg="lightblue", show="*").place(x=145, y=280)

    Button(register_frame, text="Submit", font=("calibri", 13), bg="brown", fg="white", width="10", height="1", command=register_submit).place(x=110, y=350)

def register_submit():
    name = register_name.get()
    mail = register_mail.get()
    gender = register_gender.get()
    address = register_address.get()
    username = register_username.get()
    password = register_password.get()

    if name == "" or mail == "" or gender == "" or address == "" or username == "" or password == "":
        tkinter.messagebox.showwarning("Register", "Please fill all the fields")
    else:
        cursor.execute("SELECT * FROM logindetails WHERE Username=%s", [username])
        data = cursor.fetchone()

        if data is not None:
            tkinter.messagebox.showwarning("Register", "Username already exists")
        else:
            cursor.execute("INSERT INTO logindetails(Name, Email, Gender, Address, Username, Password, Status) VALUES (%s, %s, %s, %s, %s, %s, %s)", (name, mail, gender, address, username, password, 0))
            db.commit()
            tkinter.messagebox.showinfo("Register", "Registration Successful")

homepage = Tk()
homepage.geometry("1300x650")
homepage.title("Login Page")
homepage.configure(bg="lightblue")

Label(homepage,text="Welcome to login page!",font=("calibri",20),bg="lightblue",fg="black").place(x=500,y=20)

Button(homepage, text="Admin", font=("calibri", 15), bg="brown", fg="white", width="15", height="1", command=admin).place(x=50, y=80)
Button(homepage, text="User", font=("calibri", 15), bg="brown", fg="white", width="15", height="1", command=user).place(x=450, y=80)

homepage.mainloop()





    