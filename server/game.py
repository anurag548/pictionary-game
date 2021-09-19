"""
Handles operations related to game and connections between, player, board, chat and round
"""
from .player import Player
from .round import Round
from .board import Board


class Game(object):

    def __init__(self, id, players):
        """
        init the game once threshold is met
        :param id: int
        :param players: Players[]
        """
        self.id = id
        self.players = players
        self.words_used = []
        self.round = None
        self.board = Board()
        self.connected_thread = None
        self.player_draw_ind = 0

        self.start_new_round()

    def start_new_round(self):
        """
        Starts a new round with a new word
        :return: None
        """
        self.round = Round(self.get_word(), self.players[self.player_draw_ind], self.players, self)
        self.player_draw_ind += 1

        if self.player_draw_ind >= len(self.players):
            self.end_round()
            self.end_game()

    def player_guess(self, player, guess):
        """
        Player guesses the word
        :param player: Player
        :param guess: str
        :return: bool
        """
        return self.round.guess(player, guess)

    def player_disconnected(self, player):
        """
        call to clean up objects when player disconnects
        :param player: player
        :return: Exception()
        """
        pass

    def skip(self):
        """
        Increments the round skips if skips are greater than threshold, start new round
        :return: none
        """
        if self.round:
            new_round = self.round.skip()
            if new_round:
                self.round_ended()
        else:
            raise Exception("Np round started yet")

    def round_ended(self):
        """
        if the round ends call start_new_round
        :return:
        """
        self.start_new_round()
        self.board.clear()

    def end_game(self):
        """
        ends game
        :return:
        """
        # TODO implement
        pass

    def update_board(self, x, y, color):
        """
        calls update board method
        :param x: int
        :param y: int
        :param color: (int, int, int)
        :return:None
        """
        if not self.board:
            raise Exception("No board created")
        self.board.update(x, y, color)

    def get_word(self):
        """
        gives a word not used in the game/ previous rounds
        :return: string
        """
        # TODO make word list
        pass
