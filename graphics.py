from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("maze-solver")
        self.canvas = Canvas(self.__root, width=width, height=height)
        self.canvas.pack()
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
        print("Window closed...")
            
    def close(self):
        self.running = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2
        )

class Cell():
    def __init__(self, has_left_wall, has_right_wall, has_top_wall, has_bottom_wall, x1, y1, x2, y2, win):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win

    def draw(self):
        # Points
        point_top_left = Point(self._x1, self._y1)
        point_top_right = Point(self._x2, self._y1)
        point_bottom_left = Point(self._x1, self._y2)
        point_bottom_right = Point(self._x2, self._y2)

        # Create walls of cell (lines)
        left_wall = Line(point_top_left, point_bottom_left)
        right_wall = Line(point_top_right, point_bottom_right)
        top_wall = Line(point_top_left, point_top_right)
        bottom_wall = Line(point_bottom_left, point_bottom_right)


        # Draw walls
        if self.has_left_wall:
            self._win.draw_line(left_wall, "black")
        if self.has_right_wall:
            self._win.draw_line(right_wall, "black")
        if self.has_top_wall:
            self._win.draw_line(top_wall, "black")
        if self.has_bottom_wall:
            self._win.draw_line(bottom_wall, "black")


