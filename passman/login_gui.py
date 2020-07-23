from tkinter import *
from tkinter import messagebox
from passman.login import login
from  passman.register import register
import bcrypt
from passman.sub_menu import sub_menu
from  PIL import  Image,ImageTk
class l_gui:
    def __init__(self):
        self.root = Toplevel()
        self.root.geometry("900x600+280+50")
        self.root.title("PASSWORD MANAGER")
        self.login_user = login()
        self.register_user = register()

        self.bg = ImageTk.PhotoImage(file="images\\loginback.jpg")
        bg = Label(self.root,image=self.bg).place(x=-250,y=-50)

        frame = Frame(self.root, bg="white"
                                    "")
        frame.place(x=190, y=120, width=700, height=400)
        self.left = ImageTk.PhotoImage(file="images\\side-security.jpg")
        left = Label(self.root, image=self.left, bg="black").place(x=5, y=145, height=350)
        title = Label(frame, text="LOGIN", font=("Verdana", 18, "bold"), bg="white", fg="maroon")
        title.place(x=250, y=30)


        self.user_name = Label(frame, text="Username",font=("Verdana",12,"bold"),bg="white",fg="black")
        self.user_name.place(x=403,y=70)

        self.entry_user = Entry(frame,font=("Verdana",10,),bg="light grey")
        self.entry_user.place(x=375,y=100)
        self.password = Label(frame, text="Password",font=("Verdana",12,"bold"),bg="white",fg="black")
        self.password.place(x=403,y=130)


        self.password_entry = Entry(frame,font=("Verdana",10,),bg="light grey",show=" ")
        self.password_entry.place(x=375,y=160)
        login_img = ImageTk.PhotoImage(file ="images\\button_login.png")
        forget_img = ImageTk.PhotoImage(file="images\\button_forgot-password (2).png")
        login_btn = Button(frame, text="LOGIN",image=login_img, bg="white",bd="0",command =self.login)
        login_btn.image = login_img
        login_btn.place(x=382,y=210)
        forget_btn = Button(frame, text="LOGIN", image=forget_img, bg="white", bd="0", command=self.forget_top)
        forget_btn.image = forget_img
        forget_btn.place(x=320, y=280)

        
    def login(self):
        user = self.entry_user.get()
        passwd = self.password_entry.get()
        encode_pass= passwd.encode("utf8")
        hashed_user =self.register_user.hash_user(user)
        data = self.login_user.show_data_one(hashed_user)
        if user != "" and passwd != "":
            try:
                salt = data[2]
                if salt!=None:

                    if bcrypt.checkpw(encode_pass,salt.encode("utf8")):

                         sub_menu(user)

                    else:
                        messagebox.showerror("Error","username or password mismatched",parent=self.root)
            except Exception:
                messagebox.showerror("Error","User doesn't exist",parent=self.root)
        else:
            messagebox.showerror("error","please fill up all the entry")
    def forget_top(self):
        top = Toplevel(self.root, bg="white")
        top.geometry("400x400+550+150")
        key_label = Label(top,bg="white")
        key_label.pack()
        key_label = Label(top,bg="white")
        key_label.pack()
        key_label = Label(top, text="Enter the key", font=("Verdana", 10, "bold"), bg="white", fg="black")
        key_label.pack()
        self.key_entry = Entry(top, font=("Verdana", 8,), bg="light grey")
        self.key_entry.pack()
        key_label = Label(top, bg="white")
        key_label.pack()
        new_label = Label(top, text="New Password", font=("Verdana", 10, "bold"), bg="white", fg="black")
        new_label.pack()
        self.new_password = Entry(top, font=("Verdana", 8,), bg="light grey")
        self.new_password.pack()
        key_label = Label(top, bg="white")
        key_label.pack()
        con_label  = Label(top, text="Confirm Password", font=("Verdana", 10, "bold"), bg="white", fg="black")
        con_label.pack()
        self.confirm_pass = Entry(top, font=("Verdana", 8,), bg="light grey")
        self.confirm_pass.pack()
        key_label = Label(top, bg="white")
        key_label.pack()
        forget_img = ImageTk.PhotoImage(file="images\\button_update.png")
        get_btn = Button(top, text="get",  image=forget_img, bg="white", bd="0",command=self.forget_password)
        get_btn.image = forget_img
        get_btn.pack()
    def forget_password(self):

        key =self.key_entry.get()
        new_pwd = self.new_password.get()
        con_pwd= self.confirm_pass.get()
        save_key = self.login_user.return_keys(key)
        b_passwd = new_pwd.encode("utf-8")
        hashed_passwd = bcrypt.hashpw(b_passwd, bcrypt.gensalt())

        if key !="" and new_pwd!="" and con_pwd !="" :
            if save_key!=None:
                username = save_key[0]
                hashed_user = self.register_user.hash_user(username)

                if new_pwd == con_pwd:
                    if self.login_user.update_password(hashed_passwd,hashed_user):

                        messagebox.showinfo("Success!","password updated")
                else:
                    messagebox.showerror("Error!", "Please check your password")
            else:
                messagebox.showerror("Error!", "Please enter the right key")
        else:
            messagebox.showerror("Error!","Please fill up the entry")