from random import choice, randint, random, shuffle
from enum import Enum
import pygame, pgzero, pgzrun, sys

if sys.version_info < (3,6):
    print("This game requies at least version 3.6 of Python. Please download"
          "it from www.python.org")
    sys.exit()

pgzero_version = [int(s) if s.isnumeric() else s
                  for s in pgzero.__version__.split('.')]

if pgzero_version < [1,2]:
    print(f"This game requires at least version 1.2 of Pygame Zero. You are"
          "using version {pgzero.__version__}. Please upgrade using the command"
          "'pip install --upgrade pgzero'")
    sys.exit()

WIDTH = 800
HEIGHT = 480
TITLE = "Cavern"

NUM_ROWS = 18
NUM_COLUMNS = 28

LEVEL_X_OFFSET = 50
GRID_BLOCK_SIZE =25

ANCHOR_CENTER = ("center", "center")
ANCHOR_CENTER_BOTTOM = ("center", "bottom")

LEVELS = [
    ["XXXXX     XXXXXXXX     XXXXX",
     "","","","",
     "  XXXXXXX          XXXXXXX  ",
     "","","",
     "  XXXXXXXXXXXXXXXXXXXXXXXX  ",
     "","","",
     "XXXXXXXXX          XXXXXXXXX",
     "","",""],

    ["XXXX     XXXXXXXXXX     XXXX",
     "","","","",
     "  XXXXXXXXXXXXXXXXXXXXXXXX  ",
     "","","",
     "XXXXXX                XXXXXX",
     "      X              X      ",
     "       X            X       ",
     "        X          X        ",
     "         X        X         ",
     "","",""],

    ["XXXX    XXXX    XXXX    XXXX",
     "","","","",
     "  XXXXXXXX        XXXXXXXX  ",
     "","","",
     "XXXX      XXXXXXXX      XXXX",
     "","","",
     "    XXXXXX        XXXXXX    ",
     "","",""]]

def block(x,y):
    grid_x = (x - LEVEL_X_OFFSET) // GRID_BLOCK_SIZE
    grid_y = y // GRID_BLOCK_SIZE

    if grid_y > 0 and grid_y < NUM_ROWS:
        row = game.grid[grid_y]
        return grid_x >= 0 and grid_x < NUM_COLUMNS and len(row) > 0 and \
            row[grid_x] != " "
    else:
        return False
    
def sign(x):
    return -1 if x < 0 else 1

class CollideActor(Actor):
    def __init__(self, pos, anchor=ANCHOR_CENTER):
        super().__init__("blank", pos, anchor)

    def move(self, dx, dy, speed):
        new_x, new_y = int(self.x), int(self.y)

        for i in range(speed):
            new_x, new_y = new_x + dx, new_y + dy

            if new_x < 70 or new_x > 730:
                return True
            
            if ((dy > 0 and new_y % GRID_BLOCK_SIZE == 0 or 
                 dx > 0 and new_x % GRID_BLOCK_SIZE == 0 or 
                 dx < 0 and new_x % GRID_BLOCK_SIZE == GRID_BLOCK_SIZE-1)
                 and block(new_x, new_y)):
                return True
            
            self.pos = new_x, new_y

        return False
    
    
