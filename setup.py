#!/usr/bin/python3
# Andrew Kerr
# 10/08/2019

''' The purpose of this script is to setup all of the current scripts contained within the '''

import os
import subprocess
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def addApp(home,path_to_file,name,comment):
    filename = name.replace(" ","_")
    with open(home+"/.local/share/applications/"+filename+".desktop", "w") as f:
        f.write("[Desktop Entry]\n")
        f.write("Name="+name+"\n")
        f.write("Type=Application\n")
        f.write("Exec="+path_to_file+"/script.py\n")
        f.write("Terminal=false\n")
        f.write("Icon="+path_to_file+"/icon.png\n")
        f.write("Comment="+comment+"\n")
        f.write("NoDisplay=false\n")
        f.write("Categories=Development;Programming\n")
        f.write("Name[en]="+name+"\n")
        f.write("Name[en_US]="+name+"\n")
        f.close()
    os.system("cd "+home+"/.local/share/applications && chmod a+x "+filename+".desktop")

root = tk.Tk()
root.withdraw()

if tk.messagebox.askyesno("Setup Confirmation","Do you wish to install this series of programs?"):
    
    #if os.geteuid() != 0: # Not necessary as the .local directory applications does not need to root access to execute.
    #    tk.messagebox.showerror("Root permissions needed!","This installer needs root permissions to append its scripts onto the applications menu. Level: "+str(os.geteuid()))
    #    exit("Root permissions needed!")

    path = filedialog.askdirectory(initialdir = "/home/", title="Please select your home directory") 
    addApp(path,path+"/GIT/gitTools/pull/","Git Pull","Attempts to update the local repo with the repo on github.")
    
