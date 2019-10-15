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
    def status(self, selector=""):
        return subprocess.check_output("git status"+("" if selector == "" else " "+selector), shell=True)
