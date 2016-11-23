from collections import deque
from termcolor import colored

from Child import Child

# define board size
board_size_width = 18
board_size_height = 13

# initialize expored array
explored = []

# define destinations array
x_destinations = []
y_destinations = []

# set the solution object
solution = False

# printing variables
EMPTY = ' '
GATE = colored('#', 'red')
XLINE = '-'
YLINE = '|'
BEGIN = colored('#', 'green')
END = colored('#', 'green')

class Bfs_function:

    # standard initializer with board
    def __init__(self, board):
        self.board = board
        self.queue = deque()

        # gate positions
        gates_x = [12,1,6,10,15,3,12,14,12,8,1,4,11,16,13,16,2,6,9,11,15,1,2,9,1]
        gates_y = [11,1,1,1,1,2,2,2,3,4,5,5,5,5,7,7,8,8,8,8,8,9,10,10,11]

        # netlist start and end separately
        startcoordinates = [23,5,1,15,3,7,23,22,15,20,15,13,19,22,10,11,3,2,3,20,16,19,3,15,6,7,9,22,10]
        endcoordinates = [4,7,0,21,5,13,8,13,17,10,8,18,2,11,4,24,15,20,4,19,9,5,0,5,14,9,13,16,7]

        # set emty x and y coordinates
        x = []
        y = []

        # loopt through all the assigned element in the list
        # and append all the (start & end) locations into the list
        for i in range(0, 24):
                 explored.append((gates_x[i],gates_y[i]))
                 self.board.set_value(GATE, gates_x[i], gates_y[i])

                 x.append(gates_x[startcoordinates[i]])
                 y.append(gates_y[startcoordinates[i]])

                 x_destinations.append(gates_x[endcoordinates[i]])
                 y_destinations.append(gates_y[endcoordinates[i]])

        # set the first startchilderen
        self.makechildren(x[0], y[0])

        # removed the end coordinates [x,y]
        explored.pop(4)

    # find and calculate the childeren
    def makechildren(self, x,y):

        children = [(x-1, y),(x,y - 1),(x,y + 1),(x + 1,y)]

        for child in children:
            if child[0] >= 0 and child[1] >= 0 and child[0] <= board_size_width and child[1] <= board_size_height:
                if not child in explored:

                    self.queue.append(child)

                    explored.append(child)

                    self.print_child_state(child)

        if child[0] == x_destinations[0] and child[1] == y_destinations[0]:

            solution = True
            return solution
        else:
            solution = False
            return solution

    #
    def pop_queue_left(self):
        self.queue.popleft()

    #
    def print_child_state(self, child):

        self.board.set_value(colored('*', 'blue'), child[0], child[1])
        self.board.print_board()
