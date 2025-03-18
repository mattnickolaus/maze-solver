from graphics import *
from cell import Cell
from maze1 import Maze

def main():
    win = Window(800, 600)

    maze_cols = 10
    maze_rows = 10
    
    cell_size = 50
    pos_x = (800 / 2) - (maze_cols * cell_size * .5) # centers horizontally
    pos_y = (600 / 2) - (maze_rows * cell_size * .5) # centers vertically
    maze = Maze(pos_x, pos_y, maze_cols, maze_rows, cell_size, cell_size, win)

    maze.solve()
    
    win.wait_for_close()

if __name__ == "__main__":
    main()
