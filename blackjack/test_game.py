import pytest

from blackjack.game import (
    BlackJackCard,
    BlackJackDeck,
    Player,
    PlayerStatus,
    PlayerInvalidOperation, Game)


@pytest.mark.parametrize('expected,suit',
                         zip(range(2, 10), BlackJackDeck.suits))
def test_black_jack_card_number_values(expected, suit):
    assert expected == BlackJackCard(str(expected), suit).value


@pytest.mark.parametrize('suit', BlackJackDeck.suits)
def test_ace_value(suit):
    assert 1 == BlackJackCard('A', suit).value


@pytest.mark.parametrize('suit', BlackJackDeck.suits)
def test_ace_value(suit):
    assert 1 == BlackJackCard('A', suit).value


@pytest.mark.parametrize('face,suit', zip('JQK', BlackJackDeck.suits))
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


@pytest.fixture
def lucky_player(player):
    winning_hand = (
        BlackJackCard('10', '♣'),
        BlackJackCard('9', '♣'),
        BlackJackCard('2', '♣')
    )

    for card in winning_hand:
        player.hit(card)
    return player


@pytest.fixture
def exceeded_player(lucky_player):
    exc_player = lucky_player
    exc_player.hit(BlackJackCard('A', '♣'))
    return exc_player


@pytest.fixture
def stopped_player(lucky_player: Player):
    st_player = lucky_player
    st_player.stop()
    return st_player


def test_player_exceeding_21(exceeded_player):
    assert PlayerStatus.EXCEEDED == exceeded_player.status


def test_player_stopped_status(stopped_player):
    assert PlayerStatus.STOPPED == stopped_player.status


def test_player_stopped_cant_hit(stopped_player):
    with pytest.raises(PlayerInvalidOperation):
        stopped_player.hit(BlackJackCard('A', '♣'))


def test_player_exceeded_cant_hit(exceeded_player):
    with pytest.raises(PlayerInvalidOperation):
        exceeded_player.hit(BlackJackCard('A', '♣'))


@pytest.fixture
def reset_player_count():
    count = Player._players_count
    Player._players_count = 0
    yield
    Player._players_count = count


@pytest.mark.usefixtures('reset_player_count')
def test_default_player_name():
    assert 'Player 1' == str(Player())


@pytest.mark.usefixtures('reset_player_count')
def test_default_player_incrementing_name():
    """Check defaults name are Player 1, Player 2 and so on"""
    players_and_names = ((Player(), f'Player {i}') for i in range(1, 10))
    players, names = zip(*players_and_names)
    assert list(names) == list(map(str, players))


def test_custom_player_name():
    assert 'Player Jane' == str(Player('Jane'))


def test_black_jack_deck_card():
    assert isinstance(BlackJackDeck().pop(), BlackJackCard)


@pytest.mark.parametrize('n_players', range(2, 10))
def test_game_init_with_players_count(n_players):
    """Check Game initialization with players count"""
    game = Game(n_players=n_players)
    assert n_players == len(game._players)


@pytest.mark.parametrize(
    'names',
    [
        'Jane Mary'.split(),
        'Jane Mary Susan'.split(),
        'Jane Mary Susan May'.split(),
    ]
)
def test_game_init_with_player_names(names):
    """Check Game initialization with players count"""
    game = Game(player_names=names)
    assert names == [player.name for player in game._players]
