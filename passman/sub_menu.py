from tkinter import *
from passman.gen import generator_gui
from passman.mannger_gui import manager_gui
from PIL import ImageTk
from passman.file_encryption_gui import file_gui

class sub_menu:
    def __init__(self,user):
        self.root = Toplevel()

        self.name = user
        self.root.geometry("900x600+280+50")
        self.root.title("PASSWORD MANAGER")
        self.root.configure(bg="black")
        self.bg = ImageTk.PhotoImage(file="images\\loginback.jpg")
        bg = Label(self.root, image=self.bg).place(x=-250, y=-50)
        frame = Frame(self.root, bg="white")
        frame.place(x=180,y=50, width=600, height=500)
        title = Label(frame, text="WELCOME TO PASSWORD MANAGER AND FILE SYSTEM ENCRYPTION", font=("times", 13, "bold"), bg="white", fg="maroon")
        title.pack()


       # self.welcome = Label(self.root, text="Welcome to passman,{}".format(self.name))
       # self.welcome.grid(row=1,column = 5)
        key_label = Label(frame, bg="white")
        key_label.pack()
        key_label = Label(frame, bg="white")
        key_label.pack()
        key_label = Label(frame, bg="white")
        key_label.pack()

        pass_man_img = ImageTk.PhotoImage(file="images\\button_password-manager.png")
        self.pass_man = Button(frame, image=pass_man_img, bg="white", bd="0", command=self.manager)
        self.pass_man.image = pass_man_img
        self.pass_man.pack()
        key_label = Label(frame, bg="white")
        key_label.pack()
        key_label = Label(frame, bg="white")
        key_label.pack()
        key_label = Label(frame, bg="white")
        key_label.pack()
        pass_gen_img = ImageTk.PhotoImage(file="images\\button_password-generator.png")
        self.pass_gen = Button(frame, image=pass_gen_img, bg="white", bd="0", command=self.generator)
        self.pass_gen.image = pass_gen_img
        self.pass_gen.pack()
        key_label = Label(frame, bg="white")
        key_label.pack()
        key_label = Label(frame, bg="white")
        key_label.pack()
        key_label = Label(frame, bg="white")
        key_label.pack()
        file_img = ImageTk.PhotoImage(file="images\\button_file-system-encryption.png")
        self.file_btn = Button(frame, image=file_img, bg="white", bd="0", command=self.file)
        self.file_btn.image = file_img
        self.file_btn.pack()

        self.root.mainloop()
    def manager(self):
        name = self.name
        manager_gui(name)
    def generator(self):
        generator_gui()

    def file(self):
        file_gui(self.name)