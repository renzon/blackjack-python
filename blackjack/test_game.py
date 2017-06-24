import pytest

from blackjack.base_deck import FrenchDeck
from blackjack.game import BlackJackCard, Player, PlayerStatus


@pytest.mark.parametrize('expected,suit', zip(range(2, 10), FrenchDeck.suits))
def test_black_jack_card_number_values(expected, suit):
    assert expected == BlackJackCard(str(expected), suit).value


@pytest.mark.parametrize('suit', FrenchDeck.suits)
def test_ace_value(suit):
    assert 1 == BlackJackCard('A', suit).value


@pytest.mark.parametrize('suit', FrenchDeck.suits)
def test_ace_value(suit):
    assert 1 == BlackJackCard('A', suit).value


@pytest.mark.parametrize('face,suit', zip('JQK', FrenchDeck.suits))
def test_face_card_value(face, suit):
    assert 10 == BlackJackCard(face, suit).value


@pytest.fixture
def player():
    return Player()


def test_player_initial_hand(player):
    assert tuple() == player.hand


def test_player_initial_count(player):
    assert 0 == player.count()


HAND_COUNT = {
    1: [BlackJackCard('A', '♣')],
    3: [
        BlackJackCard('A', '♣'),
        BlackJackCard('2', '♣')
    ],
    6: [
        BlackJackCard('A', '♣'),
        BlackJackCard('2', '♣'),
        BlackJackCard('3', '♣')
    ],
}


@pytest.mark.parametrize('hand', HAND_COUNT.values())
def test_player_hit_effect_on_hand(hand, player: Player):
    for c in hand:
        player.hit(c)
    assert tuple(hand) == player.hand


@pytest.mark.parametrize('count,hand', HAND_COUNT.items())
def test_player_hit_effect_on_count(count, hand, player: Player):
    for c in hand:
        player.hit(c)
    assert count == player.count()


def test_player_initial_status(player: Player):
    assert PlayerStatus.PLAYING == player.status
