from random import shuffle

import pytest

from blackjack.game import (
    BlackJackCard,
    BlackJackDeck,
    Player,
    PlayerStatus,
    PlayerInvalidOperation, Game, GameStatus)


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
    player.name = 'Luck'
    winning_hand = (
        BlackJackCard('10', '♣'),
        BlackJackCard('9', '♢'),
        BlackJackCard('2', '♡')
    )

    for card in winning_hand:
        player.hit(card)
    return player


LUCKY_PLAYER_STR = """Player Luck
    hand : 
        10 of ♣
        9 of ♢
        2 of ♡
    count: 21"""


def test_player_description(lucky_player):
    assert LUCKY_PLAYER_STR == lucky_player.description()


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


@pytest.fixture
def game():
    game = Game(n_players=4)
    return game


def test_game_has_black_jack_deck(game):
    assert isinstance(game._deck, BlackJackDeck)


def test_game_shuffle_cards(game: Game):
    initial_cards_order = list(game._deck)
    game.shuffle_cards()
    assert initial_cards_order != list(game._deck)


def test_game_initial_status(game: Game):
    assert GameStatus.RUNNING == game.status


def test_game_initial_turn_player(game: Game):
    """Check first player is current turn player"""
    assert game._players[0] is game.current_turn_player


def test_game_toss_card_effect_on_player(game: Game):
    """Check first player is current turn player"""
    player = game.current_turn_player
    previous_hand_len = len(player.hand)
    game.toss_card()
    assert (0, 1) == (previous_hand_len, len(player.hand))


def test_game_toss_card_effect_on_deck(game: Game):
    """Check card is popped from deck"""
    previous_deck_len = len(game._deck)
    game.toss_card()
    assert (52, 51) == (previous_deck_len, len(game._deck))


def test_game_toss_card_effect_current_turn_player(game: Game):
    """Check next player become current_turn_player"""
    game.toss_card()
    assert game._players[1] is game.current_turn_player


def test_game_initial_deal(game: Game):
    game.deal()
    player_hands_lens = [len(p.hand) for p in game._players]
    assert [2] * len(player_hands_lens) == player_hands_lens


def test_game_stop_effect_on_current_player(game: Game):
    player = game.current_turn_player
    game.stop()
    assert PlayerStatus.STOPPED == player.status


def test_game_current_player_chaange_after_stop(game: Game):
    game.stop()
    assert game._players[1] is game.current_turn_player


def test_stopped_player_never_become_current_player(game):
    stopped_player = game.current_turn_player
    game.stop()
    round_players = []
    for _ in range(len(game._players)):
        round_players.append(game.current_turn_player)
        game.toss_card()
    assert stopped_player not in round_players


def test_stopped_player_never_become_current_player(game):
    exceeded_player = game.current_turn_player
    game.toss_card()  # updating to next player
    # exceeding player
    for _ in range(3):
        exceeded_player.hit(BlackJackCard('10', '♣'))
    round_players = []
    for _ in range(len(game._players)):
        round_players.append(game.current_turn_player)
        game.toss_card()
    assert exceeded_player not in round_players


def test_game_over_when_all_players_stopped(game):
    for _ in game._players:
        game.stop()
    assert GameStatus.OVER == game.status


def test_game_over_when_all_players_exceeded(game):
    while game.toss_card():
        pass
    assert GameStatus.OVER == game.status


def test_game_over_when_all_players_exceeded_or_stopped(game):
    game.stop()
    while game.toss_card():
        pass
    assert GameStatus.OVER == game.status


def generate_ordered_stopped_players():
    """Generating tuples of ordered players by points on hands"""

    players = list(map(Player, range(1, 5)))
    players[0]._hand = [
        BlackJackCard('A', '♣'),
        BlackJackCard('2', '♣'),
        BlackJackCard('3', '♣'),
        BlackJackCard('4', '♣'),
    ]
    players[1]._hand = [
        BlackJackCard('A', '♣'),
        BlackJackCard('2', '♣'),
        BlackJackCard('3', '♣'),
    ]
    players[2]._hand = [BlackJackCard('A', '♣'), BlackJackCard('2', '♣'), ]

    players[3]._hand = [BlackJackCard('A', '♣')]

    yield players

    # Forth player exceed
    players[3]._hand = [
        BlackJackCard('J', '♣'),
        BlackJackCard('Q', '♣'),
        BlackJackCard('K', '♣'),
    ]
    yield players


@pytest.mark.parametrize('ordered_players', generate_ordered_stopped_players(),
                         ids=['No exceeded players', 'One exceeed player'])
def test_game_rank(game: Game, ordered_players):
    shuffled_players = list(ordered_players)
    shuffle(shuffled_players)
    game._players = shuffled_players
    assert ordered_players == game.rank()
