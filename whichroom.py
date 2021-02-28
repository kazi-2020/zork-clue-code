from board import *
from tkinter import *

root = Tk()

present_room=" this room"
def current_room(position):
    
    global present_room
    
    if position in storage:
        player_location_label = Label(root,text = "Player is in storage.")
        player_location_label.pack()
        #print("Player is in storage.")
        present_room="storage"
        
    elif position in study:
        player_location_label = Label(root,text = "Player is in study.")
        player_location_label.pack()
        #print("Player is in study.")
        present_room="study"
    
    elif position in bathroom:
        player_location_label = Label(root,text = "Player is in bathroom.")
        player_location_label.pack()
        #print("Player is in bathroom.")
        present_room="bathroom"
    
    elif position in lib:
        player_location_label = Label(root,text = "Player is in library.")
        player_location_label.pack()
        #print("Player is in library.")
        present_room="lib"
    
    elif position in gallery:
        player_location_label = Label(root,text = "Player is in gallery.")
        player_location_label.pack()
        #print("Player is in gallery.")
        present_room="gallery"
    
    elif position in bed1:
        player_location_label = Label(root,text = "Player is in bedroom 1.")
        player_location_label.pack()
        #print("Player is in bedroom 1.")
        present_room="bed1"
    
    elif position in foyer:
        player_location_label = Label(root,text = "Player is in foyer.")
        player_location_label.pack()
        #print("Player is in foyer.")
        present_room="foyer"
    
    elif position in bed2:
        player_location_label = Label(root,text = "Player is in bedroom 2.")
        player_location_label.pack()
        #print("Player is in bedroom 2.")
        present_room="bed2"
    
    elif position in kitchen:
        player_location_label = Label(root,text = "Player is in kitchen.")
        player_location_label.pack()
        #print("Player is in kitchen.")
        present_room="kitchen"
    
    else:
        player_location_label = Label(root,text = "Player is in hallway")
        player_location_label.pack()
        #print("Player is in hallway")
        present_room="hallway"





root.mainloop()