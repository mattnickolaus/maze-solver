import unittest
from maze1 import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

        self.assertEqual(
                len(m1._cells),
                num_cols,
        )

        self.assertEqual(
                len(m1._cells[0]),
                num_rows,
        )

    def test_maze_larger_cells(self):
        num_cols = 16
        num_rows = 20
        m1 = Maze(0, 0, num_rows, num_cols, 20, 20)

        self.assertEqual(
                len(m1._cells),
                num_cols,
        )

        self.assertEqual(
                len(m1._cells[0]),
                num_rows,
        )

    def test_break_entrance_and_exit(self):
        num_cols = 16
        num_rows = 20
        m1 = Maze(0, 0, num_rows, num_cols, 20, 20)

        m1._break_entrance_and_exit()
        start = m1._cells[0][0]
        end = m1._cells[num_cols - 1][num_rows - 1]

        self.assertEqual(False, start.has_top_wall)
        self.assertEqual(False, end.has_bottom_wall)

    def test_reset_visited_after_maze(self):
        num_cols = 16
        num_rows = 20
        m1 = Maze(0, 0, num_rows, num_cols, 20, 20)
        
        start = m1._cells[0][0]
        middle = m1._cells[num_cols // 2][num_rows // 2]
        end = m1._cells[num_cols - 1][num_rows - 1]

        self.assertEqual(False, start.visited)
        self.assertEqual(False, middle.visited)
        self.assertEqual(False, end.visited)


if __name__ == "__main__":
    unittest.main()
