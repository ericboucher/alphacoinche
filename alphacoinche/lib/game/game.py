"""Top layer game class."""
from alphacoinche.lib.cards import deck
from alphacoinche.lib.game import round
from alphacoinche.lib.player import ai_player, human_player


class CoincheGame(object):
    """Coinche Game class."""

    def __init__(self, ai_players=[], score_limit=1000, shuffle_init=True):
        """Init CoincheGame."""
        self.ai_players = ai_players
        self.score_limit = score_limit
        self.shuffle_init = shuffle_init
        self.deck = deck.CoincheDeck(shuffle_init=self.shuffle_init)
        # Init game variables.
        self.players = []
        self.scores = {'0': 0, '1': 0}
        self.dealer_id = 0
        self._initialize_players()
        self.dealer = self.players[self.dealer_id]

    def _initialize_players(self):
        players = []
        for player_number in range(0, 4):
            if player_number in self.ai_players:
                players.append(
                    ai_player.AiCoinchePlayer(
                        init_number=player_number,
                        team=player_number % 2))
            else:
                players.append(
                    human_player.HumanCoinchePlayer(
                        init_number=player_number,
                        team=player_number % 2))
        self.players = players

    def _get_next_dealer(self):
        # TODO: Get player's name.
        print("It's {}'s turn to deal.".format(self.dealer.name))
        # TODO: Ask for aggressive dealing.
        aggressive = False
        return aggressive

    def _increment_dealer(self):
        self.dealer_id += 1
        self.dealer_id %= 4
        self.dealer = self.players[self.dealer_id]

    def _update_scores(self, round_scores):
        for team in ['0', '1']:
            self.scores[team] += round_scores[team]

    def play(self):
        """Start game."""
        while max(self.scores['0'], self.scores['1']) < self.score_limit:
            print('Scores are {}'.format(self.scores))

            # Deal cards.
            aggressive = self._get_next_dealer()
            decks = self.deck.distribute(dealer_id=self.dealer_id, aggressive=aggressive)
            print('decks', decks)
            for player in self.players:
                player.distribute_deck(decks[player.init_number])

            # Play round.
            coinche_round = round.Round(self.players, self.dealer_id)
            round_scores = coinche_round.start()
            self._update_scores(round_scores)

            # End round. Next dealer.
            self._increment_dealer()


if __name__ == '__main__':
    ai_players = [1]
    coinche_game = CoincheGame(ai_players=ai_players, score_limit=500)
    coinche_game.play()
