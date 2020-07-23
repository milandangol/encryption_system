
from  passman.register import register
from passman.manager import manager
from  tkinter import messagebox
import pyclipper
from PIL import ImageTk
from tkinter import *
from tkinter import ttk
from passman.images.data import Data
class manager_gui():
    def __init__(self,user):

            self.root = Toplevel()
            self.root.geometry("900x600+280+50")
            self.root.title("PASSWORD MANAGER")
            self.register = register()
            self.name = user


            self.manager = manager()
            self.index =""
            self.root.configure(bg="black")
            frame = Frame(self.root,bg="white")
            frame.place(x=240, y=50, width=550, height=500)
            title = Label(frame, text="PASSWORD MANAGER \n 'Your datas are safe with us '",
                          font=("verdana", 10, "bold"), bg="white", fg="maroon")
            title.pack()
            self.website = Label(frame, text="Website Name",font=("Verdana",10,"bold"),bg="white",fg="black")
            self.website.place(x=30,y =70)
            self.website_entry = Entry(frame,font=("Verdana",8,),bg="light grey")
            self.website_entry.place(x=30,y =90)
            self.password = Label(frame, text="Password",font=("Verdana",10,"bold"),bg="white",fg="black")
            self.password.place(x=210,y=70)
            self.password_entry = Entry(frame,font=("Verdana",8,),bg="light grey")
            self.password_entry.place(x=210,y =90)
            self.email = Label(frame, text="Email", font=("Verdana", 10, "bold"), bg="white", fg="black")
            self.email.place(x=380 , y=70)
            self.emai_entry = Entry(frame, font=("Verdana", 8,), bg="light grey")
            self.emai_entry.place(x=380, y=90)
            save_img = ImageTk.PhotoImage(file="images\\button_save-password (1).png")
            self.save= Button(frame, image = save_img,bg="white", bd="0",command = self.returndata)
            self.save.image = save_img
            self.save.place(x=10,y =160)
            update_img = ImageTk.PhotoImage(file="images\\button_update-password.png")
            self.update = Button(frame, image = update_img ,bg="white", bd="0", command=self.update_pass)
            self.update.image = update_img
            self.update.place(x=180,y =160)
            get_img = ImageTk.PhotoImage(file="images\\button_get-password (1).png")

            self.get_pass = Button(frame, image = get_img,bg="white", bd="0", command=self.get_password)
            self.get_pass.image = get_img
            self.get_pass.place(x=380,y =160)
            self.password_tree =ttk.Treeview(frame, columns=("email","website"))

            self.password_tree.place(x=70,y=200)
            self.password_tree['show'] = 'headings'
          

            self.password_tree.column('website',)

            self.password_tree.column('email', )

            self.password_tree.heading('website', text="WEBSITE NAME")
            self.password_tree.heading('email', text="EMAIL", )
            self.show_password_tree()

            keys = self.manager.return_keys(user)
            self.new_keys = keys[0][0].encode("utf-8")


            self.root.mainloop()
    def returndata(self):
            user = self.name
            print(user)
            website = self.website_entry.get()
            password = self.password_entry.get()
            email =self.emai_entry.get()
            #f_pass = password.encode("utf-8")
            #salt_pass = self.manager.salt_passwd(f_pass)


            en_pas = self.manager.passwd_encrpt(self.new_keys,password)

            if website != "" or password != "":
                    self.data = Data(website,en_pas,user,email)
                    if self.manager.add_data(self.data.get_website(),self.data.get_passwords(),self.data.get_users(),self.data.get_email()):
                            messagebox.showinfo("password", "password added, THANK YOU FOR TRUSTING US ")
                            self.show_password_tree()

                    else:
                            messagebox.showerror("error", "couldnt add")
            else:
                    messagebox.showerror("error", "fill up the form")


    def update_pass(self):
            if self.index=="":
                    messagebox.showerror("Error","Please select a row first")
            else:
                website = self.website_entry.get()
                password = self.password_entry.get()
                email =self.emai_entry.get()
                salt_pass = self.manager.passwd_encrpt(self.new_keys,password)
                self.data = Data(website,salt_pass,email,self.name)

                if self.manager.update_password(self.data.set_website(website),self.data.set_passwords(salt_pass),self.data.set_email(email), users = self.name ):
                        messagebox.showinfo('Item', "Item Updated")
                        self.show_password_tree()
                        self.update_index = ""
                else:
                        messagebox.showerror("Error", 'Can not be updated !!!')

    def delete_pasword(self):
            pass
    def get_password(self):
            top = Toplevel(self.root,bg="white")
            top.geometry("200x200")
            website_label = Label(top,text="website",font=("Verdana",10,"bold"),bg="white",fg="black")
            website_label.pack()
            self.website_entry = Entry(top,font=("Verdana",8,),bg="light grey")
            self.website_entry.pack()

            get_btn = Button(top,text="get",command = self.get)
            get_btn.pack()
    def get(self):
            website=self.website_entry.get()
            get_pswd = self.manager.show_passsword(self.name, website)

            password = get_pswd[0][0]

            plain = self.manager.passwd_decpt(password,self.new_keys)
            print(plain)
    def show_password_tree(self):
            self.password_tree.delete(*self.password_tree.get_children())
            data = self.manager.show_data(self.name)
            for i in data:
                    self.password_tree.insert("", "end", text=i[0], value=(i[4], i[1]))
            self.password_tree.bind("<Double-1>", self.select_password)

    def select_password(self, event):
            selected_row = self.password_tree.selection()[0]

            selected_pass = self.password_tree.item(selected_row, 'values')
            self.index = self.password_tree.item(selected_row, 'text')
            self.website_entry.delete(0, END)
            self.website_entry.insert(0, selected_pass[1])
            self.emai_entry.delete(0,END)
            self.emai_entry.insert(0,selected_pass[0])