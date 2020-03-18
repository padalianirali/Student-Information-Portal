#importing required libraries and packages
from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

#insert method for insert
def insert():
    id=e_id.get()
    name=e_name.get()
    number=e_number.get()
    
    if(id=="" or name=="" or number==""):
        MessageBox.showinfo("Insert Status","All fields are mandatory")
    else:
        con=mysql.connect(host='localhost',user='root',passwd='',database='student_db')
        student_cursor = con.cursor()
        student_cursor.execute("insert into student_info values('"+id+"','"+name+"','"+number+"')")
        student_cursor.execute("commit")
        
        #to clear entry widget upon completion from character at position 0 until end
        e_id.delete(0,'end')
        e_name.delete(0,'end')
        e_number.delete(0,'end')
        
        #to update list with the inserted record
        show()
        MessageBox.showinfo("Insert Status","Record inserted successfully")
        con.close()
        
#delete method for delete    
def delete():
    id=e_id.get()

    if(id==""):
        MessageBox.showinfo("Delete Status","ID is mandatory")
    else:
        con=mysql.connect(host='localhost',user='root',passwd='',database='student_db')
        student_cursor = con.cursor()
        student_cursor.execute("delete from student_info where id = '"+id+"'")
        student_cursor.execute("commit")
        
        #to clear entry widget upon completion from character at position 0 until end
        e_id.delete(0,'end')
        e_name.delete(0,'end')
        e_number.delete(0,'end')
        
        #to update list with the deleted record
        show()
        MessageBox.showinfo("Delete Status","Record deleted successfully")
        con.close()

#update method for update
def update():
    id=e_id.get()
    name=e_name.get()
    number=e_number.get()
    
    if(id=="" or name=="" or number==""):
        MessageBox.showinfo("Update Status","All fields are mandatory")
    else:
        con=mysql.connect(host='localhost',user='root',passwd='',database='student_db')
        student_cursor = con.cursor()
        student_cursor.execute("update student_info set name='"+name+"',number='"+number+"' where id='"+id+"'")
        student_cursor.execute("commit")
        
        #to clear entry widget upon completion from character at position 0 until end
        e_id.delete(0,'end')
        e_name.delete(0,'end')
        e_number.delete(0,'end')
        
        #to update list with the updated record
        show()
        MessageBox.showinfo("Update Status","Record updated successfully")
        con.close()
        
#get method for fetch
def get():
    id=e_id.get()
    
    if(id==""):
        MessageBox.showinfo("Fetch Status","All fields are mandatory")
    else:
        con=mysql.connect(host='localhost',user='root',passwd='',database='student_db')
        student_cursor = con.cursor()
        student_cursor.execute("select * from student_info where id='"+id+"'")
        rows = student_cursor.fetchall()
        
        #to insert data into 0th position of entry widget (here entry widget itself)
        for r in rows:
            e_name.insert(0,r[1])
            e_number.insert(0,r[2])
        
        con.close()

#show method for list
def show():
    con=mysql.connect(host='localhost',user='root',passwd='',database='student_db')
    student_cursor = con.cursor()
    student_cursor.execute("select * from student_info")
    rows = student_cursor.fetchall()
    
    #to refresh and avoid repeat list entries displayed
    list.delete(0,list.size())
    
     #to insert data into list widget
    for r in rows:
        data = str(r[0])+' '+r[1]+' '+r[2]
        list.insert(list.size()+1,data)
        
    con.close()
    
#defining window
root = Tk()
root.title("Student Information Portal")
root.geometry("600x500")

#defining labels
id = Label(root,text="Enter ID",font=('bold',10))
id.place(x=20,y=30)

name = Label(root,text="Enter Name",font=('bold',10))
name.place(x=20,y=60)

number = Label(root,text="Enter Number",font=('bold',10))
number.place(x=20,y=90)

#defining entry widgets
e_id = Entry(root)
e_id.place(x=150,y=30)

e_name = Entry(root)
e_name.place(x=150,y=60)

e_number = Entry(root)
e_number.place(x=150,y=90)

#defining buttons
insert = Button(root, text="Insert", font=('bold',10), bg='navy', fg='white', command=insert)
insert.place(x=20,y=150)

delete = Button(root, text="Delete", font=('bold',10), bg='navy', fg='white', command=delete)
delete.place(x=100,y=150)

update = Button(root, text="Update", font=('bold',10), bg='navy', fg='white', command=update)
update.place(x=180,y=150)

get = Button(root, text="Fetch", font=('bold',10), bg='navy', fg='white', command=get)
get.place(x=265,y=150)

#defining list
list = Listbox(root)
list.place(x=350,y=30)
show()

root.mainloop()

