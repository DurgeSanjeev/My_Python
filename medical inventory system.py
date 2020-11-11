from tkinter import *
import mysql.connector
import tkinter.messagebox as MessageBox   #to show messages
login=0
conn=mysql.connector.connect(
             host="localhost",
             user="root",
             passwd="8809769655aks",
             
            )
mycursor=conn.cursor()      #to execute the command of database
 
def validate():             #to checck the data credentials if it is right or wrong
        global login,mycursor   #to use the global variables 
        login=0
        
        mycursor.execute("Use akshay")           
        
        query="Select * from users"
        mycursor.execute(query)
        uname1=t_uname.get()
        password1=t_pwd.get()
       # print("entered : ",uname1,password1)
        login=0
        for i in mycursor:
            if(i[0]==uname1 and i[1]==password1):
                login=1                                 #for logged succesfully
          #  print(i[0],i[1])
            
    
        if login:
            MessageBox.showinfo(uname1,"logged successfully")
            root.destroy()

        else:
            Messagebox.showinfo(uname,"wrong credentials")

    
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

import sys
    
        
def mclickedbtn5(window):       #to destroy the passed window
    window.destroy()
    #print("closing button")
    
    
#=====Medicine Menu====


def show_medicines(window1,outofstock):
    global mycursor
    
    _list = window1.winfo_children()
    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())
    widget_list = _list
    for item in widget_list:
        item.pack_forget()
        item.grid_forget()
    srnoLabel=Label(window1,text="Sr No",bg="#232345",fg="white")
    srnoLabel.grid(row=0,column=0)    
    custLabel=Label(window1,text="Medicine Name",bg="#232345",fg="white")
    custLabel.grid(row=0,column=1)
    qtyLabel=Label(window1, text="Qty(pkts)",bg="#232345",fg="white")
    qtyLabel.grid(row=0,column=2)
    priceLabel=Label(window1, text="Price(Rs per pkt)",bg="#232345",fg="white")
    priceLabel.grid(row=0,column=3)
    if(outofstock):
        mycursor.execute("select * from medicine where qty=0")          #==Medicines out of stock==
    else:
        mycursor.execute("Select * from medicine");                     #==Medicines in stock====

    r=1
    info=[]
    i=0
    for k in mycursor:
            info.append(Label(window1, bd=4, text=r))
            info[i].grid(row=r, column=0, pady=1)
            i=i+1
            info.append(Label(window1, bd=4, text=k[0]))
            info[i].grid(row=r, column=1, pady=1)
            i=i+1
            info.append(Label(window1, bd=4, text=k[1]))
            info[i].grid(row=r, column=2, pady=1)
            i=i+1
            info.append(Label(window1, bd=4, text=k[2]))
            info[i].grid(row=r, column=3, pady=1)
            r+=1
            i=i+1
        #    print(k[0],k[1],k[2])
            
   # print("Inside show Medicines")
    


    
def addedMed(name,qty,price,result):
    global mycursor,conn
    #addbtnclicked=1
   # print("inside addedSupp",name,)
    if(name=="" or qty=="" or price=="" or int(price)<0 or int(qty)<0):
            result.configure(text="Wrong Info, Re-enter !",fg="red",font="Arial 18 bold")
            
    else:
            result.configure(text="New Medicine Added !",fg="green",font="Arial 18 bold")
            mycursor.execute("INSERT INTO medicine Values (%s , %s, %s)",(name,qty,price))
            conn.commit()

  #======Medicine menu window====  
    
def add_medicine(window1):
    global mycursor
    
    _list = window1.winfo_children()
    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())
    widget_list = _list
    for item in widget_list:
        item.pack_forget()
        item.grid_forget()
    
    medName=Label(window1,text="Enter Medicine Name : ")
    medicine=Entry(window1,font="Arial 18 bold")
    medQty=Label(window1,text="Enter Quantity (pkt) : ")
    qty=Entry(window1,font="Arial 18 bold")
    medPrice=Label(window1,text="Enter Price (Rs per pkt) : ")
    price=Entry(window1,font="Arial 18 bold")
    result=Label(window1,text=" Enter Info..!",fg="blue",font="Arial 18 bold")
    result.grid(row=8)
    btn=Button(window1,text="Add",bg="#005e13",fg="white",command=lambda: addedMed(medicine.get(),qty.get(),price.get(),result)) #lambda is a inbuilt single line function
    medName.grid(row=1)
    medicine.grid(row=2)
    medQty.grid(row=3)
    qty.grid(row=4)
    medPrice.grid(row=5)
    price.grid(row=6)
    btn.grid(row=7)


def clickedbtn1():
    medicine_menu_window = Tk()
    medicine_menu_window.geometry('600x300')
    medicine_menu_window.configure(bg="#232345")
    medicine_menu_window.title("Medical Inventory System")
    lbl = Label(medicine_menu_window, text="Medicine Menu!")
    lbl.grid(row=0)
    lbl2 = Label(medicine_menu_window, text="What would you like to do!")
    lbl2.grid(row=2)
    btn1 = Button(medicine_menu_window, text="Add New Medicine",fg="red", command=lambda: add_medicine(medicine_menu_window))
    btn1.grid(row=4)
    btn2 = Button(medicine_menu_window, text="Show All Medicines",fg="red", command=lambda: show_medicines(medicine_menu_window,0))
    btn2.grid(row=6)
    btn3 = Button(medicine_menu_window, text="Out of Stock Meds",fg="red", command=lambda: show_medicines(medicine_menu_window,1))
    btn3.grid(row=8)
    btn3 = Button(medicine_menu_window, text="Return to main menu",fg="red", command=lambda: mclickedbtn5(medicine_menu_window))
    btn3.grid(row=10)
    medicine_menu_window.mainloop()
    
#=====Customer Menu window=======

#function for showing all customer deails
def show_customers(window1):
    global mycursor
    
    _list = window1.winfo_children()
    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())
    widget_list = _list
    for item in widget_list:
        item.pack_forget()
        item.grid_forget()
    srnoLabel=Label(window1,text="Sr No",bg="#232345",fg="white")
    srnoLabel.grid(row=0,column=0)    
    custLabel=Label(window1,text="Customer Name",bg="#232345",fg="white")
    custLabel.grid(row=0,column=1)
    mobLabel=Label(window1, text="Mobile No",bg="#232345",fg="white")
    mobLabel.grid(row=0,column=2)
    mycursor.execute("Select * from customer");
    r=1
    info=[]
    i=0
    for k in mycursor:
            info.append(Label(window1, bd=4, text=r))
            info[i].grid(row=r, column=0, pady=1)
            i=i+1
            info.append(Label(window1, bd=4, text=k[0]))
            info[i].grid(row=r, column=1, pady=1)
            i=i+1
            info.append(Label(window1, bd=4, text=k[1]))
            info[i].grid(row=r, column=2, pady=1)
            r+=1
            i=i+1
            
    #=====(Inside show customers)===

#=========================================================
    #===inserting new customer===
def added(name,mobile,result):
    global mycursor,conn
    addbtnclicked=1
    print("inside added",name,mobile)
    if(name=="" or mobile=="" or len(mobile)<10):
            result.configure(text="Wrong Info, Re-enter !",fg="red",font="Arial 18 bold")
            
    else:
            result.configure(text="New Customer Added !",fg="green",font="Arial 18 bold")
            print("validated")
            
            mycursor.execute("INSERT INTO customer Values (%s , %s)",(name,mobile))            
            conn.commit()
    
    
def add_customer(window1):
    global mycursor
    
    _list = window1.winfo_children()
    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())
    widget_list = _list
    for item in widget_list:
        item.pack_forget()
        item.grid_forget()
    
    #=====entering new customer====

    custName=Label(window1,text="Enter Customer Name : ")
    customer=Entry(window1,font="Arial 18 bold")
    custMob=Label(window1,text="Enter Mobile Name : ")
    mobile=Entry(window1,font="Arial 18 bold")
    result=Label(window1,text=" Enter Info..!",fg="blue",font="Arial 18 bold")
    result.grid(row=7)
    btn=Button(window1,text="Add",bg="#005e13",fg="white",command=lambda: added(customer.get(),mobile.get(),result)) 
    custName.grid(row=1)
    customer.grid(row=2)
    custMob.grid(row=3)
    mobile.grid(row=4)
    btn.grid(row=6)
    
#======customer menu=======

def clickedbtn2():
    c_menu_window = Tk()
    c_menu_window.geometry('600x300')
    c_menu_window.configure(bg="#232345")
    c_menu_window.title("Medical Inventory System")
    lbl = Label(c_menu_window, text="Customer Menu!")
    lbl.grid(column=0, row=0)
    lbl2 = Label(c_menu_window, text="What would you like to do!")
    lbl2.grid(column=0, row=1)
    btn1 = Button(c_menu_window, text="Show All Customers",fg="red", command=lambda: show_customers(c_menu_window))
    btn1.grid(column=0, row=2)
    btn2 = Button(c_menu_window, text="New Customer",fg="red", command=lambda: add_customer(c_menu_window))
    btn2.grid(column=0, row=3)
    btn4 = Button(c_menu_window, text="Return to main menu",fg="red", command=lambda:mclickedbtn5(c_menu_window))
    btn4.grid(column=0, row=4)
    c_menu_window.mainloop()
     
#=====Supplier Menu======

def show_suppliers(window1):
    global mycursor
    
    _list = window1.winfo_children()
    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())
    widget_list = _list
    for item in widget_list:
        item.pack_forget()
        item.grid_forget()
    srnoLabel=Label(window1,text="Sr No",bg="#232345",fg="white")
    srnoLabel.grid(row=0,column=0)    
    suppLabel=Label(window1,text="Supplier Name",bg="#232345",fg="white")
    suppLabel.grid(row=0,column=1)
    mobLabel=Label(window1, text="Mobile No",bg="#232345",fg="white")
    mobLabel.grid(row=0,column=2)
    mycursor.execute("Select * from supplier");

    r=1
    info=[]
    i=0
    for k in mycursor:
            info.append(Label(window1, bd=4, text=r))
            info[i].grid(row=r, column=0, pady=1)
            i=i+1
            info.append(Label(window1, bd=4, text=k[0]))
            info[i].grid(row=r, column=1, pady=1)
            i=i+1
            info.append(Label(window1, bd=4, text=k[1]))
            info[i].grid(row=r, column=2, pady=1)
            r+=1
            i=i+1
          #  print(k[0],k[1])
            
  #  print("Inside show suppliers")

    
    
def addedSupp(name,mobile,result):
    global mycursor,conn
    addbtnclicked=1
    print("inside addedSupp",name,mobile)
    if(name=="" or mobile=="" or len(mobile)<10):
            result.configure(text="Wrong Info, Re-enter !",fg="red",font="Arial 18 bold")
            
    else:
            result.configure(text="New Customer Added !",fg="green",font="Arial 18 bold")
            print("validated")
            
            mycursor.execute("INSERT INTO Supplier Values (%s , %s)",(name,mobile))           #===inserting supplier====
            conn.commit()
    
    
def add_supplier(window1):
    global mycursor
    
    _list = window1.winfo_children()
    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())
    widget_list = _list
    for item in widget_list:
        item.pack_forget()
        item.grid_forget()
    
    suppName=Label(window1,text="Enter Supplier Name : ")
    supplier=Entry(window1,font="Arial 18 bold")
    suppMob=Label(window1,text="Enter Mobile Name : ")
    mobile=Entry(window1,font="Arial 18 bold")
    result=Label(window1,text=" Enter Info..!",fg="blue",font="Arial 18 bold")
    result.grid(row=7)
    btn=Button(window1,text="Add",bg="#005e13",fg="white",command=lambda: addedSupp(supplier.get(),mobile.get(),result)) 
    suppName.grid(row=1)
    supplier.grid(row=2)
    suppMob.grid(row=3)
    mobile.grid(row=4)
    btn.grid(row=6)

#=======================supplier menu======
def clickedbtn3():
    s_menu_window = Tk()
    s_menu_window.geometry('600x300')
    s_menu_window.configure(bg="#232345")
    s_menu_window.title("Medical Inventory System")
    lbl = Label(s_menu_window, text="Supplier Menu!")
    lbl.grid(column=0, row=0)
    lbl2 = Label(s_menu_window, text="What would you like to do!")
    lbl2.grid(column=0, row=1)
    btn1 = Button(s_menu_window, text="Show All Suppliers",fg="red", command=lambda : show_suppliers(s_menu_window))
    btn1.grid(column=0, row=2)
    btn2 = Button(s_menu_window, text="New Supplier",fg="red", command=lambda: add_supplier(s_menu_window))
    btn2.grid(column=0, row=3)
    btn4 = Button(s_menu_window, text="Return to main menu",fg="red", command=lambda:mclickedbtn5(s_menu_window))
    btn4.grid(column=0, row=5)
    s_menu_window.mainloop()

#======Main Menu=====

window = Tk()
window.geometry('600x300')
window.configure(bg="#232345")
window.title("Medical Inventory System")
lbl = Label(window, text="Welcome to Medical Inventory System!")
lbl.place(x=150, y=10)
lbl2 = Label(window, text="What would you like to do!")
lbl2.place(x=10, y=50)
btn1 = Button(window, text="Medicine Menu",fg="green", command=clickedbtn1)
btn1.place(x=10, y=80)
btn2 = Button(window, text="Customer Menu",fg="green", command=clickedbtn2)
btn2.place(x=10, y=110)
btn3 = Button(window, text="Supplier Menu",fg="green", command=clickedbtn3)
btn3.place(x=10, y=140)
window.mainloop()