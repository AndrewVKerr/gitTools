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
    stat = subprocess.check_output("git status -uno", shell=True).decode("utf-8").split("\n")
    result = []    
    ready = False
    for item in stat:
        if "\t" in item:
            result.append(item.replace("\t",""))
        else:
            if "Your branch is ahead of" in item or "Changes not staged for commit" in item:
                ready = True
            if len(result) > 0:
                break
    return (stat,result,ready)
def add():
    return subprocess.check_output("git add .", shell=True)

def commit(message,changes):
    if len(message) <= 0:
        return subprocess.check_output("git commit -m \""+changes+"\"", shell=True)
    else:
        return subprocess.check_output("git commit -m \""+message+"\"", shell=True)

def push():
    params = simpledialog.askstring("Additional Parameters", "Additional parameters:")
    cmd = "git push "+params
    return subprocess.check_output("mate-terminal --command \""+cmd+"\"", shell=True)

root = tk.Tk()
root.withdraw()

while messagebox.askyesno("Git Push","Would you like to attempt to push a repositorys changes up to github?"):

    path = filedialog.askdirectory(initialdir = "./GIT", title = "Select a valid git repository directory")
    
    wd = os.getcwd()
    os.chdir(path)

    if os.path.exists(path+"/.git"):
        stat = status()
        result = "\n".join(stat[1])
        if not stat[2]:
            messagebox.showinfo("Git repo already up to date!","The selected directory \""+path+"\" is currently up to date with the github repo. Nothing to push!")
            continue
        if messagebox.askyesno("Git push","The following files have been updated, would you like to attempt to push these changes to github?\n"+result):
            if len(result) > 0:
                add()
                commit(simpledialog.askstring("Custom Message", "Custom message for commit, leave blank for message to list modified files."),result)
            print(push())
            messagebox.askokcancel("Awaiting push", "Please input your username and password when prompted by a seperate console.\nDO NOT PRESS\nOk or Cancel until the seperate console has closed!")
            stat = status()
            if stat[2]:
                messagebox.showwarning("Git push failed!", "Push was not successfull for some reason, this could happen if you entered in the wrong account information.")
                continue
        else:
            print("Git push aborted!")
    else:
        print("Not a git folder")
        messagebox.showwarning("Git repo not found...", "The selected directory does not contain a .git file and has been ignored.")

    os.chdir(wd)
