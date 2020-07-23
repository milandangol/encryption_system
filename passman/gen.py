
import random
# import pyperclip
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import *


class generator_gui:
    def __init__(self):
        self.root = Toplevel()
        self.root.geometry("500x500")
        self.root.title("PASSWORD MANAGER")
        self.label = Label(self.root, text='Welcome')
        self.rad = IntVar()
        self.password = ""


        self.var1 = IntVar()
        self.Random_password = Label(self.root, text="Password")
        self.Random_password.grid(row=0)
        self.entry = Entry(self.root)
        self.entry.grid(row=0, column=1)
        self.a = StringVar()
        self.c_label = Label(self.root, text="Length")
        self.c_label.grid(row=1)
        self.copy_button = Button(self.root, text="Copy", command=self.copy1)
        self.copy_button.grid(row=0, column=2)
        self.generate_button = Button(self.root, text="Generate", command=self.generate)
        self.generate_button.grid(row=0, column=3)
        self.gender = StringVar()
        #self.rb_male = Radiobutton(self.root, text="male", value="Male", variable=self.gender, command=self.test).grid(row=1, column=2, sticky='E')
        #self.rb_male = Radiobutton(self.root, text="female", value="Female", variable=self.gender, command=self.test).grid(row=1, column=3, sticky='E')
        #self.rb_male = Radiobutton(self.root, text="other", value="Other", variable=self.gender, command=self.test).grid(row=1, column=4, sticky='E')
        #self.rb = ttk.Radiobutton(self.root, text="Male", value="4", variable=self.rad, command=self.test) .grid(row=1, column=5)
        self.radio_low = ttk.Radiobutton(self.root, text="LOW", variable=self.rad, value=1, command=self.main_gen)
        self.radio_low.grid(row=1, column=2, sticky='E')
        self.radio_middle = ttk.Radiobutton(self.root, text="Medium", variable=self.rad, value=2, command=self.main_gen)
        self.radio_middle.grid(row=1, column=3, sticky='E')
        self.radio_strong = ttk.Radiobutton(self.root, text="Strong", variable=self.rad, value=3, command=self.main_gen)
        self.radio_strong.grid(row=1, column=4, sticky='E')
        self.combo = Combobox(self.root, textvariable=self.var1, state="readonly", values=[8, 9, 10, 11, 12, 13, 14, 15, 16,
                                                                                           17, 18, 19, 20, 21, 22, 23, 24, 25,
                                                                                           26, 27, 28, 29, 30, 31, 32,
                                                                                           "Length"])
        self.combo.current(0)
        self.combo.bind('<<ComboboxSelected>>')
        self.combo.grid(column=1, row=1)
        self.root.mainloop()


    def test(self):
        messagebox.showinfo('Test', self.gender.get())


    def main_gen(self):
        self.entry.delete(0, END)
        length = int(self.combo.get())
        val = self.rad.get()
        print(val)
        lower = "abcdefghijklmnopqrstuvwxyz"


        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        digits = "!@#$%^&*()"
        password = ""
        # if strength selected is low
        if val == 1:
            for i in range(0, length):
                password = password + random.choice(lower)
            return password
        # if strength selected is medium
        elif val == 2:
            for i in range(0, length):
                password = password + random.choice(upper)
            return password
        # if strength selected is strong
        elif val == 3:
            for i in range(0, length):
                password = password + random.choice(digits)
            return password
        else:
            print("Please choose an option")


    def generate(self):
        passwords = self.main_gen()
        self.entry.insert(0, str(passwords))


    def copy1(self):
        random_password = self.entry.get()
        # pyperclip.copy(random_password)



