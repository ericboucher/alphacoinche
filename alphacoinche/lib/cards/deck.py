"""Definition of a Coinche card deck."""
import pydealer


class CoincheDeck(object):
    """Class to create and hold coinche cards."""

    def __init__(self, shuffle_init=True):
        """Initialise a CoincheDeck."""
        self.deck = self._initialize_deck(shuffle_init)
        self.next_deck_team_1 = []
        self.next_deck_team_2 = []

    @staticmethod
    def _is_coinche_card(card):
        """Check if a card is part of a coinche deck."""
        return not card.value.isdigit() or int(card.value) >= 7

    @staticmethod
    def _initialize_deck(shuffle_init):
        """Start with a full deck and only keep cards above 7."""
        deck = pydealer.Deck()
        if shuffle_init:
            deck.shuffle()
        # REMOVE cards above 7.
        # Turn the deck into a list of cards.
        return [card for card in deck if CoincheDeck._is_coinche_card(card)]

    @staticmethod
    def _move_decks(decks, moves):
        # TODO: Implement.
        print('decks', decks)
        return decks

    def distribute(self, dealer_id, aggressive=False):
        """Distribute cards in a classical Coinche way, ot the aggressive way.

        Return 4 list of cards.
        """

        if aggressive:
            distributions = [4, 4]
        else:
            distributions = [3, 2, 3]

        # Initialize an empty deck for each player.
        decks = [[]] * 4

        for distribution_round in distributions:
            for i in range(0, len(decks)):
                print('distribution_round', distribution_round)
                print('player_deck', i)
                print(self.deck)
                cards = self.deck[-distribution_round:]
                print(cards)
                decks[i].append(cards)
                del self.deck[-distribution_round:]
                print(self.deck)
                raise

        print(decks)
        print(len(decks))
        # TODO: Move decks around to account for dealer variable.
        # Make dealers deck the last one => Move deck from 3 - dealer
        return self._move_decks(decks, 3 - dealer_id)
