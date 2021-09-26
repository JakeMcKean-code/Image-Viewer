"""
Created on Sunday Sep 26 17:32:16 2021

@author: Jake McKean
"""
# --------------------------------------------------------------
# Use the os package to list all the files in my images directory and then 
# append them all to a list
from os.path import join
import os
import glob
from PIL import ImageTk, ImageFile
import PIL.Image
from tkinter import *
from tkinter import Label
from tkinter import Button
from tkinter import Tk
from tkinter.filedialog import askdirectory
from tkinter import messagebox
# --------------------------------------------------------------
class window():
    def __init__(self, master):
        self.master = master
        master.geometry("1100x750")
        master.title("Image Viewer")
        self.image_list = []
        self.files = []
        self.image_num = 0
        master.configure(bg='#355C7D')

    # First screen of the application     
    def open_directory_screen(self):
        self.path_to_directory = StringVar()
        self.frame = LabelFrame(self.master, padx = 20, pady = 10) # padding here controls the padding inside the frame
        self.frame.configure(bg='#6C5B7B')
        self.frame.grid(row = 2, column = 1, padx = 470, pady=250) # padding here controls how sunken in the frame is in the window
        
        self.Set_button = Button(self.frame, text = "Press to view images", command = self.open_directory)
        self.Set_button.grid(row = 6, column = 0, columnspan = 3, pady=20)
        
        self.File_button = Button(self.frame, text = "Choose image directory", command = self.get_directory)
        self.File_button.grid(row = 3, column = 0, pady = 20)
        return
        
    def get_directory(self):
        path = askdirectory()
        self.path_to_directory.set(path)
        return    
    def open_directory(self):
        self.SAVE_PATH = self.path_to_directory.get()
        self.remove_window(self.frame)
        return
    
    def forward(self, image_number):
        self.back_button = Button(root, text = "<<", command = lambda: self.backward(self.image_num))
        self.back_button.grid(row = 1, column = 1)
        # delete image and redefine the label with the new image
        if(image_number < (len(self.image_list)-1)):
            self.my_label.grid_forget()
            self.my_label = Label(image = self.image_list[self.image_num+1], padx = 10, pady = 20)
            self.image_num += 1
            self.my_label.grid(row = 0, column = 1, columnspan = 3)
        if(self.image_num == len(self.image_list)-1): 
            self.forward_button = Button(root, text = ">>", state = DISABLED)
            self.forward_button.grid(row = 1, column = 3)

        # Text for status bar    
        status_text = "Image " + str(self.image_num + 1) + " of " + str(len(self.image_list))
        self.status = Label(root,text = status_text, bd = 1, relief = SUNKEN)
        self.status.grid(row = 2, column = 3)
        return

    def backward(self, image_number):
        # delete image and redefine the label with the new image
        if(self.image_num ==1):
            self.back_button = Button(root, text = "<<", state = DISABLED)
            self.back_button.grid(row = 1, column = 1)
        if(image_number != 0):
            self.forward_button = Button(root, text = ">>", command = lambda: self.forward(self.image_num))
            self.forward_button.grid(row = 1, column = 3)
            self.my_label.grid_forget()
            self.image_num -= 1
            self.my_label = Label(image = self.image_list[self.image_num-1], padx = 10, pady = 20)
            self.my_label.grid(row = 0, column = 1, columnspan = 3)
        
        # Text or status bar
        status_text = "Image " + str(self.image_num+1) + " of " + str(len(self.image_list))
        self.status = Label(root,text = status_text, bd = 1, relief = SUNKEN)
        self.status.grid(row = 2, column = 3)
        return

    # Second screen of the application
    def second_frame(self):
        # element in the file
        for filename in glob.glob(os.path.join(self.SAVE_PATH,"*.png")):
            self.files.append(filename)

        for j in self.files:
            self.image_list.append(ImageTk.PhotoImage(PIL.Image.open(join(self.SAVE_PATH,j)).resize((1000,600))))

        self.my_label = Label(image = self.image_list[self.image_num], padx = 10, pady = 20)
        self.my_label.grid(row = 0, column = 1, columnspan = 3)
        # Create the back button
        self.back_button = Button(root, text = "<<", command = lambda: self.backward(self.image_num))
        if(self.image_num ==0):
                self.back_button = Button(root, text = "<<", state = DISABLED)
                self.back_button.grid(row = 1, column = 1)
        # Creating an exit button
        self.quit_button = Button(root, text = "press to exit", command = self.master.quit)
        # Creating the forward button
        self.forward_button = Button(root, text = ">>", command = lambda: self.forward(self.image_num + 1))

        self.back_button.grid(row = 1, column = 1)
        self.quit_button.grid(row = 1, column = 2)
        self.forward_button.grid(row = 1, column = 3, pady=10)

        # Create a status label
        status_text = "Image " + str(self.image_num+1) + " of " + str(len(self.image_list))
        self.status = Label(root,text = status_text, bd = 1, relief = SUNKEN)
        self.status.grid(row = 2, column = 3)
        return

    def remove_window(self, frame, first_time = True):
        frame.destroy()
        if(first_time == True):
            self.Set_button.destroy()
            self.second_frame()
        return
# --------------------------------------------------------------
root = Tk()
gui = window(root)
gui.open_directory_screen()
root.mainloop()  
root.mainloop()
