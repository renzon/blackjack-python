from enum import Enum
from itertools import cycle

from blackjack.base_deck import Card


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
        self.name = name or str(Player._players_count)
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
