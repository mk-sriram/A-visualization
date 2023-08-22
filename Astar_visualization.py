import pygame
import math
from queue import PriorityQueue


WIDTH = 900 
WIN = pygame.display.set_mode((WIDTH, WIDTH))

pygame.display.set_caption("A* path Finding Algorithm")

#color 
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

#functions to create the spot grid 

class Spot:  #singular spot and its attributes 
    def __init__(self, row , col, width, total_rows): 
        self.row = row
        self.col = col 
        self.x = row * width 
        self.y = col * width
        self.color = WHITE 
        self.neighbors = [] 
        self.width = width 
        self.total_rows = total_rows

    #functions to retrieve position
    def get_position(self):
        return self.row, self.col # returns the y,x position as a iteratable 

    #checking if the 
    def is_closed(self):
        if self.color == RED:
            return True
        else:
            return False
    def is_open(self):
        if self.color == GREEN:
            return True
        else:
            return False
    
    def is_barrier(self):
        return self.color == BLACK
    def is_start(self):
        return self.color == ORANGE
    def is_end(self):
        return self.color == PURPLE
    def reset(self):
        self.color == WHITE

    ##Functions to alter the values 
    def make_closed(self):
        self.color == RED
    def make_open(self):
        self.color == GREEN
    def make_barrier(self):
        self.color == BLACK
    def make_start(self):
        self.color == ORANGE
    def make_end(self):
        self.color == BLACK
    def make_path(self):
        self.color == PURPLE
    
    #function to draw the lines
    def draw(self, win):
        pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.width))
    
    def update_neighbors(self,grid):
        pass
    def __lt__(self, other): #less than function 
        #handling if the comparing two spots together, comparing one spot to another spot
        return False
    
def h(p1,p2): #Heuristic Function ( manhattan distance )
    x1,y1 = p1
    x2,y2 = p2 

    return abs(x1 - x2 ) + abs(y1 - y2)

def make_grid(rows,width):
    grid = []
    gap = width//rows ## changes depending on the size of the grid you want 

    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i,j,gap,rows)

            grid[i].append(spot)
    return grid 


def draw_grid(win,rows, width):
    gap = width // rows 
    for i in range (rows):
        pygame.draw.line(win , GREY, (0, i*gap), (width, i* gap))

        for j in range(rows):
            pygame.draw.line(win , GREY, ( j*gap ,0), (j* gap, width))

def draw(win, grid, rows, width):
    win.fill(WHITE) #fills the canvas with white each time and then redraws the points 
    for row in grid:
        for spot in row:
            spot.draw(win) # draws a white spot ( default color in class)
    
    draw_grid(win,rows,width)
    pygame.display.update() #tells pygame to update the canvas 
def mouse_pos()