from collections import namedtuple

Card = namedtuple('Card', 'rank suit')


class FrenchDeck:
    ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    suits = '♣ ♢ ♡ ♠'.split()
    _card_class = Card

    def __init__(self):
        self._create_cards()

    def _create_cards(self):
        self._cards = [
            self._card_class(r, s) for r in self.ranks for s in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, pos):
        return self._cards[pos]

    def __contains__(self, card):
        return card in self._cards

    def __setitem__(self, key, value):
        self._cards[key] = value

    def __eq__(self, other):
        return self._cards == other._cards

    def pop(self):
        return self._cards.pop()
