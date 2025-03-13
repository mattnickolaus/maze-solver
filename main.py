from graphics import *
from cell import Cell

def main():
    win = Window(800, 600)

    c1 = Cell(win)
    c1.has_top_wall = False
    c1.has_bottom_wall = False
    c1.draw(50, 50, 100, 100)

    c2 = Cell(win)
    c2.has_top_wall = False
    c2.has_bottom_wall = False
    c2.draw(50, 100, 100, 150)

    c3 = Cell(win)
    c3.has_top_wall = False
    c3.has_right_wall = False
    c3.draw(50, 150, 100, 200)

    c4 = Cell(win)
    c4.has_top_wall = False
    c4.has_left_wall = False
    c4.draw(100, 150, 150, 200)

    c1.draw_move(c2, False)
    c2.draw_move(c3)
    c3.draw_move(c4)
    
    win.wait_for_close()

if __name__ == "__main__":
    main()
