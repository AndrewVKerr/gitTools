#!/usr/bin/python3
# Andrew Kerr
# 10/08/2019

''' The purpose of this script is to execute a git pull command upon execution. '''

import os
import subprocess
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def pull(path):
    return subprocess.check_output("cd "+str(path)+" && git pull", shell=True)

root = tk.Tk()
root.withdraw()

while tk.messagebox.askyesno("Git Pull","Would you like to attempt to pull a repositorys changes down from github?"):

    path = filedialog.askdirectory(initialdir = "./GIT", title = "Select a valid git repository directory")

    if os.path.exists(path+"/.git"):
        messagebox.showinfo("Git repo updated...","Attempting a pull on git repo \""+path+"\".\nResponse: "+str(pull(path).decode("utf-8")))
    else:
        print("Not a git folder")
        messagebox.showwarning("Git repo not found...", "The selected directory does not contain a .git file and has been ignored.")
