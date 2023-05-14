from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import mysql.connector
class productClass:
        def __init__(self,root):
                self.root = root
                self.root.geometry("1100x500+220+130")
                self.root.title("Inventory management System")
                self.root.configure(bg = "#004643")
                self.root.focus_force()         #) to enable another page in highlight mode.

                #-------Variables-------------------------
                self.var_cat = StringVar()
                self.var_sup = StringVar()

                self.var_pid = StringVar()
                self.cat_list =  []             #)  variable for combo box value category
                self.sup_list =  []             #)  variable for combo box value supplier
                self.fetch_cat_sup()
                self.var_name = StringVar()
                self.var_price = StringVar()
                self.var_qty = StringVar()
                self.var_status = StringVar()

                self.var_searchby  = StringVar()
                self.var_searchtxt  = StringVar()




                #===========Frame============
                product_frame = Frame(self.root,bd=3,relief=RIDGE, bg='#ABD1C6')
                product_frame.place(x=10,y=10,width=450,height=480)


                #------------------------Title======================

                title = Label(product_frame,text=" Manage Product Details", font=("Gabriola",18,"bold"),bg="#3C6255",fg="#EAE7B1").pack(side=TOP,fill=X)

                #================ Labels/ column 1/ =============================================================
                lbl_category = Label(product_frame,text="Category", font=("Gabriola",22,"bold"),bg="#ABD1C6").place(x=30,y=55)
                lbl_supplier = Label(product_frame,text="Supplier", font=("Gabriola",22,"bold"),bg="#ABD1C6").place(x=30,y=110)
                lbl_product_name = Label(product_frame,text="Product name", font=("Gabriola",22,"bold"),bg="#ABD1C6").place(x=30,y=160)
                lbl_price = Label(product_frame,text="Price", font=("Gabriola",22,"bold"),bg="#ABD1C6").place(x=30,y=210)
                lbl_quantity = Label(product_frame,text="Quantity", font=("Gabriola",22,"bold"),bg="#ABD1C6").place(x=30,y=260)
                lbl_status = Label(product_frame,text="Status", font=("Gabriola",22,"bold"),bg="#ABD1C6").place(x=30,y=310)

                #=================== Entry/Text fields/column 2 ==================================================================
                                                                        #)before the value="select"
                cmb_cat = ttk.Combobox(product_frame,textvariable = self.var_cat,values=self.cat_list,state="readonly",justify=CENTER,font=("Georgia",15))
                cmb_cat.place(x=150,y=65,width=200)
                cmb_cat.current(0)

                                                                #) before the value was values="select"
                cmb_sup = ttk.Combobox(product_frame,textvariable = self.var_sup,values=self.sup_list,state="readonly",justify=CENTER,font=("Georgia",15))
                cmb_sup.place(x=150,y=110,width=200)
                cmb_sup.current(0)

                txt_name = Entry(product_frame,textvariable = self.var_name, font=("Georgia",18),bg="#00ECBC").place(x=190,y=160,width=200)
                txt_price = Entry(product_frame,textvariable = self.var_price, font=("Georgia",18),bg="#00ECBC").place(x=150,y=210,width=200)
                txt_qty = Entry(product_frame,textvariable = self.var_qty, font=("Georgia",18),bg="#00ECBC").place(x=150,y=260,width=200)

                cmb_status = ttk.Combobox(product_frame,textvariable = self.var_status,values=("Available","Unavailable"),state="readonly",justify=CENTER,font=("Georgia",15))
                cmb_status.place(x=150,y=310,width=200)
                cmb_status.current(0)



                
                #-------------Button--------------------------
                #1)
                icon1 = Image.open(r"C:\Users\Hp\Desktop\CLass Practice\Tkinter Project\images\save.jpg")
                photo1 = icon1.resize((20,20))
                self.icon1_side = ImageTk.PhotoImage(photo1)

                #2)
                icon2 = Image.open(r"C:\Users\Hp\Desktop\CLass Practice\Tkinter Project\images\update2.png")
                photo2 = icon2.resize((16,16))
                self.icon2_side = ImageTk.PhotoImage(photo2)

                #3)
                icon3 = Image.open(r"C:\Users\Hp\Desktop\CLass Practice\Tkinter Project\images\delete.png")
                photo3 = icon3.resize((20,20))
                self.icon3_side = ImageTk.PhotoImage(photo3)

                #4)
                icon4 = Image.open(r"C:\Users\Hp\Desktop\CLass Practice\Tkinter Project\images\clear.png")
                photo4 = icon4.resize((20,20))
                self.icon4_side = ImageTk.PhotoImage(photo4)







                

                btn_add = Button(product_frame,text="SAVE",font=("Gabriola",18,"bold"),image=self.icon1_side,compound=LEFT,padx=5,anchor='w',bg="#4B749F",fg="white",cursor="hand2",command=self.add).place(x=10,y=400, width=100,height=40)
                btn_update = Button(product_frame,text="UPDATE",font=("Gabriola",18,"bold"),image=self.icon2_side,compound=LEFT,padx=1,anchor='w',bg="#8546F0",fg="white",cursor="hand2",command=self.update).place(x=120,y=400, width=100,height=40)
                btn_delete = Button(product_frame,text="DELETE",font=("Gabriola",18,"bold"),image=self.icon3_side,compound=LEFT,padx=2,anchor='w',bg="#D9376E",fg="white",cursor="hand2",command=self.delete).place(x=230,y=400, width=100,height=40)
                btn_clear = Button(product_frame,text="CLEAR",font=("Gabriola",18,"bold"),image=self.icon4_side,compound=LEFT,padx=5,anchor='w',bg="#001858",fg="white",cursor="hand2",command=self.clear).place(x=340,y=400, width=100,height=40)






                #------------Search Frame----------------
                 #1)
                img_srch = Image.open(r"C:\Users\Hp\Desktop\CLass Practice\Tkinter Project\images\search.png")
                img_srch = img_srch.resize((20,20))
                self.img_srch = ImageTk.PhotoImage(img_srch)




                
                SearchFrame = LabelFrame(self.root,text="Search Employee" , bg="#ABD1C6",font=("Georgia",12,"bold"),bd=2,relief=RIDGE)
                SearchFrame.place(x=480,y=10,width=610,height=80)

                #---------------------Options=================
                cmb_search = ttk.Combobox(SearchFrame,textvariable = self.var_searchby,values=("Select","category","supplier","name"),state="readonly",justify=CENTER,font=("Georgia",15))
                cmb_search.place(x=10,y=10,width=180)
                cmb_search.current(0)

                txt_search = Entry(SearchFrame,textvariable=self.var_searchtxt,font=("Georgia",15),bg="#00ECBC").place(x=200,y=10)

                btn_search = Button(SearchFrame,text="Search",image=self.img_srch,compound=LEFT,padx=12,anchor='w',font=("Georgia",15),bg="#259F6C",fg="#2D033B",cursor="hand2",command=self.search).place(x=450,y=9, width=150,height=30)






                 #--------------Product Details----------------------

                p_frame = Frame(self.root,bd=3,relief=RIDGE)
                p_frame.place(x=480,y=100,width=600,height=390)

                scrolly = Scrollbar(p_frame,orient=VERTICAL)
                scrollx = Scrollbar(p_frame,orient=HORIZONTAL)

                self.product_table = ttk.Treeview(p_frame,columns=("pid","category","supplier","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.config(command=self.product_table.xview)
                scrolly.config(command=self.product_table.yview)
                


                self.product_table.heading("pid",text="PRODUCT ID")
                self.product_table.heading("category",text="CATEGORY")
                self.product_table.heading("supplier",text="SUPPLIER")
                self.product_table.heading("name",text="NAME")
                self.product_table.heading("price",text="PRICE")
                self.product_table.heading("qty",text="QUANTITY")
                self.product_table.heading("status",text="STATUS")
               
               
                self.product_table["show"] = "headings"

                self.product_table.column("pid",width=90)
                self.product_table.column("category",width=100)
                self.product_table.column("supplier",width=100)
                self.product_table.column("name",width=100)
                self.product_table.column("price",width=100)
                self.product_table.column("qty",width=100)
                self.product_table.column("status",width=100)
                 
                self.product_table.pack(fill=BOTH,expand=1)
                self.product_table.bind("<ButtonRelease-1>",self.get_data)


                self.show()
                

#======================================================================================================================================


        #) function for fetching supplier and category details.
        def fetch_cat_sup(self):
                self.cat_list.append("Empty")   #) if there is no category it will display "Empty"
                self.sup_list.append("Empty")   #) if there is no supplier it will display "Empty"   
                mydb = mysql.connector.connect(host="localhost", user="root",password="oramca",database="mydatabase")
                mycursor = mydb.cursor()
                try:
                    mycursor.execute("select name  from category") 
                    cat = mycursor.fetchall()
                    

                    if len(cat)>0:
                        del self.cat_list[:]
                        self.cat_list.append("select")
                        for i in cat:
                         self.cat_list.append(i[0])
                  
                    mycursor.execute("select name  from supplier") 
                    sup = mycursor.fetchall()

                    if len(sup)>0:
                        del self.sup_list[:]
                        self.sup_list.append("select")
                        for i in sup:
                         self.sup_list.append(i[0])
                    
                   

                except Exception as ex:
                        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent = self.root)      
                        





                 # function for saving/adding the data into database.        
        def add(self):
                mydb = mysql.connector.connect(host="localhost", user="root",password="oramca",database="mydatabase")
                mycursor = mydb.cursor()
                try:
                        if self.var_cat.get()=="select" or self.var_cat.get()=="Empty" or self.var_sup.get()=="select" or self.var_name.get()=="":
                                messagebox.showerror("Error","All fields are required",parent=self.root)
                        else:
                                mycursor.execute("select * from product where name = %s " , (self.var_name.get(),)) #) giving product name
                                row  = mycursor.fetchone()
                                if row!= None: #-----True/False.
                                        messagebox.showerror("Error!","Product already present, Try different",parent = self.root)
                                else:
                                        mycursor.execute("Insert Into product (category,supplier,name,price,qty,status) values(%s,%s,%s,%s,%s,%s)",(
                                                                
                                                                self.var_cat.get(),
                                                                self.var_sup.get(),
                                                                self.var_name.get(),
                                                                self.var_price.get(),
                                                                self.var_qty.get(),
                                                                self.var_status.get(),
                                                               
                                        )) 
                                        mydb.commit()
                                        messagebox.showinfo("Sucess","Product Added Successfully",parent=self.root) 
                                        self.show()        
                except Exception as ex:
                        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent = self.root)      
                        
                   
        # function for displaying data in the tree view after submitting the data succesfully.
        def show(self):
                 mydb = mysql.connector.connect(host="localhost", user="root",password="oramca",database="mydatabase")
                 mycursor = mydb.cursor()
                 try:
                        mycursor.execute("select * from product") 
                        rows=mycursor.fetchall()
                        self.product_table.delete(*self.product_table.get_children())
                        for row in rows:
                                self.product_table.insert('',END,values=row)    
                 except Exception as ex:
                        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent = self.root)    




        # on clicking the data on treeview the data will be displayed on the respected cell.
        def get_data(self,ev):
                f = self.product_table.focus()
                content = (self.product_table.item(f))  #passing in form of tuple
                row  = content['values']
                self.var_pid.set(row[0]),
                self.var_cat.set(row[1]),
                self.var_sup.set(row[2]),
                self.var_name.set(row[3]),
                self.var_price.set(row[4]),
                self.var_qty.set(row[5]),
                self.var_status.set(row[6]),
                                                               
               



        # Function for updating values.
        def update(self):
                mydb = mysql.connector.connect(host="localhost", user="root",password="oramca",database="mydatabase")
                mycursor = mydb.cursor()
                try:
                        if self.var_pid.get()=="":      #) fetches the pid from database which is autoincremented
                                messagebox.showerror("Error","Please select product from list",parent=self.root)
                        else:
                                mycursor.execute("select * from product where pid= %s " , (self.var_pid.get(),)) 
                                row  = mycursor.fetchone()
                                if row== None: #-----True/False.(If i found the employee id as mentioned then only i will update.)
                                        messagebox.showerror("Error!","Invalid product",parent = self.root)
                                else:
                                        mycursor.execute("update product set category= %s,supplier= %s,name= %s,price= %s,qty= %s,status= %s where pid = %s",(
                                                                self.var_cat.get(),
                                                                self.var_sup.get(),
                                                                self.var_name.get(),
                                                                self.var_price.get(),
                                                                self.var_qty.get(),
                                                                self.var_status.get(),
                                                                self.var_pid.get()
                                        )) 
                                        mydb.commit()
                                        messagebox.showinfo("Sucess","Product Updated Successfully",parent=self.root) 
                                        self.show()        
                except Exception as ex:
                        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent = self.root)    
               
                        



        def delete(self):
                 mydb = mysql.connector.connect(host="localhost", user="root",password="oramca",database="mydatabase")
                 mycursor = mydb.cursor()
                 try:
                      if self.var_pid.get()=="":
                                messagebox.showerror("Error","Select product from the list",parent=self.root)
                      else:
                                mycursor.execute("select * from product where pid= %s " , (self.var_pid.get(),)) 
                                row  = mycursor.fetchone()
                                if row== None: #-----True/False.(If i found the employee id as mentioned then only i will update.)
                                        messagebox.showerror("Error!","Invalid Product",parent = self.root) 
                                else:
                                        op = messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)  #message box for asking whther user really wanted to delte.
                                        if op == True:
                                                mycursor.execute("delete from product where pid=%s",(self.var_pid.get(),))
                                                mydb.commit()  
                                                messagebox.showinfo("Delete","Product Deleted Successfully",parent = self.root)
                                                self.clear()

                 except Exception as ex:
                        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent = self.root) 



        def clear(self):
                self.var_cat.set("Select"),
                self.var_sup.set("Select"),
                self.var_name.set(""),
                self.var_price.set(""),
                self.var_qty.set(""),
                self.var_status.set("Available"),
                self.var_pid.set("")
                
                self.var_searchtxt.set("")
                self.var_searchby.set("Select")
                self.show()


        #) for searching data from the inventory.(Product table)
        def search(self):
                 mydb = mysql.connector.connect(host="localhost", user="root",password="oramca",database="mydatabase")
                 mycursor = mydb.cursor()
                 try:
                        if self.var_searchby.get()=="Select":
                                messagebox.showerror("Error","Select search by option",parent=self.root)
                        elif self.var_searchtxt.get()=="":
                                messagebox.showerror("Error","Search area should be required",parent=self.root)
                        else:
                                mycursor.execute("select * from product WHERE " +self.var_searchby.get()+ " LIKE '%"+self.var_searchtxt.get()+"%'") 
                                rows=mycursor.fetchall()
                                if len(rows)!=0:
                                        self.product_table.delete(*self.product_table.get_children())
                                        for row in rows:
                                                self.product_table.insert('',END,values=row)  
                                else:
                                        messagebox.showerror("Error","No record found..",parent=self.root)  
                 except Exception as ex:
                        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent = self.root)   




if __name__=="__main__":
        root=Tk()
        obj=productClass(root)
        root.mainloop()                
