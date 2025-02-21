from cell import Cell
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
        win=None,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()

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

    def _draw_cell(self, row, column):
        x_pos = self.x1 + (column * self.cell_size_x)
        y_pos = self.y1 + (row * self.cell_size_y)
        self._cells[column][row].draw(x_pos, y_pos, x_pos + self.cell_size_x, y_pos + self.cell_size_y)
        
        if self.win is not None:
            self._animate()

    def _animate(self):
        if self.win is not None:
            self.win.redraw()
            time.sleep(0.05)

    def _break_entrance_and_exit(self):
        first_cell = self._cells[0][0]
        first_cell.has_left_wall = False
        self._draw_cell(0, 0)

        last_row_index = len(self._cells[0]) - 1
        last_column_index = len(self._cells) - 1

        last_cell = self._cells[last_column_index][last_row_index]
        last_cell.has_bottom_wall = False
        self._draw_cell(last_row_index, last_column_index)
