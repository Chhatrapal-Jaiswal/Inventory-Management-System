from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import mysql.connector
class supplierClass:
        def __init__(self,root):
                self.root = root
                self.root.geometry("1100x500+220+130")
                self.root.title("Inventory management System")
                self.root.configure(bg = "#F79797")
                self.root.iconbitmap(r"C:\Users\Hp\Desktop\CLass Practice\Tkinter Project\images\supplier_icon.ico")
                self.root.focus_force()         #) to enable another page in highlight mode.

                #-------Variables--------------------------
                self.var_searchby  = StringVar()
                self.var_searchtxt  = StringVar()


                self.var_sup_invoice = StringVar()
                self.var_name  = StringVar()
                self.var_contact  = StringVar()
               
                


                #------------Search Frame----------------

                #---------------------Options=================
                #1)
                img_srch = Image.open(r"C:\Users\Hp\Desktop\CLass Practice\Tkinter Project\images\search.png")
                img_srch = img_srch.resize((20,20))
                self.img_srch = ImageTk.PhotoImage(img_srch)





                
                lbl_search = Label(self.root,text="Invoice No.",font=("Gabriola",22,"bold"),bg="#F79797")
                lbl_search.place(x=700,y=65)
                

                txt_search = Entry(self.root,textvariable=self.var_searchtxt,font=("Georgia",15),bg="#F58484").place(x=810,y=80,width=160)

                btn_search = Button(self.root,text="Search",image=self.img_srch,compound=LEFT,padx=8,anchor='w',font=("Gabriola",15,'bold'),bg="#167F0A",fg="white",cursor="hand2",command=self.search).place(x=980,y=79, width=100,height=30)

                #------------------------Title======================

                title = Label(self.root,text="Supplier Details", font=("Gabriola",20,"bold"),bg="#0f4d7d",fg="#9CF7C8").place(x=50,y=10,width=1000,height=40)


                #-------------------Content-------------------------

                #---------ROW 1---------------

                lbl_supplier_invoice = Label(self.root,text=" Invoice No: ", font=("Gabriola",22,"bold"),bg="#F79797").place(x=50,y=62)
               
                txt_supplier_invoice = Entry(self.root,textvariable=self.var_sup_invoice, font=("Georgia",15),bg="#F58484").place(x=180,y=80,width=180)

               


                #-------ROW 2---------------------------------------------

                lbl_name = Label(self.root,text="Name", font=("Gabriola",22,"bold"),bg="#F79797").place(x=58,y=105)
               
                txt_name = Entry(self.root,textvariable=self.var_name, font=("Georgia",15),bg="#F58484").place(x=180,y=120,width=180)
                




                 #-------ROW 3---------------------------------------------

                lbl_contact = Label(self.root,text=" Contact", font=("Gabriola",22,"bold"),bg="#F79797").place(x=50,y=145)
               
                self.txt_contact = Entry(self.root,textvariable=self.var_contact, font=("Georgia",15),bg="#F58484").place(x=180,y=160,width=180)
               




                 #-------ROW 4---------------------------------------------

                lbl_desc = Label(self.root,text="Description", font=("Gabriola",22,"bold"),bg="#F79797").place(x=50,y=200)
                
                self.txt_descr = Text(self.root,font=("Georgia",15),bg="#F58484")
                self.txt_descr.place(x=180,y=200,width=450,height=90)
               


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





                

                btn_add = Button(self.root,text="SAVE",image=self.icon1_side,compound=LEFT,padx=5,anchor='w',font=("Georgia",15),bg="#F55555",fg="#FCDAD5",cursor="hand2",command=self.add).place(x=180,y=400, width=110,height=35)
                btn_update = Button(self.root,text="UPDATE",image=self.icon2_side,compound=LEFT,padx=5,anchor='w',font=("Georgia",15),bg="#002661",fg="#F36DF1",cursor="hand2",command=self.update).place(x=300,y=400, width=120,height=35)
                btn_delete = Button(self.root,text="DELETE",image=self.icon3_side,compound=LEFT,padx=5,anchor='w',font=("Georgia",15),bg="#FFDDE1",fg="#F36DF1",cursor="hand2",command=self.delete).place(x=430,y=400, width=120,height=35)
                btn_clear = Button(self.root,text="CLEAR",image=self.icon4_side,compound=LEFT,padx=5,anchor='w',font=("Georgia",15),bg="#42C9F1",fg="#0C1C92",cursor="hand2",command=self.clear).place(x=560,y=400, width=110,height=35)


                #--------------Employee Details----------------------

                emp_frame = Frame(self.root,bd=3,relief=RIDGE)
                emp_frame.place(x=700,y=120,width=380,height=350)

                scrolly = Scrollbar(emp_frame,orient=VERTICAL)
                scrollx = Scrollbar(emp_frame,orient=HORIZONTAL)

                self.supplierTable = ttk.Treeview(emp_frame,columns=("invoice","name","contact","descr"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.config(command=self.supplierTable.xview)
                scrolly.config(command=self.supplierTable.yview)
                


                self.supplierTable.heading("invoice",text="INVOICE")
                self.supplierTable.heading("name",text="NAME")
                self.supplierTable.heading("contact",text="CONTACT")
                self.supplierTable.heading("descr",text="DESCRIPTION")
                

                self.supplierTable["show"] = "headings"

                self.supplierTable.column("invoice",width=90)
                self.supplierTable.column("name",width=100)
                self.supplierTable.column("contact",width=100)
                self.supplierTable.column("descr",width=110)
               
                self.supplierTable.pack(fill=BOTH,expand=1)
                self.supplierTable.bind("<ButtonRelease-1>",self.get_data)


                self.show()

#=============================================================================================================================================
         # function for saving/adding the data into database.        
        def add(self):
                mydb = mysql.connector.connect(host="localhost", user="root",password="oramca",database="mydatabase")
                mycursor = mydb.cursor()
                try:
                        if self.var_sup_invoice.get()=="":
                                messagebox.showerror("Error","Invoice  must be required",parent=self.root)
                        else:
                                mycursor.execute("select * from supplier where invoice = %s " , (self.var_sup_invoice.get(),)) 
                                row  = mycursor.fetchone()
                                if row!= None: #-----True/False.
                                        messagebox.showerror("Error!","This Invoice No. already assigned, Try different ID",parent = self.root)
                                else:
                                        mycursor.execute("Insert Into supplier (invoice,name,contact,descr) values(%s,%s,%s,%s)",(
                                                                self.var_sup_invoice.get(),
                                                                self.var_name.get(),
                                                                self.var_contact.get(),
                                                                self.txt_descr.get('1.0',END),
                                                               
                                        )) 
                                                               
                                                                
                                        mydb.commit()
                                        messagebox.showinfo("Sucess","Supplier Added Successfully",parent=self.root) 
                                        self.show()        

                except Exception as ex:
                        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent = self.root)      


                        
                   
        # function for displaying data in the tree view after submitting the data succesfully.
        def show(self):
                 mydb = mysql.connector.connect(host="localhost", user="root",password="oramca",database="mydatabase")
                 mycursor = mydb.cursor()
                 try:
                        mycursor.execute("select * from supplier") 
                        rows=mycursor.fetchall()
                        self.supplierTable.delete(*self.supplierTable.get_children())
                        for row in rows:
                                self.supplierTable.insert('',END,values=row)    
                 except Exception as ex:
                        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent = self.root)    




        # on clicking the data on treeview the data will be displayed on the respected cell.
        def get_data(self,ev):
                f = self.supplierTable.focus()
                content = (self.supplierTable.item(f))  #passing in form of tuple
                row  = content['values']
                #print(row)
                self.var_sup_invoice.set(row[0])
                self.var_name.set(row[1])
                self.var_contact.set(row[2])
                self.txt_descr.delete('1.0',END),
                self.txt_descr.insert(END,row[3]),








        # Function for updating values.
        def update(self):
                mydb = mysql.connector.connect(host="localhost", user="root",password="oramca",database="mydatabase")
                mycursor = mydb.cursor()
                try:
                        if self.var_sup_invoice.get()=="":
                                messagebox.showerror("Error","Invoice No. must be required",parent=self.root)
                        else:
                                mycursor.execute("select * from supplier where invoice= %s " , (self.var_sup_invoice.get(),)) 
                                row  = mycursor.fetchone()
                                if row== None: #-----True/False.(If i found the employee id as mentioned then only i will update.)
                                        messagebox.showerror("Error!","Invalid Invoice No.",parent = self.root)
                                else:
                                        mycursor.execute("update supplier set name= %s,contact= %s,descr= %s where invoice = %s",(
                                                              
                                                                self.var_name.get(),
                                                                self.var_contact.get(),
                                                                self.txt_descr.get('1.0',END),
                                                                self.var_sup_invoice.get(),
                    
                                                              
                                        )) 
                                        mydb.commit()
                                        messagebox.showinfo("Sucess","Supplier Updated Successfully",parent=self.root) 
                                                               
                                        self.show()        

                except Exception as ex:

                        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent = self.root)    

               
                        



        def delete(self):
                 mydb = mysql.connector.connect(host="localhost", user="root",password="oramca",database="mydatabase")
                 mycursor = mydb.cursor()
                 try:
                      if self.var_sup_invoice.get()=="":
                                messagebox.showerror("Error","Invoice No. must be required",parent=self.root)
                      else:
                                mycursor.execute("select * from supplier where invoice= %s " , (self.var_sup_invoice.get(),)) 
                                row  = mycursor.fetchone()
                                if row== None: #-----True/False.(If i found the employee id as mentioned then only i will update.)
                                        messagebox.showerror("Error!","Invalid Invoice No.",parent = self.root) 
                                else:
                                        op = messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)  #message box for asking whther user really wanted to delte.
                                        if op == True:
                                                mycursor.execute("delete from supplier where invoice=%s",(self.var_sup_invoice.get(),))
                                                mydb.commit()  
                                                messagebox.showinfo("Delete","Supplier Deleted Successfully",parent = self.root)
                                                self.clear()

                 except Exception as ex:
                        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent = self.root) 



        def clear(self):
                self.var_sup_invoice.set("")
                self.var_name.set("")
                self.var_contact.set("")
                self.txt_descr.delete('1.0',END),
                self.var_searchtxt.set("")
                
               
                self.show()
               
               



        def search(self):
                 mydb = mysql.connector.connect(host="localhost", user="root",password="oramca",database="mydatabase")
                 mycursor = mydb.cursor()
                 try:
                       
                        if self.var_searchtxt.get()=="":
                                messagebox.showerror("Error","Invoice No. should be required",parent=self.root)
                        else:
                                mycursor.execute("select * from supplier WHERE invoice = %s", (self.var_searchtxt.get(),))      #'%s' is a place holder.
                                row=mycursor.fetchone()
                                if row!=None:
                                        self.supplierTable.delete(*self.supplierTable.get_children())
                                        self.supplierTable.insert('',END,values=row)  
                                else:   #) if row == None
                                        messagebox.showerror("Error","No record found..",parent=self.root)  
                                       
                 except Exception as ex:
                        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent = self.root)    













if __name__=="__main__":
        root=Tk()
        obj=supplierClass(root)
        root.mainloop()
               
