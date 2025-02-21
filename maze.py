from cell import Cell
import time, random

frame = 0

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
        seed=None,
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
        self.seed = seed
        if seed is not None:
            random.seed(seed)
        self._break_walls_r(0, 0)

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
            time.sleep(0.25)

    def _break_entrance_and_exit(self):
        first_cell = self._cells[0][0]
        first_cell.has_left_wall = False
        self._draw_cell(0, 0)

        last_row_index = len(self._cells[0]) - 1
        last_column_index = len(self._cells) - 1

        last_cell = self._cells[last_column_index][last_row_index]
        last_cell.has_bottom_wall = False
        self._draw_cell(last_row_index, last_column_index)

    def _break_walls_r(self, row, column):
        boolean_list = []
        for columns in self._cells:
            for cell in columns:
                boolean_list.append(cell.visited)

        if all(boolean_list):
            return
        
        current = self._cells[column][row]
        print(f"starting at {current}")
        current.visited = True
        print("current marked visited = True")
        above = None
        right = None
        below = None
        left = None
        chosen_row = None
        chosen_column = None

        while True:
            global frame
            frame += 1
            print(f"beginning of while loop {frame}")
            need_visit = []
            if row > 0:
                above = self._cells[column][row - 1]
                if above.visited is not True:
                    need_visit.append(above)
                    print("above added")
                    print(need_visit)
            if column > 0:
                left = self._cells[column - 1][row]
                if left.visited is not True:
                    need_visit.append(left)
                    print("left added")
                    print(need_visit)
            if row < len(self._cells[0]) - 1:
                below = self._cells[column][row + 1]
                if below.visited is not True:
                    need_visit.append(below)
                    print("below added")
                    print(need_visit)
            if column < len(self._cells) - 1:
                right = self._cells[column + 1][row]
                if right.visited is not True:
                    need_visit.append(right)
                    print("right added")
                    print(need_visit)

            print(f"final need_visit is {need_visit}")

            if len(need_visit) is 0: 
                self._draw_cell(row, column)
                return
            else:
                choice = random.choice(need_visit)
                need_visit = []
                print(f"choice is {choice}")
                
                if choice is above:
                    current.has_top_wall = False
                    self._draw_cell(row, column)
                    above.has_bottom_wall = False
                    self._draw_cell(row - 1, column)
                    chosen_row = row - 1
                    chosen_column = column
                if choice is left:
                    current.has_left_wall = False
                    self._draw_cell(row, column)
                    left.has_right_wall = False
                    self._draw_cell(row, column - 1)
                    chosen_row = row
                    chosen_column = column - 1
                if choice is below:
                    current.has_bottom_wall = False
                    self._draw_cell(row, column)
                    below.has_top_wall = False
                    self._draw_cell(row + 1, column)
                    chosen_row = row + 1
                    chosen_column = column
                if choice is right:
                    current.has_right_wall = False
                    self._draw_cell(row, column)
                    right.has_left_wall = False
                    self._draw_cell(row, column + 1)
                    chosen_row = row
                    chosen_column = column + 1
            frame += 1
            print(f"end of first while loop pre-recursion {frame}")
            self._break_walls_r(chosen_row, chosen_column)
            frame += 1
            print(f"after recursion {frame}")

    def _reset_cells_visited(self):
        for columns in self._cells:
            for cells in columns:
                cells.visited = False
