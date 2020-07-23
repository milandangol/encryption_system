from tkinter import *
from tkinter import filedialog
from passman.file_encryption import file
from tkinter import  messagebox
import os
class file_gui:
    def __init__(self,name):
        self.root = Toplevel()
        self.file =file()
        self.name = name
        self.root.geometry("900x600+280+50")
        self.root.title("PASSWORD MANAGER")
        self.root.configure(bg="black")
        self.frame = Frame(self.root, bg="white")
        self.frame.place(x=240, y=50, width=500, height=400)
        title = Label(self.frame, text="WELCOME TO  FILE ENCRYPTION SYSTEM", font=("VERDANA", 12, "bold"),
                      bg="white", fg="maroon")
        title.pack()
        open_label = Label(self.frame,text = "Open a file to encrypt",font=("Verdana", 10, "bold"), bg="white", fg="black")
        open_label.place(x=173,y =70)
        self.openfile = Button(self.frame, text="OPEN AND ENCRYPT A FILE ", command=self.open_file)
        self.openfile.place(x=190, y=100)

        self.file_saveas = Label(self.frame, text="save file as in DB: ", font=("Verdana", 10, "bold"), bg="white",
                                 fg="black")
        self.file_saveas.place(x=180, y=145)

        self.file_saveas_entry = Entry(self.frame,font=("Verdana",8,),bg="light grey")
        self.file_saveas_entry.place(x=180, y=165)
        self.save_lable = Label(self.frame, text="open a file to save  ", font=("Verdana", 10, "bold"), bg="white",
                                fg="black")
        self.save_lable.place(x=180, y=190)
        self.save_btn = Button(self.frame, text="Open and Save", command=self.save_file).place(x=200, y=220)

        self.check_label = Label(self.frame,text = "enter the key to decrypt ",font=("Verdana", 10, "bold"), bg="white", fg="black")
        self.check_label.place(x=150,y =260)
        self.decrypt_file = Button(self.frame, text="enter here", command=self.top_level)
        self.decrypt_file.place(x=200, y=300)
        self.keys = self.file.return_keys(self.name)


        self.new_keys = self.keys[0][0].encode("utf-8")




        self.root.mainloop()
    def open_file(self):
        self.filename = filedialog.askopenfilename(initialdir="SAMPLE_IMAGE\\IMAGE_TO_ ENCRYPT", title ="select a file ", filetype=(("jpeg","*jpg"),("All Files","*.*")))
        encypt = self.file.encrpyt(key=self.new_keys,filename=self.filename)
        if encypt:
            messagebox.showinfo("Success!","Encryption successful \n please select .encrypted file")
    def save_file(self):
        self.file_save = filedialog.askopenfilename(initialdir="SAMPLE_IMAGE\\IMAGE_TO_ ENCRYPT",title="select a file",filetype=(("encrypted","*encrypted"),("All Files","*.*")))
        binary_data = self.file.img_to_binary(self.file_save)

        file_name = self.file_saveas_entry.get()
        data = self.file.retrive_img_file_name(self.name)
        if len(data)==0:
            if self.file.encrypt_save(self.name,binary_data,file_name):
                messagebox.showinfo("Success!","Data has been saved successfully")
        else:
            new_data = list(zip(*data))[3]
            if file_name in new_data:
                    messagebox.showerror("Error","File name exist")
            else:
                if self.file.encrypt_save(self.name,binary_data,file_name):
                    messagebox.showinfo("Success!","Data has been saved successfully")
    def top_level(self):
        self.top = Toplevel(self.root, bg="white")
        self.top.geometry("200x200")
        key_label = Label(self.top, text="key", font=("Verdana", 10, "bold"), bg="white", fg="black")
        key_label.pack()
        self.key_entry = Entry(self.top, font=("Verdana", 8,), bg="light grey")
        self.key_entry.pack()
        get_btn = Button(self.top, text="check", command=self.check_key)
        get_btn.pack()
    def check_key(self):
        key = self.key_entry.get().encode("utf-8")

        if self.new_keys==key:
            messagebox.showinfo("Succes","key matched now you can decrpyt the file")
            get_btn = Button(self.frame, text="Decrypt", command=self.decypt_top)
            get_btn.place(x=200, y=350)
            self.top.destroy()

        else:
            messagebox.showerror("incorrect","please enter right key!")
    def decypt_top(self):
        self.decrypt_top = Toplevel(self.root,bg="white")
        self.decrypt_top.geometry("200x200")
        file_label = Label(self.decrypt_top, text="FILE NAME", font=("Verdana", 10, "bold"), bg="white", fg="black")
        file_label.pack()
        self.file_entry = Entry(self.decrypt_top, font=("Verdana", 8,), bg="light grey")
        self.file_entry.pack()

        get_btn = Button(self.decrypt_top, text="check", command=self.write_img)
        get_btn.pack()

    def write_img(self):

        location= self.file_entry.get()
        basename = os.path.basename(location+".encrypted")
        path = "SAMPLE_IMAGE\\IMAGE_TO_DECRYPT"
        file_name = os.path.join(path,basename)

        
        img = self.file.retrive_img(self.name,location)
        try:
            data=img[0][2]
            self.file.write_file(filename=file_name, data=data)
            get_btn = Button(self.decrypt_top, text="open", command=self.decryption)
            get_btn.pack()

        except Exception:
            messagebox.showerror("error","file name doesnt exist ")

    def decryption(self):

        path ="SAMPLE_IMAGE\\IMAGE_TO_DECRYPT"
        open_file= filedialog.askopenfilename(initialdir=path,title="select a file",filetype=(("encrypted","*encrypted"),("All Files","*.*")))
        decrypt = self.file.decrypt(open_file,self.new_keys)
        if decrypt:
            messagebox.showinfo("success!","File has been sucessfully decrypted")
        else:
            messagebox.showerror("Error","cant decryp the file ")