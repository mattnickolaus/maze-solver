from cell import Cell
import time
import random

class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None,
        ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y 
        self._win = win

        if seed is not None:
            self.seed = random.seed(seed)
        
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)

    
    def _create_cells(self):
        self._cells = []
        for i in range(self.num_cols):
            rows = []
            for j in range(self.num_rows):
                new_cell = Cell(self._win)
                rows.append(new_cell)
            self._cells.append(rows)

        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        x1 = self.x1 + (self.cell_size_x * i)
        x2 = self.x1 + (self.cell_size_x * i) + self.cell_size_x
        y1 = self.y1 + (self.cell_size_y * j)
        y2 = self.y1 + (self.cell_size_y * j) + self.cell_size_y

        cell = self._cells[i][j]
        cell.draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        start = self._cells[0][0]
        end = self._cells[self.num_cols - 1][self.num_rows - 1]

        start.has_top_wall = False
        end.has_bottom_wall = False

        self._draw_cell(0, 0)
        self._draw_cell(self.num_cols - 1, self.num_rows -1)

    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]
        current_cell.visited = True

        while True:
            possible_to_visit = []

            above = self._cells[i][j - 1]
            below = self._cells[i][j + 1]
            left = self._cells[i - 1][j]
            right = self._cells[i + 1][j]
            if j > 0 and not above.visited:
                possible_to_visit.append((i, j - 1))
            if j < self.num_rows - 1 and not below.visited:
                possible_to_visit.append((i, j + 1))
            if i > 0 and not left.visited:
                possible_to_visit.append((i - 1, j))
            if i < self.num_cols  - 1 and not right.visited:
                possible_to_visit.append((i + 1, j))

            if len(possible_to_visit) == 0:
                self._draw_cell(i, j)
                return

            rand_index = random.randrange(len(possible_to_visit))
            indicies = possible_to_visit[rand_index]

            to_i = indicies[0]
            to_j = indicies[1]
            to_cell = self._cells[to_i][to_j]

            if to_j == j + 1:
                # its below
                current_cell.has_bottom_wall = False
                to_cell.has_top_wall = False
                self._draw_cell(i, j)
                self._draw_cell(to_i, to_j)
            if to_j == j - 1:
                # its above
                current_cell.has_top_wall = False
                to_cell.has_bottom_wall = False
                self._draw_cell(i, j)
                self._draw_cell(to_i, to_j)
            if to_i == i - 1:
                # its left
                current_cell.has_left_wall = False
                to_cell.has_right_wall = False
                self._draw_cell(i, j)
                self._draw_cell(to_i, to_j)
            if to_i == i + 1:
                # its right
                current_cell.has_right_wall = False
                to_cell.has_left_wall = False
                self._draw_cell(i, j)
                self._draw_cell(to_i, to_j)

        self._break_walls_r(to_i, to_j)        
