#!/usr/bin/python
#
# http://www.tutorialspoint.com/python/python_command_line_arguments.htm
# http://effbot.org/zone/tkinter-callbacks.htm
# http://zetcode.com/gui/tkinter/layout/

import sys, getopt, os, tkinter
from subprocess import call

class MyGUI:
    def __init__(self):
    
        self._baseDir = '/getlab/dpb6/repos/pygui/4V1c/'
        self._activePassive = 'Active'
        self._focus = 'Foc_20mm'

        os.chdir(os.path.join(self._baseDir,self._activePassive,self._focus))
        print(os.getcwd())

        command_list = ['Foc_20mm','Foc_25mm','Foc_30mm','Foc_35mm','Foc_40mm']

        self.__top=tkinter.Tk()
        
        # Initialize an empty button array
        btn=[]
        # Add a button for each item in the command list
        for i in range(len(command_list)):
            btn.append(tkinter.Button(self.__top,text=str(command_list[i]), command=lambda btn_value=command_list[i]:self.foc_callback(btn_value)))
            # Put each button in a new row, in one column
            btn[-1].grid(row=0, column=i)

        btn.append(tkinter.Button(self.__top,text='Active/Passive', command=lambda:self.activepassive_callback()))
        btn[-1].grid(row=1, column=0, columnspan=2, sticky=tkinter.W)

        btn.append(tkinter.Button(self.__top,text='Go!', command=lambda:self.go_callback()))
        btn[-1].grid(row=1, column=1, columnspan=len(command_list)-1, sticky=tkinter.E)

        lbl = []
        lbl.append(tkinter.Label(self.__top, text="CURDIR:"))
        lbl[-1].grid(row=2, column=0)

        self.entryHandle = tkinter.Label(self.__top, text= os.path.join(self._activePassive,self._focus))
        self.entryHandle.grid(row=2, column=1, columnspan=2)

        self.__top.mainloop()

    def activepassive_callback(self):

        if 'Active' in self._activePassive:
            self._activePassive = 'Passive'
            os.chdir(os.path.join(self._baseDir,self._activePassive,self._focus))
            print(os.getcwd())
        elif 'Passive' in self._activePassive:
            self._activePassive = 'Active'
            os.chdir(os.path.join(self._baseDir,self._activePassive,self._focus))
            print(os.getcwd())

        self.entryHandle.config(text=os.path.join(self._activePassive,self._focus))
        
    def foc_callback(self,btn_value):

        if 'Foc' in btn_value:
            self._focus = btn_value
            os.chdir(os.path.join(self._baseDir,self._activePassive,self._focus))
            print(os.getcwd())

        self.entryHandle.config(text=os.path.join(self._activePassive,self._focus))

    def go_callback(self):
        if 'Active' in self._activePassive:
            call(["python", "grab_TTE_Mixed.py"])
            print("grab_TTE_Mixed")
        elif 'Passive' in self._activePassive:
            call(["python", "grab_TTE_All.py"])
            print("grab_TTE_All")


        self.entryHandle.config(text=os.path.join(self._activePassive,self._focus))

if __name__ == "__main__":
    # Strip off automatic first argument (sys.argv[0] is the program ie. script btn_value)
    myGUI = MyGUI()