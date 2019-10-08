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

if tk.messagebox.askyesno("Setup Confirmation","Do you wish to install this series of programs?"):
    if os.geteuid() != 0:
        tk.messagebox.showerror("Root permissions needed!","This installer needs root permissions to append its scripts onto the applications menu. Level: "+str(os.geteuid()))
        exit("Root permissions needed!")

    with open("/usr/share/applications/GitTest.desktop", "w") as f:
        f.write("[Desktop Entry]\nName=Git Test\nType=Application\nExec=/home/andrew/Desktop/GIT/updater/pull/script.py\nTerminal=false\nIcon=/home/andrew/Desktop/GIT/updater/pull/icon.png\n")
        f.write("Comment=Clicking this application will pull from all known github directorys.\nNoDisplay=false\nCategories=Git\nName[en]=Git Test\nName[en_US]=Git Test\n")
        f.close()
    os.system("cd /usr/share/applications && chmod a+x GitTest.desktop")
