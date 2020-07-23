from tkinter import *
from tkinter import messagebox
from passman.login_gui import l_gui
from  passman.register import register
import bcrypt
from PIL import  Image, ImageTk
import binascii
class r_gui:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("900x600+280+50")
        self.root.title("PASSWORD MANAGER")
        self.register = register()



        self.bg = ImageTk.PhotoImage(file="images\\bin.png" )
        bg = Label(self.root,image=self.bg).place(x=-250,y=-50)

        frame =Frame(self.root,bg="white"
                                  "")
        frame.place(x=190,y=120,width = 700, height = 400)
        self.left = ImageTk.PhotoImage(file="images\\side.jpg")
        left = Label(self.root, image=self.left, bg="black").place(x=5, y=145, height=350)
        title = Label(frame, text="Join Us Today!",font=("Verdana",15,"bold"),bg="white",fg="maroon")
        title.place(x=250,y=30)

        self.first_name = Label(frame, text="First Name",font=("Verdana",12,"bold"),bg="white",fg="black")
        self.first_name.place(x=250,y=80)
        self.entry_first = Entry(frame,font=("Verdana",10,),bg="light grey")
        self.entry_first.place(x=250,rely=0.27)
        self.last_name = Label(frame, text="Last Name",font=("Verdana",12,"bold"),bg="white",fg="black")
        self.last_name.place(x=500,y=80)

        self.last_entry = Entry(frame,font=("Verdana",10,),bg="light grey")
        self.last_entry.place(x=500,rely=0.27)
        self.email = Label(frame, text="Email", font=("Verdana", 12, "bold"), bg="white", fg="black")
        self.email.place(x=250, y=150)
        self.entry_email = Entry(frame, font=("Verdana", 10,), bg="light grey")
        self.entry_email.place(x=250, rely=0.44)
        self.username  = Label(frame,text="Username", font=("Verdana", 12, "bold"), bg="white", fg="black")
        self.username.place(x=500,y=150)
        self.entry_user = Entry(frame,font=("Verdana", 10,), bg="light grey")
        self.entry_user.place(x=500,rely=0.44)
        self.password = Label(frame, text="Password", font=("Verdana", 12, "bold"), bg="white", fg="black")
        self.password.place(x=250, y=220)
        self.password_entry = Entry(frame, font=("Verdana", 10,), bg="light grey",show=" ")
        self.password_entry.place(x=250, rely=0.61)
        self.confirm_password = Label(frame, text="Confirm Password", font=("Verdana", 12, "bold"), bg="white", fg="black")
        self.confirm_password.place(x=500,y=220)
        self.confirm_entry = Entry(frame, font=("Verdana", 10,), bg="light grey",show=" ")
        self.confirm_entry.place(x=500, rely=0.61)

        sign = ImageTk.PhotoImage(file=("images\\btn.png"))
        reg = ImageTk.PhotoImage(Image.open("C:\\Users\\zumocom\\PycharmProjects\\passmanager\\passman\\images\\register.png"))
        self.item_add = Button(frame, text="SIGN UP!",image=sign,bg="white",bd="0",command=self.add_user)
        self.item_add.place(x=390,y=300)
        self.item_add = Button(frame, text="Alreday a user?",image=reg,bg="white",bd="0",command=self.login)
        self.item_add.place(x=350, y=350)


        self.root.mainloop()

    def add_user(self):
        first = self.entry_first.get()
        last =self.last_entry.get()
        email = self.entry_email.get()
        user = self.entry_user.get()
        passwd = self.password_entry.get()
        confirm = self.confirm_entry.get()
        b_passwd = passwd.encode("utf-8")
        hashed_passwd = bcrypt.hashpw(b_passwd,bcrypt.gensalt())
        hashed_user = self.register.hash_user(user)
        bytes_keys = self.register.random_keys()
        self.keys = bytes_keys.hex()

        try:
            if first != "" and last != "" and   email!="" and user!= "" and passwd !="" and confirm != "" :
                if self.register.check_email(email):
                    if passwd == confirm:
                            if self.register.add_user(hashed_user,hashed_passwd,first,last,email):
                                if self.register.insert_key(user,self.keys):

                                  messagebox.showinfo("User","Thank you for believing us, {} ".format(user))
                                  messagebox.showinfo("IMPORTANT","PLEASE REMEBER THIS KEY {}".format(self.keys))
                                 # self.root.destroy()
                                  l_gui()
                            else:
                                  messagebox.showerror("error","couldnt add")
                    else:
                            messagebox.showerror("error","Please check your password")
                else:
                    messagebox.showerror("error","Please check your email")
            else:
                messagebox.showerror("error","please fill up all the entry")
        except Exception:

                messagebox.showerror("Error","User name exists!",parent=self.root)
    def login(self):

        l_gui()



r_gui()