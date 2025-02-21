from window import Line, Point


class Cell:
    def __init__(self, win=None):
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
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)

    def draw_move(self, to_cell, undo=False):
        start_point = None
        end_point = None
        line = None

        if self._x1 and self._x2 and self._y1 and self._y2 != None:
            self.center_x = (self._x1 + self._x2) / 2
            self.center_y = (self._y1 + self._y2) / 2

            start_point = Point(self.center_x, self.center_y)

        if to_cell._x1 and to_cell._x2 and to_cell._y1 and to_cell._y2 != None:
            to_cell_center_x = (to_cell._x1 + to_cell._x2) / 2
            to_cell_center_y = (to_cell._y1 + to_cell._y2) / 2

            end_point = Point(to_cell_center_x, to_cell_center_y)
        

        if undo == False and start_point != None and end_point != None:
            line = Line(start_point, end_point)
            self._win.draw_line(line, "red")
        if undo == True and start_point != None and end_point != None:
            line = Line(start_point, end_point)
            self._win.draw_line(line, "gray")

