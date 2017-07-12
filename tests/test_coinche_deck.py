"""Test file for the CoincheDeck class."""
from alphacoinche.lib.cards import deck


def test_initialisation():
    """Test initialisation."""
    coinche_deck = deck.CoincheDeck()
    assert len(coinche_deck.deck) == 32


def test_selction():
    """Test selection."""
    coinche_deck = deck.CoincheDeck()
    assert [(not card.value.isdigit() or int(card.value) >= 7)
            for card in coinche_deck.deck]
