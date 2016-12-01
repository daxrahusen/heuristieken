# import libs
from collections import deque
import sys
import os
import time
import pygame
pygame.init()

# import classes
from Grid import Grid
from Bfs_function import Bfs_function

# define board size
board_size_width = 18
board_size_height = 13

# initialize expored array
explored = []

# initialize deque object
queue = deque()

# initialize pygame time ticker
clock = pygame.time.Clock()

# define destinations array
xdestinations = []
ydestinations = []

# set the solution object
solution = False

# define the Frame Per Seconds
# for animations
FPS = 20

# Main entrance function
def main():

    # initialize empty board
    board = Grid(13, 18)
    bfs = Bfs_function(board)

    while True:
        solution = bfs.makechildren(bfs.queue[0][0], bfs.queue[0][1])
        bfs.pop_queue_left()
        if solution == True:
            break

        # make delay of 20FSP per seconds
        clock.tick(FPS)

    board.print_board()



main()
