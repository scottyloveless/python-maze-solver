from window import Window
from maze import Maze

def main():
    win = Window(800, 600)
    num_cols = 12
    num_rows = 10
    maze = Maze(0, 0, num_rows, num_cols, 36, 36, win)

    win.wait_for_close()

main()


