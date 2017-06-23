from collections import namedtuple

Card = namedtuple('Card', 'rank suit')


class FrenchDeck:
    ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    suits = '♣ ♢ ♡ ♠'.split()

    def __init__(self):
        self._cards = list(Card(r, s) for r in self.ranks for s in self.suits)

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, pos):
        return self._cards[pos]

    def __setitem__(self, key, value):
        self._cards[key] = value
