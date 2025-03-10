from graphics import *

def main():
    win = Window(800, 600)

    # Cell 1
    cell1 = Cell(True, True, False, False, 20, 20, 80, 80, win)
    cell2 = Cell(True, False, False, True, 20, 80, 80, 140, win)
    cell1.draw()
    cell2.draw()

    
    win.wait_for_close()

if __name__ == "__main__":
    main()
