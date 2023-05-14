from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import mysql.connector
import time
import os
import tempfile
class billClass:
        def __init__(self,root):
                self.root = root
                self.root.geometry("1350x700+0+0")
                self.root.title("Inventory management System")
                self.root.configure(bg = "white")
                self.cart_list=[] #) used to update cart treeview
                self.chk_print = 0

                #-------------------Title_--------------------
                icon = Image.open("E:\Paul self practice\Tkinter Project\images\logo.png")
                photo = icon.resize((80,80))
                self.icon_title = ImageTk.PhotoImage(photo)
                title = Label(self.root, text="Inventory Management System",image=self.icon_title,compound = LEFT,font=("Gabriola",40,"bold"),bg="#2A363B" , fg="white",anchor="w",padx=20)
                title.place(x=0,y=0,relwidth=1,height=70)


                #-------------Button Logout--------------


                btn_logout = Button(root, text="Logout",font=("Times New Roman",30,"bold"), bg="Yellow",cursor="hand2",command=self.logout)
                btn_logout.place(x=1150,y=10,height=50,width=160)


                #---------------------------------Clock-----------------------


                self.lbl_clock = Label(root, text="Welcome to Inventory Management System\t\t Date: DD-MM-YYY\t\t  TIME: HH:MM:SS" ,font=("Gabriola",15,"bold"), bg="#E84A5F" , fg="white")
                self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

                #==================== Product Frame ===========================================
                


                ProductFrame1 = Frame(self.root,bd=4,relief=RIDGE,bg="white")
                ProductFrame1.place(x=6,y=110,width=410,height=550)

                pTitle = Label(ProductFrame1,text="All Products",font=("Georgia",20,"bold"),bg="Black" , fg="white").pack(side=TOP,fill=X)

                lbl_note = Label(ProductFrame1,text="Note: 'Enter 0(Zero) QTY to remove the product from cart ' ",font=("Georgia",10),bg="white",fg="#802105",anchor="w").pack(side=BOTTOM,fill=X)


                #================= Product Search Frame =================================================
                self.var_search = StringVar()

                ProductFrame2 = Frame(ProductFrame1,bd=4,relief=RIDGE,bg="white")
                ProductFrame2.place(x=2,y=42,width=398,height=90)

                lbl_search = Label(ProductFrame2,text="Search Products by name",font=("Times New Roman",15,"bold"),bg="White", fg="green").place(x=2,y=5)

                lbl_search = Label(ProductFrame2,text="Product Name",font=("Times New Roman",15,"bold"),bg="White", fg="Black").place(x=2,y=45)
                txt_search = Entry(ProductFrame2,textvariable=self.var_search,font=("Times New Roman",15),bg="Light yellow").place(x=129,y=47,width=150,height=22)
                btn_search = Button(ProductFrame2,text="Search",font=("Georgia",15,"bold"),bg="#6ae0eb",fg="white",cursor="hand2",command=self.search).place(x=284,y=45,width=100,height=25)
                btn_show_all = Button(ProductFrame2,text="Show all",font=("Georgia",15,"bold"),bg="#2b970e",fg="white",cursor="hand2",command=self.show).place(x=284,y=10,width=100,height=25)



                 #--------------Product Details Frame ----------------------

                ProductFrame3 = Frame(ProductFrame1,bd=3,relief=RIDGE)
                ProductFrame3.place(x=2,y=140,width=395,height=375)

                scrolly = Scrollbar(ProductFrame3,orient=VERTICAL)
                scrollx = Scrollbar(ProductFrame3,orient=HORIZONTAL)

                self.product_Table = ttk.Treeview(ProductFrame3,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.config(command=self.product_Table.xview)
                scrolly.config(command=self.product_Table.yview)
                


                self.product_Table.heading("pid",text="PID")
                self.product_Table.heading("name",text="NAME")
                self.product_Table.heading("price",text="PRICE")
                self.product_Table.heading("qty",text="QTY")
                self.product_Table.heading("status",text="STATUS")
                

                self.product_Table["show"] = "headings"

                self.product_Table.column("pid",width=40)
                self.product_Table.column("name",width=100)
                self.product_Table.column("price",width=100)
                self.product_Table.column("qty",width=40)
                self.product_Table.column("status",width=90)
               
                self.product_Table.pack(fill=BOTH,expand=1)
                self.product_Table.bind("<ButtonRelease-1>",self.get_data)



               #===================================== Customer Frame =================================================

                self.var_cname = StringVar()
                self.var_contact = StringVar()

                CustomerFrame = Frame(self.root,bd=4,relief=RIDGE,bg="white")
                CustomerFrame.place(x=420,y=110,width=530,height=70)

                cTitle = Label(CustomerFrame,text="Customer Details",font=("Georgia",15),bg="#96989c").pack(side=TOP,fill=X)
                lbl_name = Label(CustomerFrame,text="Name",font=("Times New Roman",15),bg="White", fg="Black").place(x=5,y=35)
                txt_name = Entry(CustomerFrame,textvariable=self.var_cname,font=("Times New Roman",13),bg="Light yellow").place(x=80,y=35,width=180,height=22)

                lbl_contact = Label(CustomerFrame,text="Contact No.",font=("Times New Roman",15),bg="White", fg="Black").place(x=270,y=35)
                txt_contact = Entry(CustomerFrame,textvariable=self.var_contact,font=("Times New Roman",13),bg="Light yellow").place(x=380,y=35,width=140)

                #================= Calculator and Cart Frame =================================

                self.Cal_cart_Frame = Frame(self.root,bd=2,relief=RIDGE,bg="white")
                self.Cal_cart_Frame.place(x=420,y=190,width=530,height=360)


                self.Cal_cart_Frame = Frame(self.root,bd=2,relief=RIDGE,bg="white")
                self.Cal_cart_Frame.place(x=420,y=190,width=530,height=360)

                icon = Image.open(r"C:\Users\Hp\Desktop\CLass Practice\Tkinter Project\images\cal_cart_img.jpg")
                photo = icon.resize((280,300))
                self.phone_image = ImageTk.PhotoImage(photo)

                self.lbl_phone_image = Label(self.Cal_cart_Frame,image=self.phone_image,bd=0)
                self.lbl_phone_image.place(x=5,y=47)

 




                # ===================== Cart Frame =======================================================
                self.cart_Frame = Frame(self.Cal_cart_Frame,bd=3,relief=RIDGE)
                self.cart_Frame.place(x=280,y=8,width=245,height=342)

                self.cartTitle = Label(self.cart_Frame,text="Cart Total Product :[0]",font=("Georgia",15),bg="#96989c")
                self.cartTitle.pack(side=TOP,fill=X)


                scrolly = Scrollbar(self.cart_Frame,orient=VERTICAL)
                scrollx = Scrollbar(self.cart_Frame,orient=HORIZONTAL)

                self.CartTable= ttk.Treeview(self.cart_Frame,columns=("pid","name","price","qty"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.config(command=self.CartTable.xview)
                scrolly.config(command=self.CartTable.yview)
                


                self.CartTable.heading("pid",text="PID")
                self.CartTable.heading("name",text="NAME")
                self.CartTable.heading("price",text="PRICE")
                self.CartTable.heading("qty",text="QTY")
                
                

                self.CartTable["show"] = "headings"

                self.CartTable.column("pid",width=40)
                self.CartTable.column("name",width=100)
                self.CartTable.column("price",width=90)
                self.CartTable.column("qty",width=40)
                
               
                self.CartTable.pack(fill=BOTH,expand=1)
                self.CartTable.bind("<ButtonRelease-1>",self.get_data_cart)

        
        
        #======================= ADD cart widgets Frames ===============================================

                self.var_pid = StringVar()
                self.var_pname = StringVar()
                self.var_price = StringVar()
                self.var_qty = StringVar()
                self.var_stock = StringVar()

                Add_CartWidgetsFrame = Frame(self.root,bd=3,relief=RIDGE,bg="white")
                Add_CartWidgetsFrame.place(x=420,y=550,width=530,height=110)

                lbl_p_name = Label(Add_CartWidgetsFrame,text="Product Name",font=("Times New Roman",15),bg="white").place(x=5,y=5)
                txt_p_name = Entry(Add_CartWidgetsFrame,textvariable=self.var_pname,font=("Times New Roman",15),bg="light yellow",state='readonly').place(x=5,y=35,width=190,height=22)

                lbl_p_price = Label(Add_CartWidgetsFrame,text="Price Per Qty",font=("Times New Roman",15),bg="white").place(x=230,y=5)
                txt_p_price = Entry(Add_CartWidgetsFrame,textvariable=self.var_price,font=("Times New Roman",15),bg="light yellow",state='readonly').place(x=230,y=35,width=150,height=22)

                lbl_p_qty = Label(Add_CartWidgetsFrame,text="Quantity",font=("Times New Roman",15),bg="white").place(x=390,y=5)
                txt_p_qty = Entry(Add_CartWidgetsFrame,textvariable=self.var_qty,font=("Times New Roman",15),bg="light yellow").place(x=390,y=35,width=120,height=22)

                self.lbl_inStock = Label(self.Cal_cart_Frame,text="In Stock",font=("Times New Roman",15),bg="white")
                self.lbl_inStock.place(x=5,y=5)

                btn_delete_cart = Button(Add_CartWidgetsFrame,text="Delete",font=("Times New Roman",15,"bold"),bg="#ea940f", fg="Black",cursor="hand2",command=self.delete).place(x=10,y=70,width=150,height=30)

                btn_clear_cart = Button(Add_CartWidgetsFrame,text="Clear",font=("Times New Roman",15,"bold"),bg="#ea940f", fg="Black",cursor="hand2",command=self.clear_cart).place(x=180,y=70,width=150,height=30)
                btn_add_cart = Button(Add_CartWidgetsFrame,text="Add | Update CArt",font=("Times New Roman",15,"bold"),bg="#fac947", fg="Black",cursor="hand2",command=self.add_update_cart).place(x=340,y=70,width=180,height=30)


                #========================= Billing Area =======================

                billFrame = Frame(self.root,bd=2,relief=RIDGE,bg="white")
                billFrame.place(x=953,y=110,width=410,height=410)

                bTitle = Label(billFrame,text="Customer Bill Area",font=("Georgia",15),bg="#f3184a").pack(side=TOP,fill=X)
                scrolly = Scrollbar(billFrame,orient=VERTICAL)
                scrolly.pack(side=RIGHT,fill=Y)

                self.txt_bill_area = Text(billFrame,yscrollcommand=scrolly.set)
                self.txt_bill_area.pack(fill=BOTH,expand=1)
                scrolly.config(command=self.txt_bill_area.yview)


                #==================== Billings Buttons =================================

                billMenuFrame = Frame(self.root,bd=2,relief=RIDGE,bg="white")
                billMenuFrame.place(x=953,y=520,width=410,height=140)

                self.lbl_amnt = Label(billMenuFrame,text='Bill Amnt \n[0]',font=("Georgia",15,'bold'),bg='#d300c0')
                self.lbl_amnt.place(x=2,y=5,width=120,height=70)

                self.lbl_discount = Label(billMenuFrame,text='Discount  \n[5]',font=("Georgia",15,'bold'),bg='#a902fb')
                self.lbl_discount.place(x=124,y=5,width=120,height=70)

                self.lbl_net_pay = Label(billMenuFrame,text='Net Pay \n[0]',font=("Georgia",15,'bold'),bg='#5e46fc')
                self.lbl_net_pay.place(x=246,y=5,width=160,height=70)




                btn_print = Button(billMenuFrame,text='Print',font=("Georgia",15,'bold'),bg='#d300c0',cursor='hand2',command=self.print_bill)
                btn_print.place(x=2,y=80,width=120,height=50)

                btn_clear_all = Button(billMenuFrame,text='Clear All',font=("Georgia",15,'bold'),bg='#a902fb',cursor='hand2',command=self.clear_all)
                btn_clear_all.place(x=124,y=80,width=120,height=50)

                btn_generate = Button(billMenuFrame,text='Save Bill',font=("Georgia",15,'bold'),bg='#5e46fc',cursor='hand2',command=self.generate_bill)
                btn_generate.place(x=246,y=80,width=160,height=50)



                #============================ Footer ==========================================================
                lbl_footer = Label(self.root, text="IMS-Inventory Management System | By:- Chhatrapal Jaiswal\n" ,font=("Gabriola",12), bg="#DC5A41" , fg="white")
                lbl_footer.place(x=0,y=670,height=40,width=1350)

                self.show()
                #self.bill_top()
                self.update_date_time()
        








# ============================================================================= Functions =======================================================================================================================

#) functions for calculator.

        def get_input(self,num):
                xnum = self.var_cal_input.get() + str(num)
                self.var_cal_input.set(xnum)

        def clear_cal(self):
                self.var_cal_input.set('')

        def perform_cal(self):
                result = self.var_cal_input.get()
                self.var_cal_input.set(eval(result))


 
        #) displaying all the data available from product table to product area(Product detail Frame).
        def show(self):
                 mydb = mysql.connector.connect(host="localhost", user="root",password="oramca",database="mydatabase")
                 mycursor = mydb.cursor()
                 try:

                        mycursor.execute("select pid,name,price,qty,status from product where status='Available'") 
                        rows=mycursor.fetchall()
                        self.product_Table.delete(*self.product_Table.get_children())
                        for row in rows:
                                self.product_Table.insert('',END,values=row)    
                 except Exception as ex:
                        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent = self.root) 




        #) search button on product frame, for searching available product in the list.
        def search(self):
                 mydb = mysql.connector.connect(host="localhost", user="root",password="oramca",database="mydatabase")
                 mycursor = mydb.cursor()
                 try:
                        if self.var_search.get()=="":
                                messagebox.showerror("Error","Search area should be required",parent=self.root)
                        else:
                                mycursor.execute("select pid,name,price,qty,status from product WHERE name  LIKE '%"+self.var_search.get()+"%'") 
                                rows=mycursor.fetchall()
                                if len(rows)!=0:
                                        self.product_Table.delete(*self.product_Table.get_children())
                                        for row in rows:
                                                self.product_Table.insert('',END,values=row)  
                                else:
                                        messagebox.showerror("Error","No record found..",parent=self.root)  
                 except Exception as ex:
                        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent = self.root) 


        #) thsi functn is used to get appropriate data from the table to the respected readonly textboxes.

        def get_data(self,ev):
                f = self.product_Table.focus()
                content = (self.product_Table.item(f))  #passing in form of tuple
                row  = content['values']  
                self.var_pid.set(row[0])
                self.var_pname.set(row[1])
                self.var_price.set(row[2]) 
                self.lbl_inStock.config(text=f"In Stock [{str(row[3])}]")
                #
                self.var_stock.set(row[3])
                self.var_qty.set('1')







        #) functn for getting the data from product treeview to readonly labels.
        def get_data_cart(self,ev):
                f = self.CartTable.focus()
                content = (self.CartTable.item(f))  #passing in form of tuple
                row  = content['values']  
               # pid,name,price,qty,stock
                self.var_pid.set(row[0])
                self.var_pname.set(row[1])
                self.var_price.set(row[2]) 
                self.var_qty.set(row[3])
                self.lbl_inStock.config(text=f"In Stock [{str(row[4])}]")
                self.var_stock.set(row[4])

        #) function for adding/updating the cart in the  cart_list.
        def add_update_cart(self):
                if self.var_pid.get()=='': #) if nothing entered to the cart(it is checked thrgh PID in treeview vart_list.)
                        messagebox.showerror("Error","Please select product from the list.",parent=self.root)
                elif self.var_qty.get() == "" : #) if after selecting the product, quantity is not mentioned then,
                        messagebox.showerror("Error","Quantity is required",parent=self.root)
                elif int(self.var_qty.get())>int(self.var_stock.get()):
                        messagebox.showerror("Error",f"Only {self.var_stock.get()} Quantity Available",parent=self.root)

                else:
                        #price_cal = int(self.var_qty.get())*float(self.var_price.get())  calculating price with aty in treeview cart
                        #price_cal = float(price_cal)

                        price_cal  = self.var_price.get()
                       # print(price_cal)  pid,name,price,qty,stock  (real comment)

                                                                                 #qty is user entered qty,
                        cart_data = [self.var_pid.get(),self.var_pname.get(),price_cal,self.var_qty.get(),self.var_stock.get()]
                        #print(self.cart_list) (real comment)

                        #============== Update cart ==================================
                        present = 'no'
                        index_ = 0
                        for row in self.cart_list:
                                if self.var_pid.get() == row[0]:
                                        present= 'yes'
                                        break
                                index_+=1
                        #print(present,index_)
                        if present == 'yes':
                                op = messagebox.askyesno('Confirm','Product already present\n DO you want to update/REmove?',parent=self.root)
                                if op==True:
                                        if self.var_qty.get() == '0':
                                                self.cart_list.pop(index_)

                                        else:
                                                #pid,name,price,qty,status
                                                #self.cart_list[index_][2]=price_cal #price
                                                self.cart_list[index_][3]=self.var_qty.get() #new quantity, updated quantity
                        else:
                                                 self.cart_list.append(cart_data)

                        self.show_cart()
                        self.bil_updates()


        def delete(self):
                present = 'no'
                index_ = 0
                for row in self.cart_list:
                        if self.var_pid.get() == row[0]:
                                present = 'yes'
                                break
                        index_ += 1

                if present == 'yes':
                        op = messagebox.askyesno('Confirm', 'Do you want to delete the selected product from the cart?', parent=self.root)
                        if op == True:
                                self.cart_list.pop(index_)
                                self.show_cart()
                else:
                        messagebox.showerror("Error", "Selected product is not present in the cart", parent=self.root)


        #) functn for cart total product, Bill amnt, Discount, Net Pay
        def bil_updates(self):
                self.bill_amnt = 0
                self.net_pay = 0
                self.discount=0
                for row in self.cart_list:
                        #pid,name,price,qty,stock
                        print(row)
                        self.bill_amnt=self.bill_amnt+(float(row[2]) * int(row[3])) 
                self.discount = (self.bill_amnt*5)/100
                self.net_pay=self.bill_amnt - self.discount
                self.lbl_amnt.config(text=f'Bill Amnt(Rs)\n{str(self.bill_amnt)}')
                self.lbl_net_pay.config(text=f'Net Amnt(Rs)\n{str(self.net_pay)}')
                self.cartTitle.config(text=f"Cart Total Product :[{str(len(self.cart_list))}]")

 

        

        #) this functn is to fetch the values from self.cart_list(the list created above in variables) to cart treeview
        def show_cart(self):
                
                 try:

                        #pid,name,price,qty,status
                        self.CartTable.delete(*self.CartTable.get_children())
                        for row in self.cart_list:
                                self.CartTable.insert('',END,values=row)    
                 except Exception as ex:
                        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent = self.root) 


        def generate_bill(self):
                if self.var_cname.get()=="" or self.var_contact.get()=="":
                        messagebox.showerror("Error",f"Customer name and Contact required",parent = self.root) 
                elif len(self.cart_list) == 0:
                        messagebox.showerror("Error",f"Please add product to the cart",parent = self.root)
                else:
                        #=============== Bill Top =============
                        self.bill_top()
                        #=============== Bill Middle =============
                        self.bill_middle()
                        #=============== Bill Bottom =============
                        self.bill_bottom()




                        fp = open(f'Bill/{str(self.invoice)}.txt','w')
                        fp.write(self.txt_bill_area.get('1.0',END))
                        fp.close()
                        messagebox.showinfo('Saved','Bill has been generated and saved successfully..!')


                        #=========
                        self.chk_print = 1
                       




        def bill_top(self):
                self.invoice = int(time.strftime("%H%M%S")) + int(time.strftime("%d%m%Y"))  #) time frame for unique invoice no.
                print(self.invoice)
                bill_top_temp = f'''
                
                \t\tALL-MART-Inventory
\t Phone No. 022-666333 , Delhi-125001
{str("="*47)}
 Customer Name: {self.var_cname.get()}
 Ph no. :{self.var_contact.get()}
 Bill No. {str(self.invoice)}\t\t\tDate: {str(time.strftime("%d/%m/%Y"))}
{str("="*47)}
 Product Name\t\t\tQTY\tPrice
{str("="*47)}
                '''
                self.txt_bill_area.delete('1.0',END)
                self.txt_bill_area.insert('1.0',bill_top_temp)


        def bill_bottom(self):
                bill_bottom_temp=f'''
{str("="*47)}
 Bill Amount\t\t\t\tRs.{self.bill_amnt}
 Discount\t\t\t\tRs.{self.discount}
 Net Pay\t\t\t\tRs.{self.net_pay}
{str("="*47)}\n
        '''
                self.txt_bill_area.insert(END,bill_bottom_temp)



        def bill_middle(self):
                mydb = mysql.connector.connect(host="localhost", user="root",password="oramca",database="mydatabase")
                mycursor = mydb.cursor()

                try:
                        for row in self.cart_list:
                                #pid,name,price,qty,stock
                                 
                                 pid = row[0]
                                 name=row[1]
                                 qty= int(row[4]) - int(row[3])
                                 if int(row[3]) == int(row[4]):
                                        status = 'Unavailable'

                                 if int(row[3]) != int(row[4]):
                                        status = 'Available'
                                 price=float(row[2])*int(row[3])
                                 price=str(price)
                                 self.txt_bill_area.insert(END,"\n "+name+"\t\t\t"+row[3]+"\tRs."+price)
                                 #======================= Update qty in product table ==================
                                 mycursor.execute('update product set qty= %s,status= %s where pid = %s',(
                                        qty,
                                        status,
                                        pid
                                 ))
                                 mydb.commit()
                        mydb.close()
                        self.show()
                except Exception as ex:
                        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent = self.root) 




        def clear_cart(self):
                self.var_pid.set("")
                self.var_pname.set("")
                self.var_price.set("") 
                self.var_qty.set("")
                self.lbl_inStock.config(text=f"In Stock")
                self.var_stock.set("")


        def clear_all(self):
                del self.cart_list[:]
                self.var_cname.set('')
                self.var_contact.set('')
                self.txt_bill_area.delete('1.0',END)
                self.cartTitle.config(text=f"Cart Total Product :[0]")
                self.var_search.set('')
                self.chk_print = 0
                self.clear_cart()
                self.show()
                self.show_cart()


        def update_date_time(self):
                time_ = time.strftime("%H:%M:%S")
                date_ = time.strftime("%d-%m-%Y")
                self.lbl_clock.config(text=f"Welcome to Inventory Management System\t\t Date: {str(date_)}  TIME: {str(time_)}")
                self.lbl_clock.after(200,self.update_date_time) #) for updating current time in every 200ms



        def print_bill(self):
                if self.chk_print == 1:
                        messagebox.showinfo('Print','Please wait while printing',parent=self.root)
                        new_file = tempfile.mktemp('.txt')
                        open(new_file,'w').write(self.txt_bill_area.get('1.0',END))
                        os.startfile(new_file,'print')

                else:
                        messagebox.showerror('Print','Please generate Bill to print the receipt',parent=self.root)



        def logout(self):
                self.root.destroy()
                os.system("Python login.py")
                        
        


                
   
                       




if __name__=="__main__":
        root=Tk()
        obj=billClass(root)
        root.mainloop()
               
