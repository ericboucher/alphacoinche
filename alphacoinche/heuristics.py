"""Main heuristics for the best coinche AI in the world."""


class Color(object):
    """Color."""

    HEART = 0
    SPADE = 1
    CLUB = 2
    DIAMOND = 3


# bet = (color, height)


class AlphaCoinche(object):
    """Coinche player."""

    def bet(self, higest_best=None, last_partner_bet=None):
        """Bet action."""
        pass
        # if higest_best=none, check for 9, jack
        # if 9, jack, -> 90
        # if jack+2 and more 15 points -> 80

        # if highest_n=
