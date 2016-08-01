#!/usr/bin/python
#
# http://www.tutorialspoint.com/python/python_command_line_arguments.htm
# http://effbot.org/zone/tkinter-callbacks.htm
# http://stackoverflow.com/questions/17125842/changing-the-text-on-a-label
# http://stackoverflow.com/questions/29828477/how-to-change-tkinter-label-text-on-button-press
# http://stackoverflow.com/questions/4906977/access-environment-variables-from-python
# http://askubuntu.com/questions/58814/how-do-i-add-environment-variables

import sys, getopt, os, tkinter, datetime
from subprocess import call

class MyGUI:
    def __init__(self):
    
        # These attibutes contain the parts of the path
        # Look for env var 'TTEBASEDIR' which should be created in Windows or Linux
        self.baseDir = os.getenv('TTEBASEDIR', '/getlab/dpb6/repos/pygui/4V1c/')
        self.activePassive = 'Passive'
        self.focus = 'Foc_20mm'

        # Get the starting directory where a logfile can be written
        self.startdir = os.getcwd()

        # Open a logfile and append new commmands
        self.f = open('logfile.txt', 'a')


        # Change to the default directory
        os.chdir(os.path.join(self.baseDir,self.activePassive,self.focus))

        # List of focal zones, could be auto-discovered and populated
        focus_list = ['Foc_20mm','Foc_25mm','Foc_30mm','Foc_35mm','Foc_40mm','Foc_45mm','Foc_50mm','Foc_55mm','Foc_60mm','Foc_65mm','Foc_70mm','Foc_75mm','Foc_80mm','Foc_85mm','Foc_90mm']

        self.top=tkinter.Tk()
        
        # Initialize an empty button array
        btn=[]
        i=0
        # Add a button for each item in the command list
        for rw in range(3):
            for col in range(5):
                btn.append(tkinter.Button(self.top,text=str(focus_list[i]), command=lambda btn_value=focus_list[i]:self.foc_callback(btn_value)))
                # Put each button in a new column, in one row
                btn[-1].grid(row=rw, column=col)
                i+=1

        rw+=1
        # Add a button to switch between Active and Passive Sequences
        btn.append(tkinter.Button(self.top,text='Active/Passive', command=lambda:self.activepassive_callback()))
        btn[-1].grid(row=rw, column=0, columnspan=2, sticky=tkinter.W)

        # Add a button for GO
        self.go_btn = tkinter.Button(self.top,text='Go!', command=lambda:self.go_callback(), bg='green')
        self.go_btn.grid(row=rw, column=1, columnspan=int(len(focus_list)/3)-1, sticky=tkinter.E)

        rw+=1
        # Add a Label for curdir statusbar on the GUI
        self.curdirLabel = tkinter.Label(self.top, text="CURDIR: "+os.path.join(self.activePassive,self.focus))
        self.curdirLabel.grid(row=rw, column=0, columnspan=2, sticky=tkinter.W)

        self.top.mainloop()

    def activepassive_callback(self):
        # Toggle the value of the attribute
        if 'Active' in self.activePassive:
            self.activePassive = 'Passive'
            # Update the GO button color
            self.go_btn.configure(bg = "green")

        elif 'Passive' in self.activePassive:
            self.activePassive = 'Active'
            # Update the GO button color
            self.go_btn.configure(bg = "red")

        # Change the current directory
        os.chdir(os.path.join(self.baseDir,self.activePassive,self.focus))

        # Update the statusbar on the GUI
        self.curdirLabel.config(text="CURDIR: "+os.path.join(self.activePassive,self.focus))

        
    def foc_callback(self,btn_value):
        # Update the value of the attribute
        self.focus = btn_value

        # Change the current directory
        os.chdir(os.path.join(self.baseDir,self.activePassive,self.focus))

        # Update the statusbar on the GUI
        self.curdirLabel.config(text="CURDIR: "+os.path.join(self.activePassive,self.focus))

    def go_callback(self):
        # Set the filename to call
        if 'Active' in self.activePassive:
            filename = 'grab_TTE_Mixed.py'
        elif 'Passive' in self.activePassive:
            filename = 'grab_TTE_All.py'

        # Call the script
        call(['python',filename])

        # Print to log
        print(str(datetime.datetime.now())+" "+os.path.join(self.activePassive,self.focus,filename), file=self.f)

        # Update the statusbar on the GUI
        self.curdirLabel.config(text="CURDIR: "+os.path.join(self.activePassive,self.focus))

if __name__ == "__main__":
    myGUI = MyGUI()