"""
Represents the board object for the game.
"""
import pygame
import random


class Board(object):
    ROWS = COLS = 90
    COLORS = {
        0: (255, 255, 255),
        1: (0, 0, 0),
        2: (255, 0, 0),
        3: (0, 255, 0),
        4: (0, 0, 255),
        5: (255, 255, 0),
        6: (255, 142, 0),
        7: (165, 45, 45),
        8: (128, 0, 128)
    }

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.WIDTH = 720
        self.HEIGHT = 720
        self.compressed_board = []
        self.board = self.create_board()
        self.BORDER_THICKNESS = 5

    def create_board(self):
        return [[(255, 255, 255) for _ in range(self.COLS)] for _ in range(self.ROWS)]

    def translate_board(self):
        for y, _ in enumerate(self.compressed_board):
            for x, col in enumerate(self.compressed_board[y]):
                self.board[y][x] = self.COLORS[col]

    def draw(self, win):
        pygame.draw.rect(win, (0, 0, 0), (self.x - self.BORDER_THICKNESS/2, self.y - self.BORDER_THICKNESS/2, self.WIDTH + self.BORDER_THICKNESS, self.HEIGHT + self.BORDER_THICKNESS), self.BORDER_THICKNESS)
        for y, _ in enumerate(self.board):
            for x, col in enumerate(self.board[y]):
                pygame.draw.rect(win, col, (self.x + x*8, self.y + y*8, 8, 8), 0)

    def click(self, x, y):
        """
        none if not in board, otherwise return place clicked on in terms of row and col
        :param x: float
        :param y: float
        :return: (int, int) ir none
        """
        row = int((x - self.x)/8)
        col = int((y - self.y)/8)

        if 0 <= row < self.ROWS and 0 <= col <= self.COLS:
            return row, col

    def update(self, x, y, color, thickness=3):
        try:
            ngB = [(x, y)] + self.get_neighbour(x ,y)
            for x, y in ngB:
                if 0 <= x <= self.COLS and 0 <= y <= self.ROWS:
                    self.board[y][x] = color
        except IndexError:
            pass

    def get_neighbour(self, x, y):
        # TODO change the number of associated pixels clicked if it looks too bad
        return [
            (x-1, y-1), (x, y-1), (x+1, y-1),
            (x-1, y), (x+1, y),
            (x-1, y+1), (x, y+1), (x+1, y+1)
        ]

    def clear(self):
        self.board = self.create_board()
