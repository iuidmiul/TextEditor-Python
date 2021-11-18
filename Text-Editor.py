from tkinter import *
import os
from time import sleep
from tkinter import ttk
from tkinter import filedialog
from tkinter import font
from tkinter import messagebox
from typing import Sized

class Create_GUI:
    def __init__(self,root):
        #root
        self.root = root
        self.root.title("Text-Editor")
        self.root.geometry("800x600")
        
        #menu
        self.menu_bar = Menu(self.root,font=("times new roman",15,"bold"))
        self.root.config(menu=self.menu_bar)
        self.menu_bar.add_command(label="Open",font=("times new roman",12,"bold"),command=self.open_file)
        self.menu_bar.add_command(label="Save",font=("times new roman",12,"bold"),command=self.save_file)
        self.menu_bar.add_command(label="Close Document",font=("times new roman",12,"bold"),command=self.close_file)
        self.menu_bar.add_command(label="Exit",font=("times new roman",12,"bold"),command=self.close_app)
        
        #file name
        self.file_name_string = "Untitled"
        self.file_name_text = StringVar(self.menu_bar)
        self.file_name_text.set("Untitled")
        self.new_text = Label(self.root, textvariable = self.file_name_text, font=("times new roman",25,"bold"),bg="gray80")
        self.new_text.grid(column=1,row=1)
        self.new_text.pack(side=TOP,fill=BOTH)

        #file content
        self.file_content = Text(self.root,height=100)
        self.file_content.pack(anchor=S,fill=BOTH)

        #save state
        self.data_saved = ""

    #File Open
    def open_file(self):
        try:
            self.target_file = filedialog.askopenfilename(title="Select File")
            #file name text
            file_name = os.path.basename(self.target_file)
            self.file_name_text.set(file_name)
            if len(file_name) > 0:
                self.file_name_string = str(file_name)

            #content text
            read_file = open(self.target_file,"r")
            
            #delete old text
            self.file_content.delete("1.0",END)
            #write new text
            for i in read_file:
                self.file_content.insert(END,i)
            read_file.close()
        except:
            self.file_name_text.set(self.file_name_string)
            messagebox.showinfo("No file opened","NOTHING OPENED")
    
    #File Save
    def save_file(self):
        try:
            self.target_file = filedialog.asksaveasfilename(title="Save File",initialfile=self.file_name_string)
            #file name text
            file_name = os.path.basename(self.target_file)
            self.file_name_text.set(file_name)
            if len(file_name) > 0:
                self.file_name_string = str(file_name)

            #get data
            data = self.file_content.get("1.0",END)

            #content text
            read_write_file = open(self.target_file,"w")
            read_write_file.write(data)
            read_write_file.close()
        except:
            self.file_name_text.set(self.file_name_string)
            messagebox.showinfo("Saving Cancelled","NOTHING SAVED")

    #Close Document
    def close_file(self):
        try:
            self.file_name_text.set("Untitled")
            self.file_content.delete("1.0",END)
        except:
            messagebox.showerror("Error","ERROR")

    def close_app(self):
        try:
            self.root.destroy()
        except:
            messagebox.showerror("Error","ERROR")


root = Tk()
Create_GUI(root)
root.mainloop()