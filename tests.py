import unittest
from maze import Maze

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
    
    def test_maze_big(self):
        num_cols = 100
        num_rows = 200
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
                len(m1._cells),
                num_cols,
        )
        self.assertEqual(
                len(m1._cells[0]),
                num_rows,
        )

    def test_reset_visited(self):
        m1 = Maze(0, 0, 5, 5, 10, 10)
        m1._reset_cells_visited()
        self.assertEqual(
                m1._cells[0][0].visited == False,
                True,
        )

if __name__ == "__main__":
    unittest.main()

