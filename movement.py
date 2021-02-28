from restrictions import *
from whichroom import *
from board import *
from tkinter import *
import restrictions
from GUI import *

root = tk()

def movement():
    moveto_gui_label = Label(root, text = "Which way do you want to move:- ")
    moveto_gui_input = Entry(root, text = "Enter the direction ")
    moveto_gui_label.pack()
    moveto_gui_input.pack()
    moveto = moveto_gui_input.get()
    global pos
    global x
    global y
    if moveto == "mr" :
            
        moveright()
        current_room(restrictions.pos)      
    elif moveto == "ml" :
            
        moveleft()
        current_room(restrictions.pos) 
    elif moveto == "mu" :
       moveup()     
       current_room(restrictions.pos)     
    
    elif moveto == "md" :
        movedown()  
        current_room(restrictions.pos)    
    else:
        moveto_gui_invalid = Label(root,text = "invalid move")    
        moveto_gui_invalid.pack()

#test loop

#movement()





root.mainloop()