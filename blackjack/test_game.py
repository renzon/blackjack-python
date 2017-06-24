import pytest

from blackjack.base_deck import FrenchDeck
from blackjack.game import BlackJackCard


@pytest.mark.parametrize('expected,suit', zip(range(2, 10), FrenchDeck.suits))
def test_black_jack_card_number_values(expected, suit):
    assert expected == BlackJackCard(str(expected), suit).value()


@pytest.mark.parametrize('suit', FrenchDeck.suits)
def test_ace_value(suit):
    assert 1 == BlackJackCard('A', suit).value()


@pytest.mark.parametrize('suit', FrenchDeck.suits)
def test_ace_value(suit):
    assert 1 == BlackJackCard('A', suit).value()


@pytest.mark.parametrize('face,suit', zip('JQK', FrenchDeck.suits))
def test_face_card_value(face, suit):
    assert 10 == BlackJackCard(face, suit).value()
