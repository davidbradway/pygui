#!/usr/bin/python
#
# http://www.tutorialspoint.com/python/python_command_line_arguments.htm
# http://effbot.org/zone/tkinter-callbacks.htm

import sys, getopt, os, tkinter
from subprocess import call

def callback(name):
    # Maybe make this a switch case with all your imaging cases and scripts?
    print('/getlab/dpb6/repos/pygui/4V1c/'+name)
    os.chdir('/getlab/dpb6/repos/pygui/4V1c/'+name)
    print(os.getcwd())
    if 'Active' in name:
        call(["python", "grab_TTE_Mixed.py"])
    elif 'Passive' in name:
        call(["python", "grab_TTE_all.py"])

def main(argv):
    #print('Number of arguments:', len(argv))
    print('Argument List:', str(argv))

    # If there are command line options, use those 
    if len(argv) >= 1:
        command_list = argv
    else:
        # Else, use the defaults
        command_list = ['Active/Foc_20mm','Active/Foc_25mm','Passive/Foc_20mm','Passive/Foc_25mm']
    
    top=tkinter.Tk()
    
    # Initialize an empty button array
    btn=[]
    # Add a button for each item in the command list
    for i in range(len(command_list)):
        btn.append(tkinter.Button(top,text=str(command_list[i]), command=lambda command_name=command_list[i]:callback(command_name)))
        # Put each button in a new row, in one column
        btn[-1].grid(row=i, column=0)

    top.mainloop()

if __name__ == "__main__":
    # Strip off automatic first argument (sys.argv[0] is the program ie. script name)
    main(sys.argv[1:])