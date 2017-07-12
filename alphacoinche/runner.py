"""Simple runner to start a coinche game."""
from alphacoinche.lib.game import game


def main():
    """Create a Coinche Game."""
    coinche_game = game.CoincheGame()
    print(coinche_game.deck)
    coinche_game.play()

if __name__ == '__main__':
    main()
