from enum import Enum, auto
from itertools import cycle

from blackjack.base_deck import Card


class BlackJackCard(Card):
    _values = dict(zip('A 2 3 4 5 6 7 8 9 10'.split(), range(1, 11)))
    _values.update(zip('JQK', cycle([10])))

    @property
    def value(self):
        return self._values[self.rank]


class PlayerStatus(Enum):
    PLAYING = auto()
    EXCEEDED = auto()


class Player:
    def __init__(self):
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
        self._hand.append(card)
        if self.count() > 21:
            self._status = PlayerStatus.EXCEEDED

    @property
    def status(self):
        return self._status
