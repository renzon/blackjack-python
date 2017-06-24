# blackjack-python
A Simple version of Black Jack game in Python 3.6

[![Build Status](https://travis-ci.org/renzon/blackjack-python.svg?branch=master)](https://travis-ci.org/renzon/blackjack-python)
[![codecov](https://codecov.io/gh/renzon/blackjack-python/branch/master/graph/badge.svg)](https://codecov.io/gh/renzon/blackjack-python)
[![Updates](https://pyup.io/repos/github/renzon/blackjack-python/shield.svg)](https://pyup.io/repos/github/renzon/blackjack-python/)
[![Python 3](https://pyup.io/repos/github/renzon/blackjack-python/python-3-shield.svg)](https://pyup.io/repos/github/renzon/blackjack-python/)

Console example:

```python
    >>> # Seeding random to use this as doctest
    >>> import random
    >>> random.seed(1)
    >>> from blackjack.game import Game
    >>> game = Game(player_names='Sara Susan May'.split())
    >>> sara = game.current_turn_player
    >>> sara
    Player('Sara') hand:()
    >>> game.deal()
    >>> sara
    Player('Sara') hand:(BlackJackCard(rank='A', suit='♠'), BlackJackCard(rank='A', suit='♣'))
    >>> game.toss_card()
    True
    >>> sara
    Player('Sara') hand:(BlackJackCard(rank='A', suit='♠'), BlackJackCard(rank='A', suit='♣'), BlackJackCard(rank='K', suit='♢'))
    >>> susan = game.current_turn_player
    >>> susan
    Player('Susan') hand:(BlackJackCard(rank='A', suit='♡'), BlackJackCard(rank='K', suit='♠'))
    >>> susan.status
    <PlayerStatus.PLAYING: 1>
    >>> game.toss_card()
    True
    >>> susan
    Player('Susan') hand:(BlackJackCard(rank='A', suit='♡'), BlackJackCard(rank='K', suit='♠'), BlackJackCard(rank='K', suit='♣'))
    >>> may = game.current_turn_player
    >>> game.current_turn_player
    Player('May') hand:(BlackJackCard(rank='A', suit='♢'), BlackJackCard(rank='K', suit='♡'))
    >>> may
    Player('May') hand:(BlackJackCard(rank='A', suit='♢'), BlackJackCard(rank='K', suit='♡'))
    >>> may.status
    <PlayerStatus.PLAYING: 1>
    >>> game.stop()
    >>> may
    Player('May') hand:(BlackJackCard(rank='A', suit='♢'), BlackJackCard(rank='K', suit='♡'))
    >>> may.status
    <PlayerStatus.STOPPED: 3>
    >>> game.status
    <GameStatus.RUNNING: 1>
    >>> game.current_turn_player
    Player('Sara') hand:(BlackJackCard(rank='A', suit='♠'), BlackJackCard(rank='A', suit='♣'), BlackJackCard(rank='K', suit='♢'))
    >>> game.toss_card()
    True
    >>> sara
    Player('Sara') hand:(BlackJackCard(rank='A', suit='♠'), BlackJackCard(rank='A', suit='♣'), BlackJackCard(rank='K', suit='♢'), BlackJackCard(rank='Q', suit='♠'))
    >>> sara.status
    <PlayerStatus.EXCEEDED: 2>
    >>> game.status
    <GameStatus.RUNNING: 1>
    >>> game.current_turn_player
    Player('Susan') hand:(BlackJackCard(rank='A', suit='♡'), BlackJackCard(rank='K', suit='♠'), BlackJackCard(rank='K', suit='♣'))
    >>> susan.status
    <PlayerStatus.PLAYING: 1>
    >>> game.stop()
    >>> susan.status
    <PlayerStatus.STOPPED: 3>
    >>> game.status
    <GameStatus.OVER: 2>
    >>> # Can't toss card after game is over
    >>> game.toss_card()
    False
    >>> # Players rank:
    >>> game.rank()
    [Player('Susan') hand:(BlackJackCard(rank='A', suit='♡'), BlackJackCard(rank='K', suit='♠'), BlackJackCard(rank='K', suit='♣')), Player('May') hand:(BlackJackCard(rank='A', suit='♢'), BlackJackCard(rank='K', suit='♡')), Player('Sara') hand:(BlackJackCard(rank='A', suit='♠'), BlackJackCard(rank='A', suit='♣'), BlackJackCard(rank='K', suit='♢'), BlackJackCard(rank='Q', suit='♠'))]
    >>> # Better generating description:
    >>> for player in game.rank():
    ...     print(player.description())
    ... 
    Player Susan
        hand : 
            A of ♡
            K of ♠
            K of ♣
        count: 21
    Player May
        hand : 
            A of ♢
            K of ♡
        count: 11
    Player Sara
        hand : 
            A of ♠
            A of ♣
            K of ♢
            Q of ♠
        count: 22
    >>> # Have fun!

```

To play with project code install git and python >= 3.6. 
After that can download and run tests:

```console
~ $ git clone https://github.com/renzon/blackjack-python.git blackjack
Cloning into 'blackjack'...
~ $ cd blackjack/
blackjack $ python3.6 -m venv .venv
blackjack $ source .venv/bin/activate
(.venv) blackjack $ pip install -r requirements-dev.txt 
Installing collected packages: py, pytest
Successfully installed py-1.4.34 pytest-3.1.2
(.venv) blackjack $ pytest
===================================================== test session starts =====================================================
platform darwin -- Python 3.6.1, pytest-3.1.2, py-1.4.34, pluggy-0.4.0
rootdir: /Users/renzo/blackjack, inifile:
collected 35 items 

blackjack/test_base_deck.py .......
blackjack/test_game.py ............................

================================================== 35 passed in 0.07 seconds ==================================================
```

Also this README is a doctest that you can use to test the code:
```console
(.venv) blackjack $ python -m doctest -v README.md 
Trying:
    import random
Expecting nothing
ok
Trying:
    random.seed(1)
Expecting nothing
ok
Trying:
    from blackjack.game import Game
Expecting nothing
ok
Trying:
    game = Game(player_names='Sara Susan May'.split())
Expecting nothing
ok
Trying:
    sara = game.current_turn_player
Expecting nothing
ok
Trying:
    sara
Expecting:
    Player('Sara') hand:()
ok
Trying:
    game.deal()
Expecting nothing
ok
Trying:
    sara
Expecting:
    Player('Sara') hand:(BlackJackCard(rank='A', suit='♠'), BlackJackCard(rank='A', suit='♣'))
ok
Trying:
    game.toss_card()
Expecting:
    True
ok
Trying:
    sara
Expecting:
    Player('Sara') hand:(BlackJackCard(rank='A', suit='♠'), BlackJackCard(rank='A', suit='♣'), BlackJackCard(rank='K', suit='♢'))
ok
Trying:
    susan = game.current_turn_player
Expecting nothing
ok
Trying:
    susan
Expecting:
    Player('Susan') hand:(BlackJackCard(rank='A', suit='♡'), BlackJackCard(rank='K', suit='♠'))
ok
Trying:
    susan.status
Expecting:
    <PlayerStatus.PLAYING: 1>
ok
Trying:
    game.toss_card()
Expecting:
    True
ok
Trying:
    susan
Expecting:
    Player('Susan') hand:(BlackJackCard(rank='A', suit='♡'), BlackJackCard(rank='K', suit='♠'), BlackJackCard(rank='K', suit='♣'))
ok
Trying:
    may = game.current_turn_player
Expecting nothing
ok
Trying:
    game.current_turn_player
Expecting:
    Player('May') hand:(BlackJackCard(rank='A', suit='♢'), BlackJackCard(rank='K', suit='♡'))
ok
Trying:
    may
Expecting:
    Player('May') hand:(BlackJackCard(rank='A', suit='♢'), BlackJackCard(rank='K', suit='♡'))
ok
Trying:
    may.status
Expecting:
    <PlayerStatus.PLAYING: 1>
ok
Trying:
    game.stop()
Expecting nothing
ok
Trying:
    may
Expecting:
    Player('May') hand:(BlackJackCard(rank='A', suit='♢'), BlackJackCard(rank='K', suit='♡'))
ok
Trying:
    may.status
Expecting:
    <PlayerStatus.STOPPED: 3>
ok
Trying:
    game.status
Expecting:
    <GameStatus.RUNNING: 1>
ok
Trying:
    game.current_turn_player
Expecting:
    Player('Sara') hand:(BlackJackCard(rank='A', suit='♠'), BlackJackCard(rank='A', suit='♣'), BlackJackCard(rank='K', suit='♢'))
ok
Trying:
    game.toss_card()
Expecting:
    True
ok
Trying:
    sara
Expecting:
    Player('Sara') hand:(BlackJackCard(rank='A', suit='♠'), BlackJackCard(rank='A', suit='♣'), BlackJackCard(rank='K', suit='♢'), BlackJackCard(rank='Q', suit='♠'))
ok
Trying:
    sara.status
Expecting:
    <PlayerStatus.EXCEEDED: 2>
ok
Trying:
    game.status
Expecting:
    <GameStatus.RUNNING: 1>
ok
Trying:
    game.current_turn_player
Expecting:
    Player('Susan') hand:(BlackJackCard(rank='A', suit='♡'), BlackJackCard(rank='K', suit='♠'), BlackJackCard(rank='K', suit='♣'))
ok
Trying:
    susan.status
Expecting:
    <PlayerStatus.PLAYING: 1>
ok
Trying:
    game.stop()
Expecting nothing
ok
Trying:
    susan.status
Expecting:
    <PlayerStatus.STOPPED: 3>
ok
Trying:
    game.status
Expecting:
    <GameStatus.OVER: 2>
ok
Trying:
    game.toss_card()
Expecting:
    False
ok
Trying:
    game.rank()
Expecting:
    [Player('Susan') hand:(BlackJackCard(rank='A', suit='♡'), BlackJackCard(rank='K', suit='♠'), BlackJackCard(rank='K', suit='♣')), Player('May') hand:(BlackJackCard(rank='A', suit='♢'), BlackJackCard(rank='K', suit='♡')), Player('Sara') hand:(BlackJackCard(rank='A', suit='♠'), BlackJackCard(rank='A', suit='♣'), BlackJackCard(rank='K', suit='♢'), BlackJackCard(rank='Q', suit='♠'))]
ok
Trying:
    for player in game.rank():
        print(player.description())
Expecting:
    Player Susan
        hand : 
            A of ♡
            K of ♠
            K of ♣
        count: 21
    Player May
        hand : 
            A of ♢
            K of ♡
        count: 11
    Player Sara
        hand : 
            A of ♠
            A of ♣
            K of ♢
            Q of ♠
        count: 22
ok
1 items passed all tests:
  36 tests in README.md
36 tests in 1 items.
36 passed and 0 failed.
Test passed.
(.venv) blackjack $ 

```
Have fun ;)