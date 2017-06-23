from random import shuffle

import pytest

from blackjack.deck import Card, FrenchDeck


@pytest.fixture(scope='session')
def two_of_clubs():
    return Card('2', '♣')


@pytest.fixture(scope='session')
def french_deck():
    return FrenchDeck()


def test_card_fields(two_of_clubs):
    assert ('2', '♣') == (two_of_clubs.rank, two_of_clubs.suit)


def test_card_eq(two_of_clubs):
    assert Card('2', '♣') == two_of_clubs


def test_french_deck_len(french_deck):
    number_of_ranks = 13
    number_of_suits = 4
    assert (number_of_ranks * number_of_suits) == len(french_deck)


def test_deck_shuffle(french_deck):
    shuffled_deck = FrenchDeck()
    shuffle(shuffled_deck)
    # Chances of been equal 1/(52!)
    assert french_deck != shuffled_deck


def test_deck_eq(french_deck):
    assert french_deck == FrenchDeck()
