from window import Window
from maze import Maze

def main():
    win = Window(800, 600)

    maze = Maze(1, 1, 10, 10, 36, 36, win)
    maze._create_cells()

    win.wait_for_close()

main()


