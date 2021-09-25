"""
Handles operations related to game and connections between, player, board, chat and round
"""
from round import Round
from board import Board
import random


class Game(object):

    def __init__(self, id, players):
        """
        init the game once threshold is met
        :param id: int
        :param players: Players[]
        """
        self.id = id
        self.players = players
        self.words_used = set()
        self.round = None
        self.board = Board()
        self.player_draw_ind = 0
        self.round_cnt = 1
        self.start_new_round()

    def start_new_round(self):
        """
        Starts a new round with a new word
        :return: None
        """
        try:
            round_word = self.get_word()
            self.round = Round(round_word, self.players[self.player_draw_ind], self)
            self.round_cnt += 1

            if self.player_draw_ind >= len(self.players):
                self.round_ended()
                self.end_game()
            self.player_draw_ind += 1

        except Exception as e:
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
        # TODO check this
        if player in self.players:
            player_ind = self.players.index(player)
            if player_ind >= self.player_draw_ind:
                self.player_draw_ind -= 1
            self.players.remove(player)
            self.round.player_left(player)
        else:
            raise Exception("Player not in game")

        if len(self.players) <= 2:
            self.end_game()

    def get_player_scores(self):
        """
        dict of a player scores
        :return: above desc dict
        """
        scores = {player.name: player.get_score() for player in self.players}
        return scores

    def skip(self):
        """
        Increments the round skips if skips are greater than threshold, start new round
        :return: none
        """
        if self.round:
            new_round = self.round.skip()
            if new_round:
                self.round_ended()
                return True
            return False
        else:
            raise Exception("No round started yet")

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
        print(f"[GAME] Game {self.id} ended")
        for player in self.players:
            player.game = None

    def update_board(self, x, y, color):
        """
        calls update board method
        :param x: int
        :param y: int
        :param color: 0-8
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
        with open("word.txt", "r") as f:
            words = []
            for line in f:
                wrd = line.strip()
                if wrd not in self.words_used:
                    words.append(wrd)

            self.words_used.add(wrd)

            r = random.randint(0, len(words)-1)
            return words[r].strip()
