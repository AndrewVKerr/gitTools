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
    def add(self,args="",selector="."):
        return subprocess.check_output("git add "+args+(" " if args != "" else "")+selector, shell=True)
    
    #git status [<options>...] [--] [<pathspec>...]
    def status(self, options=None, pathspec=None):
        return subprocess.check_output("git status"+("" if selector == "" else " "+selector), shell=True)
    
    #git pull [<options>] [<repository> [<refspec>...]]
    def pull(self, options=None, repository=None, refspec=None):
        return subprocess.check_output("git pull"+
                                       ("" if options == None else " "+options)+
                                       ("" if repository == None else " "+repository +
                                        ("" if refspec == None else " "+refspec)
                                        )
                                       );
    
g = Git();
print(help(g.pull))
