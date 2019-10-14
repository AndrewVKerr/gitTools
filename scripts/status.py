#!/usr/bin/python3
# Andrew Kerr
# 10/09/2019

''' The purpose of this script is to execute a git add, commit, and push command upon execution. '''

import os
import subprocess
import tkinter as tk
from tkinter import simpledialog
from tkinter import filedialog
from tkinter import messagebox

def status():
    return subprocess.check_output("git status", shell=True)

root = tk.Tk()
root.withdraw()

while messagebox.askyesno("Git Status","Would you like to see the status of a repository?"):

    path = filedialog.askdirectory(initialdir = "./GIT", title = "Select a valid git repository directory")
    
    wd = os.getcwd()
    os.chdir(path)

    if os.path.exists(path+"/.git"):
        stat = status().decode("utf-8").split("\n")
        result = []    
        for item in stat:
            if "\t" in item:
                result.append(item.replace("\t",""))
            else:
                if len(result) > 0:
                    break
        if len(result) <= 0:
            messagebox.showinfo("Git repo is all caught up!","The selected directory \""+path+"\" is currently up to date with the github repo.")
            continue
        result = "\n".join(result)
        messagebox.showinfo("Git repo has changes!",result)
    else:
        print("Not a git folder")
        messagebox.showwarning("Git repo not found...", "The selected directory does not contain a .git file and has been ignored.")

    os.chdir(wd)
