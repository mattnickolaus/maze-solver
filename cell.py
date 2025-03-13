from graphics import Line, Point


class Cell():
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        # Points
        point_top_left = Point(x1, y1)
        point_top_right = Point(x2, y1)
        point_bottom_left = Point(x1, y2)
        point_bottom_right = Point(x2, y2)

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

    def draw_move(self, to_cell, undo=False):
        color = "gray"
        if not undo:
            color = "red" 
        middle_from = Point(((self._x2 - self._x1)/2) + self._x1, ((self._y2 - self._y1)/2) + self._y1) 
        print(f"{middle_from.x}, {middle_from.y}")
        middle_to = Point(((to_cell._x2 - to_cell._x1)/2) + to_cell._x1, ((to_cell._y2 - to_cell._y1)/2) + to_cell._y1)
        print(f"{middle_to.x}, {middle_to.y}")
        line_between = Line(middle_from, middle_to)
        self._win.draw_line(line_between, color)
        print("drawn")

