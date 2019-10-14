#!/usr/bin/python3
# Andrew Kerr
# 10/08/2019

''' The purpose of this script is to either setup or destroy the current application references'''

import os
import subprocess
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def create_category(home, currdir):
    file_location = currdir+"/menudata"
    menu_location = home+"/.config/menus/applications-merged/"
    filename = "git.menu"
    with open(menu_location+filename,"w") as f:
        with open(file_location,"r") as f1:
            for line in f1:
                f.write(line)
            f1.close()
        f.close()
    os.system("chmod a+x "+menu_location+filename)

def addApp(home,category,fname,name,comment):
    filepath = currdir + fname;
    filename = name.replace(" ","_")+".desktop"
    with open(app_location+filename, "w") as f:
        f.write("[Desktop Entry]\n")
        f.write("Name="+name+"\n")
        f.write("Type=Application\n")
        f.write("Exec="+filepath+".py\n")
        f.write("Terminal=false\n")
        f.write("Icon="+filepath+".png\n")
        f.write("Comment="+comment+"\n")
        f.write("NoDisplay=false\n")
        f.write("Categories="+category+"\n")
        f.write("Name[en]="+name+"\n")
        f.write("Name[en_US]="+name+"\n")
        f.close()
    os.system("chmod a+x "+app_location+filename)

def doesCategoryExist():
    menu_location = home+"/.config/menus/applications-merged/"
    filename = "git.menu"
    return os.path.exists(menu_location+filename)

def destroyCategory():
    menu_location = home+"/.config/menus/applications-merged/"
    filename = "git.menu"
    os.remove(menu_location+filename)

def destroyApp(name):
    filename = name.replace(" ","_")+".desktop"
    os.remove(app_location+filename)

root = tk.Tk()
root.withdraw()

home = os.path.expanduser("~")
if home == None or home == "" or not tk.messagebox.askyesno("Is this you?", "Is \""+home+"\" your home directory?"):
    home = filedialog.askdirectory(initialdir = "/home/", title="Please select your home directory")
app_location = home+"/.local/share/applications/"  

if tk.messagebox.askyesno("Setup Confirmation","Please press yes if you wish to install or update the program, no to exit."):

    currdir = os.path.dirname(os.path.realpath(__file__)) 
    
    try:
        create_category(home,currdir)
        currdir = currdir + "/"
        addApp(home,"Github","updater","Git Tools Updater","Attempts to update the local repo with the repo on github.")
        addApp(home,"Git","pull","Git Pull","Attempts to update the local repo with the repo on github.")
        addApp(home,"Git","push","Git Push","Attempts to update the github repo with the local repo on this device.")
        addApp(home,"Git","status","Git Status","Retrieves the status of the local repo on this device.")
        addApp(home,"Git","commit","Git Commit","Commits any current changes from a repository on this device.")
    except Exception as e:
        tk.messagebox.showerror("Failed",str(e))
    
else:
    
    if doesCategoryExist():
        if tk.messagebox.askyesno("Uninstall shortcuts", "Would you like to attempt to uninstall the shortcuts?"):
            try:
                destroyCategory()
                destroyApp("Git Tools Updater")
                destroyApp("Git Pull")
                destroyApp("Git Push")
                destroyApp("Git Status")
                destroyApp("Git Commit")
            except Exception as e:
                tk.messagebox.showerror("Failed",str(e))

