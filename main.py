from window import Window
from maze import Maze

def main():
    win = Window(800, 600)
    num_cols = 5
    num_rows = 6
    maze = Maze(10, 10, num_rows, num_cols, 40, 40, win)
    maze.solve()
    win.wait_for_close()

main()
