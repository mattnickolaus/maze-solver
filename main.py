from graphics import *
from cell import Cell
from maze1 import Maze

def main():
    win = Window(800, 600)

    maze = Maze(50, 50, 6, 6, 50, 50, win, 10)
    
    win.wait_for_close()

if __name__ == "__main__":
    main()
