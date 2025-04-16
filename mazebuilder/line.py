from tkinter import Canvas



class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, start: Point, end: Point):
        self.__start_point = start
        self.__end_point = end

    def draw(self, canvas: Canvas, fill_color="black"):
        canvas.create_line(self.__start_point.x, self.__start_point.y, self.__end_point.x, self.__end_point.y, fill=fill_color, width=2)

class Cell:
    def __init__(self, window = None):
        self.__x1 = None
        self.__x2 = None
        self.__y1 = None
        self.__y2 = None
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False

        self.__win = window

    def draw(self, x1, y1, x2, y2, fill_color: str):
        if not self.__win:
            return
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        top_left = Point(self.__x1, self.__y1)
        top_right = Point(self.__x2, self.__y1)
        bottom_right = Point(self.__x2, self.__y2)
        bottom_left = Point(self.__x1, self.__y2)

        void = "#d9d9d9"

        self.__win.draw_line(Line(top_left, bottom_left), fill_color if self.has_left_wall else void)
        self.__win.draw_line(Line(top_right, bottom_right), fill_color if self.has_right_wall else void)
        self.__win.draw_line(Line(top_left, top_right), fill_color if self.has_top_wall else void)
        self.__win.draw_line(Line(bottom_left, bottom_right), fill_color if self.has_bottom_wall else void)

    def draw_move(self, to_cell, undo=False):
        half_length = abs(self.__x2 - self.__x1) // 2
        x_center = half_length + self.__x1
        y_center = half_length + self.__y1

        half_length2 = abs(to_cell.__x2 - to_cell.__x1) // 2
        x_center2 = half_length2 + to_cell.__x1
        y_center2 = half_length2 + to_cell.__y1

        line = Line(Point(x_center, y_center), Point(x_center2, y_center2))

        if undo:
            self.__win.draw_line(line, "grey")
        else:
            self.__win.draw_line(line)




