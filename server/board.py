"""
State of the board
"""


class Board(object):
    ROWS = COLS = 90

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
        try:
            ngB = [(x, y)] + self.get_neighbour(x, y)
            for x, y in ngB:
                if 0 <= x <= self.COLS and 0 <= y <= self.ROWS:
                    self.data[y][x] = color
        except IndexError:
            pass

    def get_neighbour(self, x, y):
        # TODO change the number of associated pixels clicked if it looks too bad
        return [
            (x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
            (x - 1, y), (x + 1, y),
            (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)
        ]

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
