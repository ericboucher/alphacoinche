"""Default CoinchePlayer class."""


class CoinchePlayer(object):
    """Main CoinchePlayer class."""

    def __init__(self, init_number, team, name=None):
        """Default init for CoinchePlayer."""
        self.init_number = init_number
        self.team = team
        if name is None:
            name = self._get_name()
        self.name = name
        self.deck = []
        self.ai = None

    def distribute_deck(self, deck):
        """Distribute."""
        self.deck = deck

    def _get_name(self):
        return None

    def play(self, cards_played=[]):
        """Play card on a round."""
        pass
