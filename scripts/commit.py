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

class Commit:
    def status():
        return subprocess.check_output("git status", shell=True)

    def add():
        return subprocess.check_output("git add .", shell=True)

    def commit(self,message,changes):
        if len(message) <= 0:
            return subprocess.check_output("git commit -m \""+changes+"\"", shell=True)
        else:
            return subprocess.check_output("git commit -m \""+message+"\"", shell=True)

    def __init__(self):
        root = tk.Tk()
        root.withdraw()

message = "Would you like to attempt to commit a repositorys changes?"

while messagebox.askyesno("Git Commit",message):

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
        if messagebox.askyesno("Git Commit","The following files have been updated, would you like to attempt to commit these changes?\n"+result):
            try:
                add()     
                commit(simpledialog.askstring("Custom Message", "Custom message for commit, leave blank for message to list modified files."),result)
                messagebox.showinfo("Git Commit","The commit was successfull.")
            except Exception as e:
                messagebox.showwarning("Git Commit Failed","The commit has failed!\n\t- Thrown Exception: "+str(e))
        else:
            print("Git push aborted!")
        message = "Would you like to attempt to commit another repositorys changes?"
    else:
        print("Not a git folder")
        messagebox.showwarning("Git repo not found...", "The selected directory does not contain a .git file and has been ignored.")

    os.chdir(wd)
