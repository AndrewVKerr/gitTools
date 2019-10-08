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

def add():
    return subprocess.check_output("git add .", shell=True)

def commit(changes):
    return subprocess.check_output("git commit -m \""+changes+"\"", shell=True)

def push():
    params = simpledialog.askstring("Additional Parameters", "Additional parameters:")
    cmd = "git push "+params
    return subprocess.check_output("mate-terminal --command \""+cmd+"\"", shell=True)

root = tk.Tk()
root.withdraw()

while messagebox.askyesno("Git push","Would you like to attempt to push a repositorys changes up to github?"):

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
            messagebox.showinfo("Git repo already up to date!","The selected directory \""+path+"\" is currently up to date with the github repo.")
            continue
        result = "\n".join(result)
        if messagebox.askyesno("Git push","The following files have been updated, would you like to attempt to push these changes to github?\n"+result):
            add()
            commit(result)
            print(push())
        else:
            print("Git push aborted!")
    else:
        print("Not a git folder")
        messagebox.showwarning("Git repo not found...", "The selected directory does not contain a .git file and has been ignored.")

    os.chdir(wd)
