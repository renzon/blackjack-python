from enum import Enum
from itertools import cycle
from random import shuffle

from blackjack.base_deck import Card, FrenchDeck


class BlackJackCard(Card):
    _values = dict(zip('A 2 3 4 5 6 7 8 9 10'.split(), range(1, 11)))
    _values.update(zip('JQK', cycle([10])))

    @property
    def value(self):
        return self._values[self.rank]


PlayerStatus = Enum('PlayerStatus', 'PLAYING EXCEEDED STOPPED')


class PlayerInvalidOperation(Exception):
    """Exception to be raised when player try an invalid operation"""


class Player:
    _players_count = 0

    def __init__(self, name=None):
        Player._players_count += 1
        self.name = str(Player._players_count) if name is None else str(name)
        self._status = PlayerStatus.PLAYING
        self._hand = []

    @property
    def hand(self):
        return tuple(self._hand)

    def count(self):
        """Sum card values on hand

        :return: int
        """
        return sum(c.value for c in self._hand)

    def hit(self, card):
        if self.status in (PlayerStatus.STOPPED, PlayerStatus.EXCEEDED):
            raise PlayerInvalidOperation(
                f"{self} can't hit because its status is {self.status}")
        self._hand.append(card)
        if self.count() > 21:
            self._status = PlayerStatus.EXCEEDED

    @property
    def status(self):
        return self._status

    def stop(self):
        self._status = PlayerStatus.STOPPED

    def __str__(self):
        cls_name = type(self).__name__
        return f'{cls_name} {self.name}'


class BlackJackDeck(FrenchDeck):
    _card_class = BlackJackCard


GameStatus = Enum('GameStatus', 'RUNNING FINISHED')


class Game:
    def __init__(self, *, n_players=None, player_names=None):
        self._deck = BlackJackDeck()
        if player_names:
            self._players = tuple(Player(name) for name in player_names)
        else:
            self._players = tuple(Player() for _ in range(n_players))
        self._current_player_cursor = cycle(self._players)
        self._update_current_player()

    def _update_current_player(self):
        self._current_turn_player = next(self._current_player_cursor)

    def shuffle_cards(self):
        shuffle(self._deck)

    @property
    def status(self):
        return GameStatus.RUNNING

    @property
    def current_turn_player(self):
        return self._current_turn_player

    def toss_card(self):
        self.current_turn_player.hit(self._deck.pop())
        self._update_current_player()

    def deal(self):
        """Proceed initial deal tossing 2 cards for each player"""
        for _ in range(2 * len(self._players)):
            self.toss_card()

    def stop(self):
        self.current_turn_player.stop()
