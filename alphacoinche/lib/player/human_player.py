"""Human coinche player."""
from alphacoinche.lib.player import player


class HumanCoinchePlayer(player.CoinchePlayer):
    """Human CoinchePlayer."""

    def _get_name(self):
        return input('Enter name for player {}: '.format(self.init_number))
