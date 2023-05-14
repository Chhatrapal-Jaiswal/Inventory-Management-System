from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import os
class Login_system:
    def __init__(self,root):
         self.root = root
         self.root.geometry("1350x700+0+0")
         self.root.title("Login  System")
         self.root.configure(bg = "white")

           #-------------------Image--------------------
        
         icon = Image.open("E:\Paul self practice\Tkinter Project\images\Login-1.jpg")
         photo = icon.resize((400,600))
         self.phone_image = ImageTk.PhotoImage(photo)

         self.lbl_phone_image = Label(self.root,image=self.phone_image,bd=0)
         self.lbl_phone_image.place(x=180,y=90)

        #========= Login Frame ===============================
         self.username = StringVar()
         self.password = StringVar()


         login_frame = Frame(self.root,bd=2,relief=RIDGE,bg="white")
         login_frame.place(x=650,y=90,width=350,height=460)

         title = Label(login_frame, text="Login System" ,font=("Georgia",30,'bold'),bg='white').place(x=0,y=30,relwidth=1)
         
         lbl_user = Label(login_frame,text="User ID:", font=("Georgia",15),bg='white',fg="Red").place(x=50,y=100)


         txt_username = Entry(login_frame,font=("Georgia",15),bg="light yellow",textvariable=self.username).place(x=50,y=140,width=250)

         lbl_pass = Label(login_frame,text="Password", font=("Georgia",15),bg='white',fg="Red").place(x=50,y=200)
         txt_pass = Entry(login_frame,font=("Georgia",15),bg="light yellow",show="*",textvariable=self.password).place(x=50,y=240,width=250)

         btn_login = Button(login_frame,text="Login",font=("Comic Sans MS",15),bg="#4b7f6e",activebackground="#4b7f6e",fg="white",cursor="hand2",command=self.login).place(x=50,y=300,width=250,height=35)

         hr = Label(login_frame,bg='light grey').place(x=50,y=370,width=250,height=2)  #horozontal line

         or_ = Label(login_frame,text="OR", font=("Georgia",15,"bold"),fg='light grey',bg="white").place(x=150,y=355) #OR word on horizontal line

         btn_login = Button(login_frame,text="Forgot Passowrd ?",font=("Comic Sans MS",15),bg="white",fg="#039a9c",cursor="hand2",bd=0,activebackground="white",activeforeground="#039a9c").place(x=80,y=390)

         #=============================== Animation Images ==========================================================
         #1)

         self.im1 = Image.open("E:\Paul self practice\Tkinter Project\images\login-cover.jpg")
         self.im1 = self.im1.resize((347,335),Image.ANTIALIAS)
         self.im1 = ImageTk.PhotoImage(self.im1)

         #self.lbl_phone1_image = Label(self.root,image=self.phone_image1,bd=0)
         #self.lbl_phone1_image.place(x=210,y=112)

          #2)
         
         self.im2 = Image.open("E:\Paul self practice\Tkinter Project\images\login-cover2.jpg")
         self.im2 = self.im2.resize((347,335),Image.ANTIALIAS)
         self.im2 = ImageTk.PhotoImage(self.im2)
         

         #self.lbl_phone2_image = Label(self.root,image=self.phone_image2,bd=0)
         #self.lbl_phone2_image.place(x=210,y=112)

          #3)
         
         self.im3 = Image.open("E:\Paul self practice\Tkinter Project\images\login-cover3.jpg")
         self.im3 = self.im3.resize((347,335),Image.ANTIALIAS)
         self.im3 = ImageTk.PhotoImage(self.im3)

         #self.lbl_phone3_image = Label(self.root,image=self.phone_image3,bd=0)
         #self.lbl_phone3_image.place(x=210,y=112)

         self.lbl_change_image = Label(self.root,bg="grey")
         self.lbl_change_image.place(x=210,y=112,width=347,height=335)

         self.animate()



#=================================================================================================================================================================================================================================
    def login(self):
         mydb = mysql.connector.connect(host="localhost", user="root",password="oramca",database="mydatabase")
         mycursor = mydb.cursor()
         try:
            if self.username.get()=="" or self.password.get()=="":
                messagebox.showerror("error","All fields are required",parent=self.root)
            else:

             mycursor.execute('select utype from employee where eid=%s AND pass=%s',(self.username.get(),self.password.get()))
             user = mycursor.fetchone()
             if user == None:
                messagebox.showerror("Error","Invalid Username/Password ",parent=self.root)
             else:
                if user[0] =="Admin":
                    self.root.destroy()
                    os.system("Python IMS.py")
                else:
                    self.root.destroy()
                    os.system("Python billing.py")

         except Exception as ex:
                        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent = self.root)



    def animate(self):
        self.im = self.im1
        self.im1 = self.im2
        self.im2 = self.im3
        self.im3 = self.im
        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(2000,self.animate)


    








        

      
        
       
        

root = Tk()
obj=Login_system(root)
root.mainloop()