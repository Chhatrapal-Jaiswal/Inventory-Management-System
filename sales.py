from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import mysql.connector
import os
class salesClass:
        def __init__(self,root):
                self.root = root
                self.root.geometry("1100x500+220+130")
                self.root.title("Inventory management System")
                self.root.configure(bg = "#1E5287")
                self.root.focus_force()         #) to enable another page in highlight mode.

                 #============ Variables===========================
                self.var_invoice = StringVar()
                self.var_name = StringVar()
                self.bill_list = []


                #======== Title ==========================

                lbl_title = Label(self.root,text="View Customer Bill", font=("Georgia",30), bg="#36C186", fg="#D0F66A",bd=3, relief=SUNKEN).pack(side=TOP, fill=X,padx=10,pady=20)

                lbl_invoice = Label(self.root,text="Invoice No:",font=("Georgia",15), bg="#1E5287", fg='#D0F66A' ).place(x=50,y=100)

                txt_invoice = Entry(self.root,textvariable=self.var_invoice,font=("Georgia",15), bg="#7B99FA" ).place(x=160,y=100,width=180,height=28)

                #========================Button==================================
                 #1)
                img_srch = Image.open(r"C:\Users\Hp\Desktop\CLass Practice\Tkinter Project\images\search.png")
                img_srch = img_srch.resize((20,20))
                self.img_srch = ImageTk.PhotoImage(img_srch)

                #4)
                icon4 = Image.open(r"C:\Users\Hp\Desktop\CLass Practice\Tkinter Project\images\clear.png")
                photo4 = icon4.resize((20,20))
                self.icon4_side = ImageTk.PhotoImage(photo4)









                
                btn_search = Button(self.root,text="Search",image=self.img_srch,compound=LEFT,padx=12,anchor='w',font=("Gabriola",15,"bold"),bg="#FF0075", fg="white",command=self.search).place(x=360,y=100,width=120,height=28)

                btn_clear = Button(self.root,text="Clear",image=self.icon4_side,compound=LEFT,padx=5,anchor='w',font=("Gabriola",15,"bold"),bg="#A34A28", fg="white",cursor="hand2",command=self.clear).place(x=490,y=100,width=120,height=28)


                #===================================== Bill List =============================================

                #) frame for viewing no. of sales through bill.
                sales_frame = Frame(self.root,bd=3,relief=RIDGE)
                sales_frame.place(x=50,y=140,width=200,height=330)


                scrolly = Scrollbar(sales_frame,orient=VERTICAL)
                self.sales_list = Listbox(sales_frame,font=("Georgia",15),bg="#D0F66A",yscrollcommand=scrolly.set) #creating listbox for storing sales data.

                scrolly.pack(side=RIGHT,fill=Y)
                scrolly.config(command=self.sales_list.yview) #) placing scroll bar on listbox

                self.sales_list.pack(fill=BOTH,expand=1)

                self.sales_list.bind("<ButtonRelease-1>",self.get_data)


                #===================================== Bill Area =============================================
                bill_frame = Frame(self.root,bd=3,relief=RIDGE)
                bill_frame.place(x=280,y=140,width=410,height=330)


                lbl_title2 = Label(bill_frame,text="Customer Bill Area",  font=("Gabriola",20), bg="#D0F66A", fg="Black").pack(side=TOP, fill=X)

                scrolly2 = Scrollbar(bill_frame,orient=VERTICAL)

                self.bill_area = Text(bill_frame,bg="Light yellow",yscrollcommand=scrolly2.set)

                scrolly2.pack(side=RIGHT,fill=Y)
                scrolly2.config(command=self.bill_area.yview)
                
                self.bill_area.pack(fill=BOTH,expand=1)


                #========================= Image ==============================================

                 #========================= Image ==============================================

                self.bill_photo = Image.open(r"C:\Users\Hp\Desktop\CLass Practice\Tkinter Project\images\save_2.png")
                self.bill_photo = self.bill_photo.resize((360,320))
                self.bill_photo = ImageTk.PhotoImage(self.bill_photo)

                lbl_image = Label(self.root, image=self.bill_photo, bd=0)
                lbl_image.place(x=700,y=140)

                self.show() #) this functn should run on opening of the page





                
                #-======================================================================================
        #) A function for displaying the files i the listbox.(left section)
        def show(self):
                del self.bill_list[:] #) created a list which will hold the sales details bills
                self.sales_list.delete(0,END)  #) refreshing the listbox to view new entered twxt files.
               # print(os.listdir('Bill'))
                for i in os.listdir('Bill'):   #) Bill folder
                       #print(i.split('.'),i.split('.')[-1])
                       if i.split('.')[-1] == 'txt':
                        self.sales_list.insert(END,i)   #) name of files is i
                        self.bill_list.append(i.split('.')[0])

        #) a function for siplaying the selected file contenet into the text box created.(Middle section)
        def get_data(self,ev):
                index_ = self.sales_list.curselection()
                file_name = self.sales_list.get(index_)
                print(file_name)
                self.bill_area.delete('1.0',END)
                fp = open(f'Bill/{file_name}','r')
                for i in fp:
                        self.bill_area.insert(END,i)
                fp.close()



        def search(self):
                if self.var_invoice.get() == "":
                        messagebox.showerror("Error" , "Invoice No. Should be required",parent = self.root)
                else:
                        if self.var_invoice.get() in self.bill_list:
                                fp = open(f'Bill/{self.var_invoice.get()}.txt','r')
                                self.bill_area.delete('1.0',END)
                                for i in fp:
                                        self.bill_area.insert(END,i)
                                fp.close()
                        else:
                                messagebox.showerror("Error" , "Invoice No. is invalid",parent = self.root)


        def clear(self):
                self.show()
                self.bill_area.delete('1.0',END)
                self.var_invoice.set("")













if __name__=="__main__":
        root=Tk()
        obj=salesClass(root)
        root.mainloop()                
