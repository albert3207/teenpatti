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

random_player_list = random.sample(player_list, len(player_list))     # randomise the player list:
total_players = len(random_player_list)  # total number of players

deck = Deck()  # creating a deck

deck.start(deck, random_player_list, total_players)
