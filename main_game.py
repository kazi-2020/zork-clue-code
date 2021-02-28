from board import *
from movement import *
from restrictions import *
from whichroom import *
import whichroom
import sys
from time import sleep
import random
from tkinter import *

print("ZORK-CLUE")
intro="""Welcome to Manor Mansions, the heart of this town. It's the residence of the mayor of this town. \n
Unfortunately the towns mental asylum had a security breach, one of the lunatics got out and killed the mayor's dog with a candle stick.\n
The killer has been caught but cannot be convicted until the murder weapon is found, according to interpol it's still in one of the rooms inside the mansion.\n
Help the mayor's dog get his justice by heping them find the weapon.\n"""
'''
for char in intro:
    sleep(0.05)
    sys.stdout.write(char)
'''




for i in range (1,1500):
    movement()

Tk.mainloop()
