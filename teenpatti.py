import random
from deck import Deck
from card import Card
from player import Player

## creating players:
player1 = Player("sunny")
player2 = Player("smith")
player3 = Player("vicky")

# list of players
player_list = [player1, player2, player3]

# randomise the player list:
random_player_list = random.sample(player_list, len(player_list))

# total number of players
total_players = len(random_player_list)

# creating a deck
deck = Deck()

deck.start(deck, random_player_list, total_players)
