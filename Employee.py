import tkinter.messagebox
from tkinter import *
import mysql.connector

db=mysql.connector.connect(host="localhost",user="root",password="arunkumar14",db="brit")
cursor=db.cursor()

access=Tk()
access.geometry("700x800")
access.title("Employee's Details")
access.configure(bg="lightgray")

def calculate():
    Emp_ctc.set(Emp_salary.get() * 12)

def add():
    id=Emp_id.get()
    name=Emp_name.get()
    age=Emp_age.get()
    email=Emp_email.get()
    phone=Emp_phone.get()
    salary=Emp_salary.get()
    experience=Emp_exp.get()
    CTC=Emp_ctc.get()

    cursor.execute("insert into Employee values(%s,%s,%s,%s,%s,%s,%s,%s)",[id,name,age,email,phone,salary,experience,CTC])
    db.commit()
    tkinter.messagebox.showinfo("Employee's Details","Datas are Added")

def view():
    id=Emp_id.get()
    cursor.execute("select * from Employee where Emp_id=%s",[id])
    data=cursor.fetchone()

    if data != None:
        Emp_name.set(data[1])
        Emp_age.set(data[2])
        Emp_email.set(data[3])
        Emp_phone.set(data[4])
        Emp_salary.set(data[5])
        Emp_exp.set(data[6])
        Emp_ctc.set(data[7])

    else:
        tkinter.messagebox.showerror("Employee's Details","No Data")

def clear():
    Emp_name.set("")
    Emp_age.set("")
    Emp_email.set("")
    Emp_phone.set("")
    Emp_salary.set("")
    Emp_exp.set("")
    Emp_ctc.set("")


def update():
    id=Emp_id.get()
    name=Emp_name.get()
    age=Emp_age.get()
    email=Emp_email.get()
    phone=Emp_phone.get()
    salary=Emp_salary.get()
    experience=Emp_exp.get()
    CTC=Emp_ctc.get()

    cursor.execute("update Employee set Emp_name=%s,Emp_age=%s,Emp_email=%s,Emp_phone=%s,Emp_salary=%s,Emp_exp=%s,Emp_ctc=%s where Emp_id=%s",[name,age,email,phone,salary,experience,CTC,id])
    db.commit()
    tkinter.messagebox.showinfo("Employee's Details","Datas are updated")

def delete():
    id=Emp_id.get()
    cursor.execute("delete from Employee where Emp_id=%s",[id])
    db.commit()
    tkinter.messagebox.showinfo("Employee's Details","Data Deleted")

def overall():
    global viewpage
    viewpage=Toplevel(access)
    viewpage.geometry("1200x500")
    viewpage.title("Employee's Details")
    viewpage.configure(bg="lightblue")
    cursor.execute("select * from Employee")
    data=cursor.fetchall()
    rows=len(data)
    cols=len(data[0])

    Label(viewpage, text="Emp_id",font=("calibri",15,"bold"),bg="lightblue").grid(row=0,column=0)
    Label(viewpage, text="Emp_name",font=("calibri",15,"bold"),bg="lightblue").grid(row=0,column=1)
    Label(viewpage, text="Emp_age",font=("calibri",15,"bold"),bg="lightblue").grid(row=0,column=2)
    Label(viewpage, text="Emp_email",font=("calibri",15,"bold"),bg="lightblue").grid(row=0,column=3)
    Label(viewpage, text="Emp_phone",font=("calibri",15,"bold"),bg="lightblue").grid(row=0,column=4)
    Label(viewpage, text="Emp_salary",font=("calibri",15,"bold"),bg="lightblue").grid(row=0,column=5)
    Label(viewpage, text="Emp_exp",font=("calibri",15,"bold"),bg="lightblue").grid(row=0,column=6)
    Label(viewpage, text="Emp_ctc",font=("calibri",15,"bold"),bg="lightblue").grid(row=0,column=7)

    for i in range(rows):
        for j in range(cols):
            S=Entry(viewpage,font=("calibri",10))
            S.grid(row=i+1,column=j)
            S.insert(END,data[i][j])


Label(access,text="Employee's Data",font=("calibri",30)).place(x=230,y=10)

Label(access,text="Employee Id",font=("calibri",20),bg="lightblue").place(x=100,y=80)
Emp_id=StringVar()
Entry(access,textvariable=Emp_id,font=("calibri",17)).place(x=300,y=80)

Label(access,text="Employee Name",font=("calibri",20),bg="lightblue").place(x=100,y=130)
Emp_name=StringVar()
Entry(access,textvariable=Emp_name,font=("calibri",17)).place(x=300,y=130)

Label(access,text="Employee Age",font=("calibri",20),bg="lightblue").place(x=100,y=180)
Emp_age=IntVar()
Entry(access,textvariable=Emp_age,font=("calibri",17)).place(x=300,y=180)

Label(access,text="Employee E-Mail",font=("calibri",20),bg="lightblue").place(x=100,y=230)
Emp_email=StringVar()
Entry(access,textvariable=Emp_email,font=("calibri",17)).place(x=300,y=230)

Label(access,text="Employee phone",font=("calibri",20),bg="lightblue").place(x=100,y=280)
Emp_phone=IntVar()
Entry(access,textvariable=Emp_phone,font=("calibri",17)).place(x=300,y=280)

Label(access,text="Employee Salary",font=("calibri",20),bg="lightblue").place(x=100,y=330)
Emp_salary=IntVar()
Entry(access,textvariable=Emp_salary,font=("calibri",17)).place(x=300,y=330)

Label(access,text="Employee Exp",font=("calibri",20),bg="lightblue").place(x=100,y=380)
Emp_exp=IntVar()
Entry(access,textvariable=Emp_exp,font=("calibri",17)).place(x=300,y=380)

Label(access,text="Employee CTC",font=("calibri",20),bg="lightblue").place(x=100,y=430)
Emp_ctc=IntVar()
Entry(access,textvariable=Emp_ctc,font=("calibri",17)).place(x=300,y=430)

but_cal=Button(access,text="calculate",font=("calibri",10),bg="blue",fg="black",width="8",height="1",command=calculate)
but_cal.place(x=560,y=230)

but_add=Button(access,text="Add",font=("calibri",18),bg="blue",fg="black",width="8",height="1",command=add)
but_add.place(x=100,y=500)

but_view=Button(access,text="View",font=("calibri",18),bg="blue",fg="black",width="8",height="1",command=view)
but_view.place(x=260,y=500)

but_clr=Button(access,text="Clear",font=("calibri",18),bg="blue",fg="black",width="8",height="1",command=clear)
but_clr.place(x=420,y=500)

but_upd=Button(access,text="Update",font=("calibri",18),bg="blue",fg="black",width="8",height="1",command=update)
but_upd.place(x=100,y=580)

but_del=Button(access,text="Delete",font=("calibri",18),bg="blue",fg="black",width="8",height="1",command=delete)
but_del.place(x=260,y=580)

but_ovr=Button(access,text="Overall",font=("calibri",15),bg="blue",fg="black",width="8",height="1",command=overall)
but_ovr.place(x=420,y=580)


access.mainloop()
