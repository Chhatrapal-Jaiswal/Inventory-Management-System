from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import mysql.connector
class employeeClass:
        def __init__(self,root):
                self.root = root
                self.root.geometry("1100x500+220+130")          #) x=220, y=130
                self.root.title("Inventory management System")
                self.root.configure(bg = "#EE7267")
                self.root.iconbitmap(r"C:\Users\Hp\Desktop\CLass Practice\Tkinter Project\images\emp_icon.ico")
                self.root.focus_force()         #) to enable another page in highlight mode.

                #-------Variables--------------------------
                self.var_searchby  = StringVar()
                self.var_searchtxt  = StringVar()


                self.var_emp_id  = StringVar()
                self.var_gender  = StringVar()
                self.var_contact  = StringVar()
                self.var_name  = StringVar()
                self.var_dob  = StringVar()
                self.var_doj  = StringVar()
                self.var_email  = StringVar()
                self.var_pass  = StringVar()
                self.var_utype  = StringVar()
               
                self.var_salary  = StringVar()
                


                #------------Search Frame----------------
                SearchFrame = LabelFrame(self.root,text="Search Employee" , bg="#EE7267",font=("Bookman Old Style",14,"bold"),bd=2,relief=RIDGE)
                SearchFrame.place(x=250,y=20,width=630,height=70)

                #---------------------Options=================
                #1)
                img_srch = Image.open(r"C:\Users\Hp\Desktop\CLass Practice\Tkinter Project\images\search.png")
                img_srch = img_srch.resize((20,20))
                self.img_srch = ImageTk.PhotoImage(img_srch)





                
                cmb_search = ttk.Combobox(SearchFrame,textvariable = self.var_searchby,values=("Select","Email","Name","Contact"),state="readonly",justify=CENTER,font=("Bookman Old Style",15,"bold"))  #) 
                cmb_search.place(x=10,y=10,width=180)
                cmb_search.current(0)

                txt_search = Entry(SearchFrame,textvariable=self.var_searchtxt,font=("Bookman Old Style",15,"bold"),bg="#F8A5EA").place(x=200,y=10)

                btn_search = Button(SearchFrame,text="Search",image=self.img_srch,compound=LEFT,padx=12,anchor='w',font=("Bookman Old Style",15,"bold"),bg="#FFDDE1",fg="bLACK",cursor="hand2",command=self.search).place(x=472,y=9, width=148,height=30)

                #------------------------Title======================

                title = Label(self.root,text="Employee Details", font=("Bookman Old Style",15),bg="#0f4d7d",fg="white").place(x=50,y=100,width=1000)


                #-------------------Content-------------------------

                #---------ROW 1---------------

                lbl_empid = Label(self.root,text="Emp ID", font=("Bookman Old Style",15,"bold"),bg="#EE7267",fg="#F8D8DF").place(x=50,y=150)
                lbl_gender = Label(self.root,text="Gender", font=("Bookman Old Style",15,"bold"),bg="#EE7267",fg="#F8D8DF").place(x=350,y=150)
                lbl_contact = Label(self.root,text="Contact", font=("Bookman Old Style",15,"bold"),bg="#EE7267",fg="#F8D8DF").place(x=750,y=150)

                txt_empid = Entry(self.root,textvariable=self.var_emp_id, font=("Georgia",15),bg="#F8A5EA").place(x=150,y=150,width=180)
                #txt_gender = Entry(self.root,textvariable=self.var_gender, font=("Georgia",15),bg="white").place(x=500,y=150,width=180)
                cmb_gender = ttk.Combobox(self.root,textvariable = self.var_gender,values=("Male","Female","Other","Select"),state="readonly",justify=CENTER,font=("Georgia",15))
                cmb_gender.place(x=500,y=150,width=180)
                cmb_gender.current(3)
                txt_contact = Entry(self.root,textvariable=self.var_contact, font=("Georgia",15),bg="#F8A5EA").place(x=850,y=150,width=180)




                #-------ROW 2---------------------------------------------

                lbl_name = Label(self.root,text="Name", font=("Bookman Old Style",15,"bold"),bg="#EE7267",fg="#F8D8DF").place(x=50,y=190)
                lbl_dob = Label(self.root,text="D.O.B", font=("Bookman Old Style",15,"bold"),bg="#EE7267",fg="#F8D8DF").place(x=350,y=190)
                lbl_doj = Label(self.root,text="D.O.J", font=("Bookman Old Style",15,"bold"),bg="#EE7267",fg="#F8D8DF").place(x=750,y=190)

                txt_name = Entry(self.root,textvariable=self.var_name, font=("Georgia",15),bg="#F8A5EA").place(x=150,y=190,width=180)
                txt_dob = Entry(self.root,textvariable=self.var_dob, font=("Georgia",15),bg="#F8A5EA").place(x=500,y=190,width=180)
                txt_doj = Entry(self.root,textvariable=self.var_doj, font=("Georgia",15),bg="#F8A5EA").place(x=850,y=190,width=180)





                 #-------ROW 3---------------------------------------------

                lbl_email = Label(self.root,text="E-Mail", font=("Bookman Old Style",15,"bold"),bg="#EE7267",fg="#F8D8DF").place(x=50,y=230)
                lbl_pass = Label(self.root,text="Password", font=("Bookman Old Style",15,"bold"),bg="#EE7267",fg="#F8D8DF").place(x=350,y=230)
                lbl_utype = Label(self.root,text="User Type", font=("Bookman Old Style",15,"bold"),bg="#EE7267",fg="#F8D8DF").place(x=740,y=230)

                self.txt_email = Entry(self.root,textvariable=self.var_email, font=("Georgia",15),bg="#F8A5EA").place(x=150,y=230,width=180)
                self.txt_pass = Entry(self.root,textvariable=self.var_pass, font=("Georgia",15),bg="#F8A5EA").place(x=500,y=230,width=180)
                cmb_utype = ttk.Combobox(self.root,textvariable = self.var_utype,values=("Select","Admin","Employee"),state="readonly",justify=CENTER,font=("Georgia",15))
                cmb_utype.place(x=850,y=230,width=180)
                cmb_utype.current(0)





                 #-------ROW 4---------------------------------------------

                lbl_address = Label(self.root,text="Address", font=("Bookman Old Style",15,"bold"),bg="#EE7267",fg="#F8D8DF").place(x=50,y=270)
                lbl_salary = Label(self.root,text="Salary", font=("Bookman Old Style",15,"bold"),bg="#EE7267",fg="#F8D8DF").place(x=500,y=270)
               
                self.txt_address = Text(self.root,font=("Georgia",15),bg="light yellow") # we have declared this textbox as self. becoz well take the values from this textbox.
                self.txt_address.place(x=150,y=270,width=300,height=60)
                txt_salary = Entry(self.root,textvariable=self.var_salary,font=("Georgia",15),bg="#F8A5EA").place(x=600,y=270,width=180)



                #-------------Button--------------------------
                #1)
                icon1 = Image.open(r"C:\Users\Hp\Desktop\CLass Practice\Tkinter Project\images\save.jpg")
                photo1 = icon1.resize((20,20))
                self.icon1_side = ImageTk.PhotoImage(photo1)

                #2)
                icon2 = Image.open(r"C:\Users\Hp\Desktop\CLass Practice\Tkinter Project\images\update2.png")
                photo2 = icon2.resize((20,20))
                self.icon2_side = ImageTk.PhotoImage(photo2)

                #3)
                icon3 = Image.open(r"C:\Users\Hp\Desktop\CLass Practice\Tkinter Project\images\delete.png")
                photo3 = icon3.resize((20,20))
                self.icon3_side = ImageTk.PhotoImage(photo3)

                #4)
                icon4 = Image.open(r"C:\Users\Hp\Desktop\CLass Practice\Tkinter Project\images\clear.png")
                photo4 = icon4.resize((20,20))
                self.icon4_side = ImageTk.PhotoImage(photo4)



                             

                btn_add = Button(self.root,text="SAVE",image=self.icon1_side,compound=LEFT,padx=5,anchor='w',font=("Georgia",15),cursor="hand2",command=self.add)
                btn_add.place(x=500,y=305, width=110,height=28)
                btn_update = Button(self.root,text="UPDATE",image=self.icon2_side,compound=LEFT,padx=2,anchor='w',font=("Georgia",15),bg="#72f9d5",fg="black",cursor="hand2",command=self.update).place(x=620,y=305, width=110,height=28)
                btn_delete = Button(self.root,text="DELETE",image=self.icon3_side,compound=LEFT,padx=2,anchor='w',font=("Georgia",15),bg="#f9bb2a",fg="black",cursor="hand2",command=self.delete).place(x=740,y=305, width=110,height=28)
                btn_clear = Button(self.root,text="CLEAR",image=self.icon4_side,compound=LEFT,padx=2,anchor='w',font=("Georgia",15),bg="#42C9F1",fg="black",cursor="hand2",command=self.clear).place(x=860,y=305, width=110,height=28)


                
                #--------------Employee Details----------------------

                emp_frame = Frame(self.root,bd=3,relief=RIDGE)
                emp_frame.place(x=0,y=350,relwidth=1,height=150)

                #) Creating scrollBar
                scrolly = Scrollbar(emp_frame,orient=VERTICAL)  
                scrollx = Scrollbar(emp_frame,orient=HORIZONTAL)

                #) Creating Treeview                        column name are case sensitive(database)                                            yscrollcommand & xscrollcommand is used for placing the scrollbar on treeview.
                self.EmployeeTable = ttk.Treeview(emp_frame,columns=("eid","name","email","gender","contact","dob","doj","pass","utype","address","salary"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
                scrollx.pack(side=BOTTOM,fill=X)        #) Packing the scrollBar
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.config(command=self.EmployeeTable.xview)        #)for functioning of scrollbar
                scrolly.config(command=self.EmployeeTable.yview)
                

                #) defining heading(Titles to be displayed, using text="")
                self.EmployeeTable.heading("eid",text="EMP ID")
                self.EmployeeTable.heading("name",text="NAME")
                self.EmployeeTable.heading("email",text="E-MAIL")
                self.EmployeeTable.heading("gender",text="GENDER")
                self.EmployeeTable.heading("contact",text="CONTACT")
                self.EmployeeTable.heading("dob",text="D.O.B")
                self.EmployeeTable.heading("doj",text="D.O.J")
                self.EmployeeTable.heading("pass",text="PASSWORD")
                self.EmployeeTable.heading("utype",text="USER-TYPE")
                self.EmployeeTable.heading("address",text="ADDRESS")
                self.EmployeeTable.heading("salary",text="SALARY")

                self.EmployeeTable["show"] = "headings"         #)This is used to remove the deafault heading from treeview. nad to used only defined ones.

                #) Defining each column width.
                self.EmployeeTable.column("eid",width=90)
                self.EmployeeTable.column("name",width=100)
                self.EmployeeTable.column("email",width=100)
                self.EmployeeTable.column("gender",width=100)
                self.EmployeeTable.column("contact",width=100)
                self.EmployeeTable.column("dob",width=100)
                self.EmployeeTable.column("doj",width=100)
                self.EmployeeTable.column("pass",width=100)
                self.EmployeeTable.column("utype",width=100)
                self.EmployeeTable.column("address",width=100)
                self.EmployeeTable.column("salary",width=100)
                self.EmployeeTable.pack(fill=BOTH,expand=1)
                self.EmployeeTable.bind("<ButtonRelease-1>",self.get_data)
                #)<ButtonRelease-1> is a event in bind functn, which will on clicking calls a fuctn self.get_data 

                self.show() #) whenever the program runs, it will displays the value from database.

#=============================================================================================================================================

        #) first import mysql.connector module for connecting to database.
         # function for saving/adding the data into database.        
        def add(self):
                mydb = mysql.connector.connect(host="localhost", user="root",password="oramca",database="mydatabase")
                mycursor = mydb.cursor()
                try:
                        if self.var_emp_id.get()=="":
                                messagebox.showerror("Error","Employee ID must be required",parent=self.root)
                        else:
                                mycursor.execute("select * from employee where eid= %s " , (self.var_emp_id.get(),)) 
                                row  = mycursor.fetchone()
                                if row!= None: #-----True/False.
                                        messagebox.showerror("Error!","This Employee Id already assigned, Try different ID",parent = self.root)
                                else:
                                        mycursor.execute("Insert Into employee (eid,name,email,gender,contact,dob,doj,pass,utype,address,salary) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                self.var_emp_id.get(),
                                                                self.var_name.get(),
                                                                self.var_email.get(),
                                                                self.var_gender.get(),
                                                                self.var_contact.get(),
                                                                self.var_dob.get(),
                                                                self.var_doj.get(),
                                                                self.var_pass.get(),
                                                                self.var_utype.get(),
                                                                self.txt_address.get('1.0',END),
                                                                self.var_salary.get(),



                                        )) 
                                        mydb.commit()
                                        messagebox.showinfo("Sucess","Employee Added Successfully",parent=self.root) 
                                        self.show()        
                except Exception as ex:
                        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent = self.root)      
                        
                   
        # function for displaying data in the tree view after submitting the data succesfully.
        def show(self):
                 mydb = mysql.connector.connect(host="localhost", user="root",password="oramca",database="mydatabase")
                 mycursor = mydb.cursor()
                 try:
                        mycursor.execute("select * from employee") 
                        rows=mycursor.fetchall()
                        self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                        for row in rows:
                                self.EmployeeTable.insert('',END,values=row)    
                 except Exception as ex:
                        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent = self.root)    




        # on clicking the data on treeview the data will be displayed on the respected cell.
        def get_data(self,ev):
                f = self.EmployeeTable.focus()
                content = (self.EmployeeTable.item(f))  #passing in form of tuple
                row  = content['values']
                #print(row)
                self.var_emp_id.set(row[0])
                self.var_name.set(row[1])
                self.var_email.set(row[2])
                self.var_gender.set(row[3])
                self.var_contact.set(row[4])
                self.var_dob.set(row[5])
                self.var_doj.set(row[6])
                self.var_pass.set(row[7])
                self.var_utype.set(row[8])
                self.txt_address.delete('1.0',END),
                self.txt_address.insert(END,row[9]),
                self.var_salary.set(row[10])








        # Function for updating values.
        def update(self):
                mydb = mysql.connector.connect(host="localhost", user="root",password="oramca",database="mydatabase")
                mycursor = mydb.cursor()
                try:
                        if self.var_emp_id.get()=="":
                                messagebox.showerror("Error","Employee ID must be required",parent=self.root)
                        else:
                                mycursor.execute("select * from employee where eid= %s " , (self.var_emp_id.get(),)) 
                                row  = mycursor.fetchone()
                                if row== None: #-----True/False.(If i found the employee id as mentioned then only i will update.)
                                        messagebox.showerror("Error!","Invalid employee ID",parent = self.root)
                                else:
                                        mycursor.execute("update employee set name= %s,email= %s,gender= %s,contact= %s,dob= %s,doj= %s,pass= %s,utype= %s,address= %s,salary= %s where eid = %s",(
                                                              
                                                                self.var_name.get(),
                                                                self.var_email.get(),
                                                                self.var_gender.get(),
                                                                self.var_contact.get(),
                                                                self.var_dob.get(),
                                                                self.var_doj.get(),
                                                                self.var_pass.get(),
                                                                self.var_utype.get(),
                                                                self.txt_address.get('1.0',END),
                                                                self.var_salary.get(),
                                                                self.var_emp_id.get(),



                                        )) 
                                        mydb.commit()
                                        messagebox.showinfo("Sucess","Employee Updated Successfully",parent=self.root) 
                                        self.show()        
                except Exception as ex:
                        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent = self.root)    
               
                        



        def delete(self):
                 mydb = mysql.connector.connect(host="localhost", user="root",password="oramca",database="mydatabase")
                 mycursor = mydb.cursor()
                 try:
                      if self.var_emp_id.get()=="":
                                messagebox.showerror("Error","Employee ID must be required",parent=self.root)
                      else:
                                mycursor.execute("select * from employee where eid= %s " , (self.var_emp_id.get(),)) 
                                row  = mycursor.fetchone()
                                if row== None: #-----True/False.(If i found the employee id as mentioned then only i will update.)
                                        messagebox.showerror("Error!","Invalid employee ID",parent = self.root) 
                                else:
                                        op = messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)  #message box for asking whther user really wanted to delte.
                                        if op == True:
                                                mycursor.execute("delete from employee where eid=%s",(self.var_emp_id.get(),))
                                                mydb.commit()  
                                                messagebox.showinfo("Delete","Employee Deleted Successfully",parent = self.root)
                                                self.clear()

                 except Exception as ex:
                        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent = self.root) 



        def clear(self):
                self.var_emp_id.set("")
                self.var_name.set("")
                self.var_email.set("")
                self.var_gender.set("Select")
                self.var_contact.set("")
                self.var_dob.set("")
                self.var_doj.set("")
                self.var_pass.set("")
                self.var_utype.set("Admin")
                self.txt_address.delete('1.0',END),
                self.var_salary.set("")
                self.var_searchtxt.set("")
                self.var_searchby.set("Select")
                self.show()



        def search(self):
                 mydb = mysql.connector.connect(host="localhost", user="root",password="oramca",database="mydatabase")
                 mycursor = mydb.cursor()
                 try:
                        if self.var_searchby.get()=="Select":
                                messagebox.showerror("Error","Select search by option",parent=self.root)
                        elif self.var_searchtxt.get()=="":
                                messagebox.showerror("Error","Search area should be required",parent=self.root)
                        else:
                                mycursor.execute("select * from employee WHERE " +self.var_searchby.get()+ " LIKE '%"+self.var_searchtxt.get()+"%'") 
                                rows=mycursor.fetchall()
                                if len(rows)!=0:
                                        self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                                        for row in rows:
                                                self.EmployeeTable.insert('',END,values=row)  
                                else:
                                        messagebox.showerror("Error","No record found..",parent=self.root)  
                 except Exception as ex:
                        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent = self.root)    













if __name__=="__main__":
        root=Tk()
        obj=employeeClass(root)
        root.mainloop()
               
