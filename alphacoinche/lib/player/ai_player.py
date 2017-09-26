"""AI Coinche player."""
from alphacoinche.lib.player import player

AI_RANDOM_NAMES = ['JohnnyAI', 'NatAI', 'LetAI', 'DarkAI']


class AiCoinchePlayer(player.CoinchePlayer):
    """AI CoinchePlayer."""

    def _get_name(self):
        name = AI_RANDOM_NAMES[self.self.init_number]
        print('Creating AI Player {} in team {}'.format(name, self.team))
        return name
