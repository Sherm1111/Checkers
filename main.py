##################################
# IMPORTS
##################################

import #pieces, board, movement, player
from tkinter import *

##################################
# MAIN
##################################
# dimensions of board for pi screen
#WIDTH = 
#HEIGHT = 

# create the window
window = Tk()
#window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("CHECKERS")

# create an instance of board
b1 = Board(window)

# render the GUI in the mainloop
window.mainloop()

# create players 1 and 2
p1 = Player(0)
p2 = Player(1)
