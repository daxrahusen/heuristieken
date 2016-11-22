import sys

# printing variables
EMPTY = ' '

class Grid:

    # initialize board to empty (val)ues for (col)umns and (row)s
    def __init__(self, row, col):
        self.width = col
        self.height = row
        self.total_length = 0

        # initialize 2D Array to EMPTY
        self._grid = []
        for i in range(self.height + 1):
            self._grid.append([])
            for j in range(self.width + 1):
                self._grid[i].append(EMPTY)

    def set_value(self, value, x, y):
        self._grid[y][x] = value

    def get_value(self, x, y):
        return self._grid[y][x]

    def print_board(self):
        for row in self._grid:
            for item in row:
                sys.stdout.write(item + '   ')
            print('\n')
