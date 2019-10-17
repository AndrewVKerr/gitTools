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

class Git:
    
    def setDirectory(self, location):
        os.chdir(location)
        return os.getcwd()
    
    #git add [<options>...] [--] [<pathspec>...]
    def add(self,options=None,pathspec="."):
        return subprocess.check_output("git add "+
                                       ("" if options == None else " "+options)+
                                       pathspec
                                       , shell=True)
    
    #git status [<options>...] [--] [<pathspec>...]
    def status(self, options=None, pathspec=None):
        return subprocess.check_output("git status"+
                                       ("" if options == None else " "+selector)+
                                       ("" if pathspec == None else " "+pathspec)
                                       , shell=True)
    
    #git pull [<options>] [<repository> [<refspec>...]]
    def pull(self, options=None, repository=None, refspec=None):
        return subprocess.check_output("git pull"+
                                       ("" if options == None else " "+options)+
                                       ("" if repository == None else " "+repository +
                                        ("" if refspec == None else " "+refspec)
                                        )
                                       , shell=True);

if(__name__ == "__main__"):
    g = Git();
    try:
        g.setDirectory("./..")
        print(g.status().decode("utf-8"))
        
    except Exception as e:
        messagebox.showerror("Failed to execute git command",e)