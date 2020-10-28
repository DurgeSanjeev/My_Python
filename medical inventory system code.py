from tkinter import *
import mysql.connector
import tkinter.messagebox as MessageBox
login=0

#function for validating login info via values in database

def validate():
        global login
        login=0
    #connecting to database
        conn=mysql.connector.connect(
             host="localhost",
             user="root",
             passwd="8809769655aks",
             
            )
#getting cursor ready for query execution
        mycursor=conn.cursor()
        mycursor.execute("Use akshay")
        
        query="Select * from users"
        mycursor.execute(query)   #executing query
        uname1=t_uname.get()
        password1=t_pwd.get()
        print("entered : ",uname1,password1)
        login=0
        for i in mycursor:
            if(i[0]==uname1 and i[1]==password1):  #compairing with every value in database
                login=1
            print(i[0],i[1])
            
    
    #checking login status as per query result and value matching
    
        if login:
            MessageBox.showinfo(uname1,"logged successfully")
            root.destroy()

        else:
            Messagebox.showinfo(uname,"wrong credentials")

    
#from PIL import ImageTk

# Login window

root = Tk()
root.geometry('600x300')

root.configure(bg='#003e53')
title=Label(root,text="Login Form",fg="white",bg='#003e53',font=("bold",15))
title.place(x=200,y=30)
uname=Label(root,text="User Name",fg="white",bg='#003e53',font=("bold",10))
uname.place(x=100,y=80)
password=Label(root,text="password",fg="white",bg='#003e53',font=("bold",10))
password.place(x=100,y=110)
t_uname=Entry()
t_uname.place(x=200,y=80)
t_pwd=Entry()
t_pwd.place(x=200,y=115)
submit=Button(root,text="Submit",command=validate)
submit.place(x=200,y=150)
root.mainloop()


#second window for medical invenory system
import sys

# function for searching supplier

def suppsearch(win,str1):

    if(str1=="Kushal"):
        str2="Supplier found!\n Name : Kushal Bhardwaj \n Place : Mahendergarh \n Mob : 999999999"
    else:
        str2="No Supplier Found!"
    win.result=Label(win,text="",fg="red",font="Arial 15 bold")
    win.result.configure(text="")
    win.result.configure(text=str2)
    win.result.grid(row=6)

#Medicine Menu

def mclickedbtn1(window1,flag):
    _list = window1.winfo_children()

    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())
    widget_list = _list
    for item in widget_list:
        item.pack_forget()
        item.grid_forget()
    if(flag==3):            # call from supplier menu
        suppName=Label(window1,text="Enter Supplier Name ")
        supplier=Entry(window1,font="Arial 18 bold")
        
        btn=Button(window1,text="Search",bg="#005e13",fg="white",command=lambda:suppsearch(window1,supplier.get()))
        
        
    else:                  # call from medicine menu
        suppName=Label(window1,text="Enter Medicine Name : ")
        supplier=Entry(window1,font="Arial 18 bold")
        result=Label(window1,text="New Medicine Added !",fg="green",font="Arial 18 bold")
        btn=Button(window1,text="Add",bg="#005e13",fg="white",command=lambda:result.grid(row=6)) 
        
    suppName.grid(row=1)
    supplier.grid(row=2)
    btn.grid(row=4)
    print("list 1 ",_list)
    print("list 2 ",widget_list)
    print("Hello1")
    
    
#function for searching medicine

def searchmed(win,str1):
    if(str1=="Paracetamol"):
        str2="Medicine found!\n Name : Paracetamol \n Price : Rs.10"
    else:
        str2="No Medicine Found!"
        
    win.result=Label(win,text="",fg="red",font="Arial 15 bold")
    win.result.configure(text="")
    win.result.configure(text=str2)
    win.result.grid(row=6)
    
    
    
 # function for controlling medicine search and adding new suplier     
def mclickedbtn2(window1,flag):
    _list = window1.winfo_children()

    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())
    widget_list = _list
    for item in widget_list:
        item.pack_forget()
        item.grid_forget()
        
    if(flag==3):                             #call from Supplier window
        suppName=Label(window1,text="Enter Supplier Name : ")
        supplier=Entry(window1,font="Arial 18 bold")
        result=Label(window1,text="New Supplier Added !",fg="green",font="Arial 18 bold")
        btn=Button(window1,text="Add",bg="#005e13",fg="white",command=lambda: result.grid(row=6)) 
        suppName.grid(row=1)
        supplier.grid(row=2)
        btn.grid(row=4)
        
        
    else:                                      #call from medicine window
        suppName=Label(window1,text="Enter Medicine Name : ")
        supplier=Entry(window1,font="Arial 18 bold")
        btn=Button(window1,text="Search",bg="#005e13",fg="white",command=lambda: searchmed(window1,supplier.get()))
                   
        suppName.grid(row=1)
        supplier.grid(row=2)
        btn.grid(row=4)
    print("list 1 ",_list)
    print("list 2 ",widget_list)
    print("tap on options")
    print("tap on options")
    
  #function for searching customer  
    
def searchcust(win,str1):
    if(str1=="Akshay"):
        str2="Customer found!\n Name : Akshay Kumar \n Mob : 9990999990"
    else:
        str2="No Customer Found!"
        
    win.result=Label(win,text="",fg="red",font="Arial 15 bold")
    win.result.configure(text="")
    win.result.configure(text=str2)
    win.result.grid(row=6)
    
#function for controlling customer window options     
def mclickedbtn3(window1,flag):
    _list = window1.winfo_children()

    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())
    widget_list = _list
    for item in widget_list:
        item.pack_forget()
        item.grid_forget()
    
    if(flag==2):                         #adding new customer 
        print("flag : ",flag)
        suppName=Label(window1,text="Enter Customer Name : ")
        supplier=Entry(window1,font="Arial 18 bold")
        result=Label(window1,text="New Customer Added !",fg="green",font="Arial 18 bold")
        btn=Button(window1,text="Add",bg="#005e13",fg="white",command=lambda: result.grid(row=6)) 
        suppName.grid(row=1)
        supplier.grid(row=2)
        btn.grid(row=4)
    else:                               #searching new customer
        print("flag : ",flag)
        suppName=Label(window1,text="Enter Customer Name : ")
        supplier=Entry(window1,font="Arial 18 bold")
        btn=Button(window1,text="Search",bg="#005e13",fg="white",command=lambda: searchcust(window1,supplier.get()))
        suppName.grid(row=1)
        supplier.grid(row=2)
        btn.grid(row=4)
        

        
#out od stock meds function        
def mclickedbtn4(window1):
    print("tap on options")
    _list = window1.winfo_children()

    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())
    widget_list = _list
    for item in widget_list:
        item.pack_forget()
        item.grid_forget()
    
    suppName=Label(window1,text=" Following meds out of stock : ")
    supplier1=Label(window1,font="Arial 18 bold",fg="red",text="Paracetamol")
    supplier2=Label(window1,font="Arial 18 bold",fg="red",text="Benedryl DR")
    btn=Button(window1,text="Ok",bg="#005e13",padx=20,fg="white",command=lambda:window1.destroy())
    supplier1.grid(row=2)
    supplier2.grid(row=3)
    suppName.grid(row=0)
    btn.grid(row=6)

# Function for returning to main menu option    
def mclickedbtn5(window):
    window.destroy()
    print("closing button")
    
#Medicine Menu 

def clickedbtn1():
    medicine_menu_window = Tk()
    medicine_menu_window.geometry('600x400')
    medicine_menu_window.title("Medical Inventory System")
    lbl = Label(medicine_menu_window, text="Medicine Menu!")
    lbl.grid(column=0, row=0)
    lbl2 = Label(medicine_menu_window, text="What would you like to do!")
    lbl2.grid(column=0, row=1)
    btn1 = Button(medicine_menu_window, text="Add New Medicine",fg="red", command=lambda: mclickedbtn1(medicine_menu_window,1))
    btn1.grid(column=0, row=2)
    btn2 = Button(medicine_menu_window, text="Search Medicine",fg="red", command=lambda:mclickedbtn2(medicine_menu_window,1))
    btn2.grid(column=0, row=3)
    btn4 = Button(medicine_menu_window, text="Out of Stock Meds",fg="red", command=lambda: mclickedbtn4(medicine_menu_window))
    btn4.grid(column=0, row=4)
    btn4 = Button(medicine_menu_window, text="Return to main menu",fg="red", command=lambda: mclickedbtn5(medicine_menu_window))
    btn4.grid(column=0, row=5)
    medicine_menu_window.mainloop()
    
#Customer Menu

def clickedbtn2():
    c_menu_window = Tk()
    c_menu_window.geometry('600x400')
    c_menu_window.title("Medical Inventory System")
    lbl = Label(c_menu_window, text="Customer Menu!")
    lbl.grid(column=0, row=0)
    lbl2 = Label(c_menu_window, text="What would you like to do!")
    lbl2.grid(column=0, row=1)
    btn1 = Button(c_menu_window, text="Search Customer",fg="red", command=lambda: mclickedbtn3(c_menu_window,1))
    btn1.grid(column=0, row=2)
    btn2 = Button(c_menu_window, text="New Customer",fg="red", command=lambda: mclickedbtn3(c_menu_window,2))
    btn2.grid(column=0, row=3)
    btn4 = Button(c_menu_window, text="Return to main menu",fg="red", command=lambda:mclickedbtn5(c_menu_window))
    btn4.grid(column=0, row=5)
    c_menu_window.mainloop()

#Supplier Menu

def clickedbtn3():
    s_menu_window = Tk()
    s_menu_window.geometry('600x400')
    s_menu_window.title("Medical Inventory Sytem")
    lbl = Label(s_menu_window, text="Supplier Menu!")
    lbl.grid(column=0, row=0)
    lbl2 = Label(s_menu_window, text="What would you like to do!")
    lbl2.grid(column=0, row=1)
    btn1 = Button(s_menu_window, text="Search Supplier",fg="red", command=lambda : mclickedbtn1(s_menu_window,3))
    btn1.grid(column=0, row=2)
    btn2 = Button(s_menu_window, text="New Supplier",fg="red", command=lambda:mclickedbtn2(s_menu_window,3))
    btn2.grid(column=0, row=3)
    btn4 = Button(s_menu_window, text="Return to main menu",fg="red", command=lambda:mclickedbtn5(s_menu_window))
    btn4.grid(column=0, row=4)
    s_menu_window.mainloop()


#Main Menu

window = Tk()
window.geometry('600x400')
window.title("Medical Inventory System")
lbl = Label(window, text="Welcome to Medical Inventory Management System Software!")
lbl.grid(column=0, row=0)
lbl2 = Label(window, text="What would you like to do!")
lbl2.grid(column=0, row=1)
btn1 = Button(window, text="Medicine Menu",fg="red", command=clickedbtn1)
btn1.grid(column=0, row=2)
btn2 = Button(window, text="Customer Menu",fg="red", command=clickedbtn2)
btn2.grid(column=0, row=3)
btn3 = Button(window, text="Supplier Menu",fg="red", command=clickedbtn3)
btn3.grid(column=0, row=4)
window.mainloop()