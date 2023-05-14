from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import mysql.connector
class categoryClass:
        def __init__(self,root):
                self.root = root
                self.root.geometry("1100x500+220+130")
                self.root.title("Inventory management System")
                self.root.configure(bg = "#FBE5E5")
                self.root.iconbitmap(r"C:\Users\Hp\Desktop\CLass Practice\Tkinter Project\images\category_icon.ico")
                self.root.focus_force()         #) to enable another page in highlight mode.

                #============ Variables===========================
                self.var_cat_id = StringVar()
                self.var_name = StringVar()

                #=========Title===========================================================================
                lbl_title = Label(self.root,text="Manage Product Category",  font=("Gabriola",22,"bold"), bg="#F94892", fg="White",bd=3, relief=RIDGE).pack(side=TOP, fill=X,padx=10,pady=20)

                lbl_name = Label(self.root,text="Enter Category Name:", font=("Gabriola",22,"bold"), bg="#FBE5E5",fg="white").place(x=50,y=100)
                txt_name = Entry(self.root,textvariable=self.var_name, font=("Gabriola",22,"bold"), bg="#F0ECE2").place(x=50,y=170,width=300,height=30)

                #=================== BUtton==================
                #1)
                icon1 = Image.open(r"C:\Users\Hp\Desktop\CLass Practice\Tkinter Project\images\save.jpg")
                photo1 = icon1.resize((20,20))
                self.icon1_side = ImageTk.PhotoImage(photo1)

                #3)
                icon3 = Image.open(r"C:\Users\Hp\Desktop\CLass Practice\Tkinter Project\images\delete.png")
                photo3 = icon3.resize((20,20))
                self.icon3_side = ImageTk.PhotoImage(photo3)




                

                btn_add = Button(self.root,text=" ADD ",image=self.icon1_side,compound=LEFT,padx=6,anchor='w', font=("Gabriola",22,"bold"), bg="#457963", fg="white", cursor="hand2",command=self.add).place(x=360,y=170,width=150,height=30)
                btn_delete = Button(self.root,text=" DELETE ",image=self.icon3_side,compound=LEFT,padx=6,anchor='w', font=("Gabriola",22,"bold"), bg="#FD3638", fg="white", cursor="hand2",command=self.delete).place(x=520,y=170,width=150,height=30)






                 #--------------Category Details----------------------

                cat_frame = Frame(self.root,bd=3,relief=RIDGE)
                cat_frame.place(x=50,y=220,width=380,height=200)

                scrolly = Scrollbar(cat_frame,orient=VERTICAL)
                scrollx = Scrollbar(cat_frame,orient=HORIZONTAL)

                self.category_table = ttk.Treeview(cat_frame,columns=("cid","name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.config(command=self.category_table.xview)
                scrolly.config(command=self.category_table.yview)
                


                self.category_table.heading("cid",text="Category Id")
                self.category_table.heading("name",text="NAME")
               
                self.category_table["show"] = "headings"
                
                self.category_table.column("cid",width=90)
                self.category_table.column("name",width=100)


               
               
                self.category_table.pack(fill=BOTH,expand=1)
                self.category_table.bind("<ButtonRelease-1>",self.get_data)


                #+====================== Animate =============================================================
                self.im1 = Image.open(r"C:\Users\Hp\Desktop\Tkinter Project_Draft\images\perfume.jpg")
                self.im1 = self.im1.resize((279,220),Image.ANTIALIAS)
                self.im1 = ImageTk.PhotoImage(self.im1)


                
                self.im2 = Image.open(r"C:\Users\Hp\Desktop\Tkinter Project_Draft\images\mobile.jpg")
                self.im2 = self.im2.resize((279,220),Image.ANTIALIAS)
                self.im2 = ImageTk.PhotoImage(self.im2)


                
                self.im3 = Image.open(r"C:\Users\Hp\Desktop\Tkinter Project_Draft\images\shoes.jpg")
                self.im3 = self.im3.resize((279,220),Image.ANTIALIAS)
                self.im3 = ImageTk.PhotoImage(self.im3)



                self.lbl_change_image = Label(self.root,bg="grey")
                self.lbl_change_image.place(x=740,y=99,width=279,height=220)

                



                #================= Images===========================

                icon = Image.open(r"C:\Users\Hp\Desktop\CLass Practice\Tkinter Project\images\Login-1.jpg")
                photo = icon.resize((325,410))
                self.phone_image = ImageTk.PhotoImage(photo)

                self.lbl_phone_image = Label(self.root,image=self.phone_image,bd=0)
                self.lbl_phone_image.place(x=715,y=82)

                '''
                self.im2 = Image.open("E:\Paul self practice\Tkinter Project\images\cat_images.jpg")
                self.im2 = self.im2.resize((400,170), Image.ANTIALIAS)
                self.im2 = ImageTk.PhotoImage(self.im2)

                self.lbl_im2 = Label(self.root, image=self.im2, bd=2, relief=RAISED)
                self.lbl_im2.place(x=680,y=310)
                '''
                self.show() #_) whenever we run the file, it will diplay the value.
                self.animate()
                
#================================== FUNCTIONS =====================================================
        #) For addind data in a treeview
        def add(self):
                mydb = mysql.connector.connect(host="localhost", user="root",password="oramca",database="mydatabase")
                mycursor = mydb.cursor()
                try:
                        if self.var_name.get()=="":
                                messagebox.showerror("Error","Category Name Should be required",parent=self.root)
                        else:
                                mycursor.execute("select * from category where name = %s " , (self.var_name.get(),)) 
                                row  = mycursor.fetchone()
                                if row!= None: #-----True/False.
                                        messagebox.showerror("Error!","This Category already present, Try different ID",parent = self.root)
                                else:
                                        mycursor.execute("Insert Into category (name) values(%s)",(
                                                                self.var_name.get(),
                                                               
                                        )) 
                                                               
                                                                
                                        mydb.commit()
                                        messagebox.showinfo("Sucess","Category Added Successfully",parent=self.root) 
                                        self.show()        

                except Exception as ex:
                        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent = self.root)  


        #) For displaying data in Treeview
        def show(self):
                 mydb = mysql.connector.connect(host="localhost", user="root",password="oramca",database="mydatabase")
                 mycursor = mydb.cursor()
                 try:
                        mycursor.execute("select * from category") 
                        rows=mycursor.fetchall()
                        self.category_table.delete(*self.category_table.get_children())
                        for row in rows:
                                self.category_table.insert('',END,values=row)    
                 except Exception as ex:
                        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent = self.root) 




        def get_data(self,ev):
                f = self.category_table.focus()
                content = (self.category_table.item(f))  #passing in form of tuple
                row  = content['values']
                #print(row)
                self.var_cat_id.set(row[0])             # these cat_id are autoincremented values.
                self.var_name.set(row[1])




        def delete(self):
                 mydb = mysql.connector.connect(host="localhost", user="root",password="oramca",database="mydatabase")
                 mycursor = mydb.cursor()
                 try:
                      if self.var_cat_id.get()=="":
                                messagebox.showerror("Error","Please select category from the list",parent=self.root)
                      else:
                                mycursor.execute("select * from category where cid= %s " , (self.var_cat_id.get(),)) 
                                row  = mycursor.fetchone()
                                if row== None: #-----True/False.(If i found the employee id as mentioned then only i will Delete.)
                                        messagebox.showerror("Error!","Please try again",parent = self.root) 
                                else:
                                        op = messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)  #message box for asking whther user really wanted to delte.
                                        if op == True:
                                                mycursor.execute("delete from category where cid=%s",(self.var_cat_id.get(),))
                                                mydb.commit()  
                                                messagebox.showinfo("Delete","Category Deleted Successfully",parent = self.root)
                                                self.show()
                                                self.var_cat_id.set("")
                                                self.var_name.set("")

                 except Exception as ex:
                        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent = self.root)




        def animate(self):
                self.im = self.im1
                self.im1 = self.im2
                self.im2 = self.im3
                self.im3 = self.im
                self.lbl_change_image.config(image=self.im)
                self.lbl_change_image.after(2000,self.animate)






                
                
                


if __name__=="__main__":
        root=Tk()
        obj=categoryClass(root)
        root.mainloop()
               
