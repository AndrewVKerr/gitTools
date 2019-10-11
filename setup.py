#!/usr/bin/python3
# Andrew Kerr
# 10/08/2019

''' The purpose of this script is to either setup or destroy the current application references'''

import os
import subprocess
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def create_category(home):
    file_location = "./menudata"
    menu_location = home+"/.config/menus/applications-merged/"
    filename = "git.menu"
    with open(menu_location+filename,"w") as f:
        with open(file_location,"r") as f1:
            for line in f1:
                f.write(line)
            f1.close()
        f.close()
    os.system("chmod a+x "+menu_location+filename)

def addApp(home,path_to_file,name,comment):
    app_location = home+"/.local/share/applications/"
    filename = name.replace(" ","_")+".desktop"
    with open(app_location+filename, "w") as f:
        f.write("[Desktop Entry]\n")
        f.write("Name="+name+"\n")
        f.write("Type=Application\n")
        f.write("Exec="+path_to_file+"script.py\n")
        f.write("Terminal=false\n")
        f.write("Icon="+path_to_file+"icon.png\n")
        f.write("Comment="+comment+"\n")
        f.write("NoDisplay=false\n")
        f.write("Categories=Git;Development;Programming\n")
        f.write("Name[en]="+name+"\n")
        f.write("Name[en_US]="+name+"\n")
        f.close()
    os.system("chmod a+x "+app_location+filename)

root = tk.Tk()
root.withdraw()

if tk.messagebox.askyesno("Setup Confirmation","Do you wish to install this series of programs?"):
    
    #if os.geteuid() != 0: # Not necessary as the .local directory applications does not need to root access to execute.
    #    tk.messagebox.showerror("Root permissions needed!","This installer needs root permissions to append its scripts onto the applications menu. Level: "+str(os.geteuid()))
    #    exit("Root permissions needed!")
    
    home = filedialog.askdirectory(initialdir = "/home/", title="Please select your home directory") 
    currdir = os.getcwd()
    create_category(home)
    addApp(home,currdir+"/pull/","Git Pull","Attempts to update the local repo with the repo on github.")
    addApp(home,currdir+"/push/","Git Push","Attempts to update the github repo with the local repo on this device.")
    addApp(home,currdir+"/status/","Git Status","Retrieves the status of the local repo on this device.")
    addApp(home,currdir+"/commit/","Git Commit","Commits any current changes from a repository on this device.")
    
