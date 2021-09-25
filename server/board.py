"""
State of the board
"""


class Board(object):
    ROWS = COLS = 720

    def __init__(self):
        """
        init board by creating board (all white pixels)
        """
        self.data = self._create_empty_board()

    def update(self, x, y, color):
        """
        updates a single pixel of board
        :param x: int
        :param y: int
        :param color: (int,int,int)
        :return:
        """
        self.data[y][x] = color

    def clear(self):
        """
        clears board
        :return: None
        """
        self.data = self._create_empty_board()

    def _create_empty_board(self):
        """"
        creates new board
        :return: None
        """
        return [[0 for _ in range(self.COLS)] for _ in range(self.ROWS)]

    def fill(self, x, y):
        """
        fills a specific area using recursion
        :param x: int
        :param y: int
        :return: None
        """
        pass

    def get_board(self):
        return self.data
