import os
import glob
from tkinter import *

def rename_files():
    folder = folder_var.get()
    base_name = base_name_var.get()

    os.chdir(folder)
    files = glob.glob("*.*")

    for i, file in enumerate(files):
        new_name = base_name + str(i+1).zfill(3) + os.path.splitext(file)[1]
        os.rename(file, new_name)

#    messagebox.showinfo("Renaming Complete", "All files have been renamed!")

root = Tk()
root.title("File Renamer")

folder_var = StringVar()
base_name_var = StringVar()

folder_label = Label(root, text="Enter the full path of the folder containing the files: ")
folder_label.pack()
folder_entry = Entry(root, textvariable=folder_var)
folder_entry.pack()

base_name_label = Label(root, text="Enter the base name for the files: ")
base_name_label.pack()
base_name_entry = Entry(root, textvariable=base_name_var)
base_name_entry.pack()

rename_button = Button(root, text="Rename Files", command=rename_files)
rename_button.pack()

root.mainloop()

