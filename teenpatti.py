import random
from deck import Deck
from card import Card
from player import Player

## creating players:
player1 = Player("sunny")
player2 = Player("smith")
player3 = Player("vicky")

#list of players
player_list = [player1, player2, player3]

#randomise the player list:

random_player_list = random.sample(player_list, len(player_list))
# total number of players
total_players = len(random_player_list)

#creating a deck
deck = Deck()

def start(random_player_list, total_players):
    assert total_players < 14, "total num of players must be less than 14 "
    # deck.suffle()
    # issued_card = deck.deal() #retruns first card from the deck

    print(deck.deck)




    print(random_player_list)

    for i in range(total_players):
        issued_card = deck.deal()  # retruns first card from the deck
        #give the current issued card to the first player form the player list:





# start(random_player_list, total_players)

deck.suffle()

