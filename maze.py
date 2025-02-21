from cell import Cell
from window import Window
import time

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
        win: Window,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []

    def _create_cells(self):
        x1 = self.x1
        y1 = self.y1

        for _ in range(self.num_cols):
            cell_column = []
            y1 = self.y1
            for _ in range(self.num_rows):
                cell = Cell(self.win)
                cell._x1 = x1
                cell._y1 = y1

                cell_column.append(cell)
                y1 += self.cell_size_y
            self._cells.append(cell_column)
            x1 += self.cell_size_x

        for j, column in enumerate(self._cells):
            for i, cell in enumerate(column):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        x_pos = self.x1 + (j * self.cell_size_x)
        y_pos = self.y1 + (i * self.cell_size_y)
        self._cells[j][i].draw(x_pos, y_pos, x_pos + self.cell_size_x, y_pos + self.cell_size_y)

        self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)
