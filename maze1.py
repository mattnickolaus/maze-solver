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
        self._cells = []
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y 
        self._win = win

        if seed is not None:
            random.seed(seed)
        
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    
    def _create_cells(self):
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
        if self._win is None:
            return
        x1 = self.x1 + (self.cell_size_x * i)
        x2 = x1 + self.cell_size_x
        y1 = self.y1 + (self.cell_size_y * j)
        y2 = y1 + self.cell_size_y

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

            # left
            if i > 0 and not self._cells[i - 1][j].visited:
                possible_to_visit.append((i - 1, j))
            # right
            if i < self.num_cols  - 1 and not self._cells[i + 1][j].visited:
                possible_to_visit.append((i + 1, j))
            # up
            if j > 0 and not self._cells[i][j - 1].visited:
                possible_to_visit.append((i, j - 1))
            # down
            if j < self.num_rows - 1 and not self._cells[i][j + 1].visited:
                possible_to_visit.append((i, j + 1))

            if len(possible_to_visit) == 0:
                self._draw_cell(i, j)
                return

            rand_index = random.randrange(len(possible_to_visit))
            next_index = possible_to_visit[rand_index]

            # right
            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            # left
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            # down
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            # up
            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False


            self._break_walls_r(next_index[0], next_index[1])        

    def _reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                cell = self._cells[i][j]
                cell.visited = False

    def solve(self):
        return self._solver_r(0, 0)

    def _solver_r(self, i, j):
        self._animate()
        current = self._cells[i][j]
        current.visited = True

        if current == self._cells[self.num_cols - 1][self.num_rows - 1]:
            print("Solved!")
            return True

        #               left        right       up          down
        directions = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]

        for direction in directions:
            exists = (0 <= direction[0] <= (self.num_cols - 1)) and (0 <= direction[1] <= (self.num_rows - 1))
            if exists:
                was_visited = self._cells[direction[0]][direction[1]].visited
                
                # left
                if direction[0] == i - 1:
                    wall = self._cells[i][j].has_left_wall
                    # print(f"Dirction: left, Visited? {was_visited}, Wall? {wall}")
                # right
                if direction[0] == i + 1:
                    wall = self._cells[i][j].has_right_wall
                    # print(f"Dirction: right, Visited? {was_visited}, Wall? {wall}")
                # down
                if direction[1] == j + 1:
                    wall = self._cells[i][j].has_bottom_wall
                    # print(f"Dirction: down, Visited? {was_visited}, Wall? {wall}")
                # up
                if direction[1] == j - 1:
                    wall = self._cells[i][j].has_top_wall
                    # print(f"Dirction: up, Visited? {was_visited}, Wall? {wall}")

                if not was_visited and not wall:
                    current.draw_move(self._cells[direction[0]][direction[1]])

                    found = self._solver_r(direction[0], direction[1])
                    if found:
                        # print("Solved!")
                        return True
                    else:
                        current.draw_move(self._cells[direction[0]][direction[1]], undo=True)
        return False
