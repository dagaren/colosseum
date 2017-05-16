from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from model import File, Rank, Square

class Board(Widget):
    def __init__(self, **kwargs):
        super(Board, self).__init__(**kwargs)
        self.bind(pos = self.draw, size = self.draw)

        self.backgroundColor = (0.5, 0.3, 0.4)
        self.boardColor = (1, 1, 0)
        self.darkSquareColor = (0.5, 0.5, 0.5)
        self.whiteSquareColor = (1, 1, 1)

    def draw(self, *args):
        self.calculate_measures()
        with self.canvas:
            self.canvas.clear()
            self.draw_board()

    def calculate_measures(self):
        self.boardWidth = min(self.size)
        self.boardSize = (self.boardWidth, self.boardWidth)
        boardPositionX = self.pos[0] + self.size[0] /2 - self.boardWidth / 2
        boardPositionY = self.pos[1] + self.size[1] / 2 - self.boardWidth / 2 
        self.boardPosition = (boardPositionX, boardPositionY)
        self.squareWidth = int(self.boardWidth / 8)
        self.squareSize = (self.squareWidth, self.squareWidth)

    def draw_board(self):
        Color(*self.backgroundColor)
        Rectangle(pos = self.pos, size = self.size)

        Color(*self.boardColor)
        Rectangle(pos = self.boardPosition, size = self.boardSize)

        for file in File:
            for rank in Rank:
                self.draw_square(Square.get_square(file, rank))

    def draw_square(self, square):
        squareColor = self.get_square_color(square)
        self.paint_square(square, squareColor)

    def paint_square(self, square, color):
        Color(*color)
        Rectangle(pos = self.get_square_position(square), size = self.squareSize)

    def get_square_position(self, square):
        squarePositionX = self.boardPosition[0] + (square.get_file() * self.squareSize[0])
        squarePositionY = self.boardPosition[1] + (square.get_rank() * self.squareSize[1])

        return (squarePositionX, squarePositionY)

    def get_square_color(self, square):
        return self.darkSquareColor if square.get_rank() % 2 == square.get_file() % 2 else self.whiteSquareColor