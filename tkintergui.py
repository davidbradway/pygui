#!/usr/bin/python
#
# http://www.tutorialspoint.com/python/python_command_line_arguments.htm
# http://effbot.org/zone/tkinter-callbacks.htm

import sys, getopt, os, tkinter
from subprocess import call

baseDir = '/getlab/dpb6/repos/pygui/4V1c/'
activePassive = 'Active'
focus = 'Foc_20mm'


def activepassive_callback():
    global baseDir
    global activePassive
    global focus

    if 'Active' in activePassive:
        activePassive = 'Passive'
        os.chdir(os.path.join(baseDir,activePassive,focus))
        print(os.getcwd())
    elif 'Passive' in activePassive:
        activePassive = 'Active'
        os.chdir(os.path.join(baseDir,activePassive,focus))
        print(os.getcwd())

    
def foc_callback(btn_value):
    global baseDir
    global activePassive
    global focus

    if 'Foc' in btn_value:
        focus = btn_value
        os.chdir(os.path.join(baseDir,activePassive,focus))
        print(os.getcwd())
    

def go_callback():
    global baseDir
    global activePassive
    global focus

    if 'Active' in activePassive:
        call(["python", "grab_TTE_Mixed.py"])
    elif 'Passive' in activePassive:
        call(["python", "grab_TTE_all.py"])

def main(argv):
    global baseDir
    global activePassive
    global focus

    #print('Number of arguments:', len(argv))
    print('Argument List:', str(argv))

    os.chdir(os.path.join(baseDir,activePassive,focus))
    print(os.getcwd())

    # If there are command line options, use those 
    if len(argv) >= 1:
        command_list = argv
    else:
        # Else, use the defaults
        command_list = ['Foc_20mm','Foc_25mm','Foc_30mm','Foc_35mm','Foc_40mm']
    
    top=tkinter.Tk()
    
    # Initialize an empty button array
    btn=[]
    # Add a button for each item in the command list
    for i in range(len(command_list)):
        btn.append(tkinter.Button(top,text=str(command_list[i]), command=lambda btn_value=command_list[i]:foc_callback(btn_value)))
        # Put each button in a new row, in one column
        btn[-1].grid(row=0, column=i)

    btn.append(tkinter.Button(top,text='Active/Passive', command=lambda:activepassive_callback()))
    btn[-1].grid(row=1, column=0, columnspan=2, sticky=tkinter.W)

    btn.append(tkinter.Button(top,text='Go!', command=lambda:go_callback()))
    btn[-1].grid(row=1, column=1, columnspan=4, sticky=tkinter.E)

    lbl = []
    lbl.append(tkinter.Label(top, text="CURDIR:"))
    lbl[-1].grid(row=2, column=0)

    # message = tkinter.StringVar()
    # message.set(os.path.join(activePassive,focus))
    message = 'Static message for now :-('

    entryHandle = []
    entryHandle.append(tkinter.Entry(top, textvariable=message))
    entryHandle[-1].grid(row=2, column=1, columnspan=2)

    top.mainloop()

if __name__ == "__main__":
    # Strip off automatic first argument (sys.argv[0] is the program ie. script btn_value)
    main(sys.argv[1:])