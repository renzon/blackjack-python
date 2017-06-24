from itertools import cycle

from blackjack.base_deck import Card


class BlackJackCard(Card):
    _values = dict(zip('A 2 3 4 5 6 7 8 9 10'.split(), range(1, 11)))
    _values.update(zip('JQK', cycle([10])))

    def value(self):
        return self._values[self.rank]
