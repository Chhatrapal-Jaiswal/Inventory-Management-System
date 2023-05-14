from tkinter import *
from PIL import Image,ImageTk
from Employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass
import mysql.connector
from tkinter import ttk,messagebox
import os
import time
class IMS:
        def __init__(self,root):
                self.root = root
                self.root.geometry("1350x700+0+0")
                self.root.title("Inventory management System")
                self.root.configure(bg = "#FECEA8")


                #-------------------Title_--------------------
                icon = Image.open("E:\Paul self practice\Tkinter Project\images\logo.png")
                photo = icon.resize((80,80))
                self.icon_title = ImageTk.PhotoImage(photo)
                title = Label(self.root, text="Inventory Management System",image=self.icon_title,compound = LEFT,font=("Gabriola",40,"bold"),bg="#2A363B" , fg="white",anchor="w",padx=20)
                title.place(x=0,y=0,relwidth=1,height=70)


                #-------------Button Logout--------------


                self.btn_logout = Button(root, text="Logout",font=("Gabriola",30,"bold"), bg="#B7E778",cursor="hand2",command=self.logout)
                self.btn_logout.place(x=1150,y=10,height=50,width=160)

                self.btn_logout.bind("<Enter>",self.button_hover)
                self.btn_logout.bind("<Leave>",self.button_hover_leave)


                #---------------------------------Clock-----------------------


                self.lbl_clock = Label(root, text="Welcome to Inventory Management System\t\t Date: DD-MM-YYY\t\t  TIME: HH:MM:SS" ,font=("Gabriola",15,"bold"), bg="#E84A5F" , fg="white")
                self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)




                #-----------------------------Left Menu---------------------------


                icon = Image.open(r"C:\Users\Hp\Desktop\CLass Practice\Tkinter Project_Draft\images\difference.png")
                photo = icon.resize((80,80), Image.ANTIALIAS)
                self.menu_logo = ImageTk.PhotoImage(photo)



                #--------------------Creating left side menu.

                Leftmenu = Frame(root,bd=2,relief=RIDGE,bg="#FF847B")
                Leftmenu.place(x=0,y=102,width=200,height=605)



                #--------------------creating label for placing image-------------

                lbl_menu_logo = Label(Leftmenu,image=self.menu_logo,bg="#FF847B").pack(side = TOP, fill=X)

                lbl_menu = Label(Leftmenu, text="MENU" ,font=("Gabriola",20), bg="#009688")
                lbl_menu.pack(fill=X)

                #================== Images on left frame buttons ==================================
                #1)
                icon = Image.open(r"C:\Users\Hp\Desktop\CLass Practice\Tkinter Project\images\employee.png")
                photo = icon.resize((60,60))
                self.icon_side = ImageTk.PhotoImage(photo)

                 #2)
                icon2 = Image.open(r"C:\Users\Hp\Desktop\CLass Practice\Tkinter Project\images\supplier.png")
                photo2 = icon2.resize((60,60))
                self.icon2_side = ImageTk.PhotoImage(photo2)

                #3)
                icon3 = Image.open(r"C:\Users\Hp\Desktop\CLass Practice\Tkinter Project\images\category.png")
                photo3 = icon3.resize((60,60))
                self.icon3_side = ImageTk.PhotoImage(photo3)

                #4)
                icon4 = Image.open(r"C:\Users\Hp\Desktop\CLass Practice\Tkinter Project\images\product.png")
                photo4 = icon4.resize((60,60))
                self.icon4_side = ImageTk.PhotoImage(photo4)

                #5)
                icon5 = Image.open(r"C:\Users\Hp\Desktop\CLass Practice\Tkinter Project\images\sale.png")
                photo5 = icon5.resize((70,70))
                self.icon5_side = ImageTk.PhotoImage(photo5)




                



                btn_employee = Button(Leftmenu,text="EMPLOYEE",image=self.icon_side,compound=LEFT,padx=5,anchor='w',font=("Gabriola",20,"bold","underline"), bg="#FF847B", bd=2, cursor="hand2", relief=RIDGE, command = self.employee)
                btn_employee.pack(side = TOP,fill=X)

                btn_supplier = Button(Leftmenu,text="SUPPLER",image=self.icon2_side,compound=LEFT,padx=5,anchor='w',font=("Gabriola",20,"bold","underline"), bg="#FF847B", bd=2, cursor="hand2",relief=RIDGE,command=self.supplier)
                btn_supplier.pack(fill=X)

                btn_category = Button(Leftmenu, text="CATEGORY",image=self.icon3_side,compound=LEFT,padx=5,anchor='w',font=("Gabriola",20,"bold","underline"), bg="#FF847B", bd=2,  cursor="hand2",relief=RIDGE,command = self.category)
                btn_category.pack(fill=X)

                product = Button(Leftmenu, text="PRODUCT" ,image=self.icon4_side,compound=LEFT,padx=5,anchor='w',font=("Gabriola",20,"bold","underline"), bg="#FF847B", bd=2,  cursor="hand2",relief=RIDGE,command=self.product)
                product.pack(fill=X)

                btn_sales = Button(Leftmenu, text="SALES" ,image=self.icon5_side,compound=LEFT,padx=5,anchor='w',font=("Gabriola",20,"bold","underline"), bg="#FF847B", bd=2,  cursor="hand2",relief=RIDGE,command=self.sales)
                btn_sales.pack(fill=X)







                #-------------------------------------------------Content------------------------------------

                self.lbl_employee = Label(self.root,text="Total Employee\n [0]",bg="#33bbf9",bd=5,relief="ridge", fg="White",font=("Georgia",20,"bold"))
                self.lbl_employee.place(x=300,y=120,height=150,width=300)

                self.lbl_supplier = Label(self.root,text="Total Supplier\n [0]",bg="#ff5722",bd=5,relief="ridge", fg="White",font=("Georgia",20,"bold"))
                self.lbl_supplier.place(x=650,y=120,height=150,width=300)

                self.lbl_category = Label(self.root,text="Total Category\n [0]",bg="#009688",bd=5,relief="ridge", fg="White",font=("Georgia",20,"bold"))
                self.lbl_category.place(x=1000,y=120,height=150,width=300)

                self.lbl_product = Label(self.root,text="Total Product\n [0]",bg="#607d8b",bd=5,relief="ridge", fg="White",font=("Georgia",20,"bold"))
                self.lbl_product.place(x=300,y=300,height=150,width=300)

                self.lbl_sales = Label(self.root,text="Total Sales\n [0]",bg="#ffc107",bd=5,relief="ridge", fg="White",font=("Georgia",20,"bold"))
                self.lbl_sales.place(x=650,y=300,height=150,width=300)





                #---------------------------------Footer-----------------------

                lbl_footer = Label(self.root, text="IMS-Inventory Management System | By:- Chhatrapal Jaiswal\n" ,font=("Gabriola",12), bg="#DC5A41" , fg="white")
                lbl_footer.place(x=0,y=670,height=40,width=1350)

                self.update_content()
        
#--------------------------------------------------------------------------------------------------------


        def employee(self):
                self.new_win = Toplevel(self.root)
                self.new_obj = employeeClass(self.new_win)




        def supplier(self):
                self.new_win = Toplevel(self.root)
                self.new_obj = supplierClass(self.new_win)


        def category(self):
                self.new_win = Toplevel(self.root)
                self.new_obj = categoryClass(self.new_win)



        def product(self):
                self.new_win = Toplevel(self.root)
                self.new_obj = productClass(self.new_win)



        def sales(self):
                self.new_win = Toplevel(self.root)
                self.new_obj = salesClass(self.new_win)


        def update_content(self):
                mydb = mysql.connector.connect(host="localhost", user="root",password="oramca",database="mydatabase")
                mycursor = mydb.cursor()
                try:
                        mycursor.execute('select * from product')
                        product = mycursor.fetchall()
                        self.lbl_product.config(text=f'Total Products\n [{str(len(product))}]')

                        mycursor.execute('select * from supplier')
                        supplier = mycursor.fetchall()
                        self.lbl_supplier.config(text=f'Total Suppliers\n [{str(len(supplier))}]')

                        mycursor.execute('select * from category')
                        category = mycursor.fetchall()
                        self.lbl_category.config(text=f'Total Category\n [{str(len(category))}]')

                        mycursor.execute('select * from employee')
                        employee = mycursor.fetchall()
                        self.lbl_employee.config(text=f'Total Employees\n [{str(len(employee))}]')
                        bill=len(os.listdir('Bill')) 
                        self.lbl_sales.config(text=f'Total sales\n [{str(bill)}]')



                        time_ = time.strftime("%H:%M:%S")
                        date_ = time.strftime("%d-%m-%Y")
                        self.lbl_clock.config(text=f"Welcome to Inventory Management System\t\t Date: {str(date_)}  TIME: {str(time_)}")
                        self.lbl_clock.after(200,self.update_content) #) for updating current time in every 200ms




                except Exception as ex:
                        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent = self.root)


        def logout(self):
                self.root.destroy()
                os.system("Python login.py")


        def button_hover(self,ev):
                self.btn_logout["bg"] = "#F4760B"

        def button_hover_leave(self,ev):
                self.btn_logout["bg"] = "Yellow"




       







        



if __name__=="__main__":
        root=Tk()
        obj=IMS(root)
        root.mainloop()
               
