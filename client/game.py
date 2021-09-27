import pygame
from button import Button, TextButton
from board import Board
from top_bar import TopBar
from leaderboard import Leaderboard
from player import Player
from bottom_bar import BottomBar
from chat import Chat
from network import Network


class Game:
    BG = (255, 255, 255)

    def __init__(self, win, connection=None):
        pygame.font.init()
        self.connection = connection
        self.win = win
        self.leaderboard = Leaderboard(50, 125)
        self.board = Board(308, 125)
        self.top_bar = TopBar(10, 10, 90, 1280)
        self.top_bar.change_round(1)
        self.players = []
        self.skip_button = TextButton(85, 830, 125, 60, (255, 255, 0), "Skip")
        self.drawing_color = (0, 0, 0)
        self.chat = Chat(1050, 125)
        self.bottom_bar = BottomBar(305, 880, self)

    def add_player(self, player):
        self.players.append(player)
        self.leaderboard.add_player(player)

    def draw(self):
        self.win.fill(self.BG)
        self.leaderboard.draw(self.win)
        self.top_bar.draw(self.win)
        self.board.draw(self.win)
        self.skip_button.draw(self.win)
        self.bottom_bar.draw(self.win)
        self.chat.draw(self.win)
        pygame.display.update()

    def check_clicks(self):
        """
        handles clicks on button and screen
        :return: None
        """
        mouse = pygame.mouse.get_pos()

        # Check skip button click
        if self.skip_button.click(*mouse):
            print("Clicked skip button")
        
        clicked_board = self.board.click(*mouse)
        if clicked_board:
            self.board.update(*clicked_board, self.drawing_color)

    def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(600)
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

                if pygame.mouse.get_pressed()[0]:
                    self.check_clicks()
                    self.bottom_bar.button_events()

                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.K_RETURN:
                        self.chat.update_chat()
                    # gets the key name
                    key_name = pygame.key.name(event.key)

                    key_name = key_name.lower()
                    self.chat.type(key_name)

        pygame.quit()


