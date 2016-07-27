#!/usr/bin/python
#
# http://www.tutorialspoint.com/python/python_command_line_arguments.htm
# http://effbot.org/zone/tkinter-callbacks.htm
# http://stackoverflow.com/questions/17125842/changing-the-text-on-a-label
# http://stackoverflow.com/questions/29828477/how-to-change-tkinter-label-text-on-button-press

import sys, getopt, os, tkinter
from subprocess import call

class MyGUI:
    def __init__(self):
    
        # These attibutes contain the parts of the path
        self.baseDir = '/getlab/dpb6/repos/pygui/4V1c/'
        self.activePassive = 'Active'
        self.focus = 'Foc_20mm'

        # Change to the default directory
        os.chdir(os.path.join(self.baseDir,self.activePassive,self.focus))

        # List of focal zones, could be auto-discovered and populated
        command_list = ['Foc_20mm','Foc_25mm','Foc_30mm','Foc_35mm','Foc_40mm']

        self.top=tkinter.Tk()
        
        # Initialize an empty button array
        btn=[]
        # Add a button for each item in the command list
        for i in range(len(command_list)):
            btn.append(tkinter.Button(self.top,text=str(command_list[i]), command=lambda btn_value=command_list[i]:self.foc_callback(btn_value)))
            # Put each button in a new column, in one row
            btn[-1].grid(row=0, column=i)

        # Add a button to switch between Active and Passive Sequences
        btn.append(tkinter.Button(self.top,text='Active/Passive', command=lambda:self.activepassive_callback()))
        btn[-1].grid(row=1, column=0, columnspan=2, sticky=tkinter.W)

        # Add a button for GO
        btn.append(tkinter.Button(self.top,text='Go!', command=lambda:self.go_callback()))
        btn[-1].grid(row=1, column=1, columnspan=len(command_list)-1, sticky=tkinter.E)

        # Add a Label for 11
        self.curdirLabel = tkinter.Label(self.top, text="CURDIR: "+os.path.join(self.activePassive,self.focus))
        self.curdirLabel.grid(row=2, column=0, columnspan=2, sticky=tkinter.W)

        self.top.mainloop()

    def activepassive_callback(self):

        if 'Active' in self.activePassive:
            self.activePassive = 'Passive'
            os.chdir(os.path.join(self.baseDir,self.activePassive,self.focus))
            print(os.getcwd()) # Can change these to print to a timestamped logfile
        elif 'Passive' in self.activePassive:
            self.activePassive = 'Active'
            os.chdir(os.path.join(self.baseDir,self.activePassive,self.focus))
            print(os.getcwd()) # Can change these to print to a timestamped logfile
            
        self.curdirLabel.config(text="CURDIR: "+os.path.join(self.activePassive,self.focus))
        
    def foc_callback(self,btn_value):

        if 'Foc' in btn_value:
            self.focus = btn_value
            os.chdir(os.path.join(self.baseDir,self.activePassive,self.focus))
            print(os.getcwd()) # Can change these to print to a timestamped logfile
            
        self.curdirLabel.config(text="CURDIR: "+os.path.join(self.activePassive,self.focus))

    def go_callback(self):
        if 'Active' in self.activePassive:
            call(["python", "grab_TTE_Mixed.py"])
            print("grab_TTE_Mixed") # Can change these to print to a timestamped logfile
        elif 'Passive' in self.activePassive:
            call(["python", "grab_TTE_All.py"])
            print("grab_TTE_All") # Can change these to print to a timestamped logfile

        self.curdirLabel.config(text="CURDIR: "+os.path.join(self.activePassive,self.focus))

if __name__ == "__main__":
    myGUI = MyGUI()