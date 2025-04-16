from line import Line, Point, Cell
from maze import Maze
from window import Window


def main():
    num_rows = 15
    num_cols = 15
    margin = 70
    screen_x = 800
    screen_y = 800
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, 10)
    maze.solve()

    win.wait_for_close()

main()