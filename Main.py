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
FPS = 40

# Main entrance function
def main():

    # initialize empty board
    board = Grid(13, 18)
    bfs = Bfs_function(board)

    while bfs.netlist_counter > 0:

        while True:
            solution = bfs.makechildren(bfs.queue[0][0], bfs.queue[0][1])
            bfs.pop_queue_left()
            if solution == True:
                bfs.queue.clear()
                bfs.netlist_counter -= 1
                bfs.index_gate += 1
                solution = False
                break

            clock.tick(FPS)

        board.clear_path()
        board.add_start_end_gates((bfs.x[bfs.index_gate], bfs.y[bfs.index_gate]), (bfs.x_destinations[bfs.index_gate], bfs.y_destinations[bfs.index_gate]))
        board.print_board()


    # while gate_counter > 0:
        # while solution == True:
            # bfs.makechildren(queue[x-element], queue[y-element])
            # if solution == True:
                # gate_counter--
                # break
        # board.clear_path()
        # board.add_start_end_gates(start_gate, end_gate)
        # board.print_board()

    # while True:
    #     solution = bfs.makechildren(bfs.queue[0][0], bfs.queue[0][1])
    #     bfs.pop_queue_left()
    #     if solution == True:
    #         break
    #
    #     # make delay of 20FSP per seconds
    #     clock.tick(FPS)
    #
    # board.clear_path()
    # board.add_start_end_gates(bfs.get_start_gate(), bfs.get_end_gate())
    # board.print_board()

main()
