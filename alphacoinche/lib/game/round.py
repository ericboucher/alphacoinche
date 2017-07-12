"""Round class."""
import itertools

class Round(object):
    """Round class."""

    def __init__(self, players, dealer):
        """Initialize a new round of coinche.

        Inputs: 4 CoinchePlayers and position of the dealer.
        """
        self.players = self.order_players(players, dealer)
        self.cards_played = []

    def start(self):
        """Start Round."""
        cards = range(0, 8)
        for card, player in itertools.product(cards, self.players):
            print(card, player)
            card_played = player.play(self.cards_played)
            self.cards_played.append(card_played)

        raise
        return {'0': 0, '1': 0}

    @staticmethod
    def order_players(players, dealer):
        """Order players."""
        # TODO: Implement.
        return players
