from window import Window
from maze import Maze

def main():
    win = Window(800, 600)
    num_cols = 5
    num_rows = 6
    maze = Maze(0, 0, num_rows, num_cols, 20, 20, win)

    win.wait_for_close()

main()


