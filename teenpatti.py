import random
from deck import Deck
from card import Card
from player import Player

## creating players:
player1 = Player("sunny")
player2 = Player("smith")
player3 = Player("vicky")
player4 = Player("celesti")

player_list = Player.total_player_list  # list of all players

##asking all the registered players whether they want to play the game, if yes, the credit of "50" will be deducted
for player in player_list:
    answer = input(f"Hey {player.name},  Do you want to play game? answer in y or n :")
    if answer == "y":
        player.credit = player.credit - 50
        ## adding player to the new list:
        Player.new_player_list.append(player)

new_player_list = Player.new_player_list  ## list of players who wants to play the game

random_player_list = random.sample(new_player_list, len(new_player_list))  # randomise the player list:

total_players = len(random_player_list)  # total number of players

deck = Deck()  # creating a deck

deck.start(random_player_list, total_players)    #staring the game and issuing the cards to all the players

deck.show_result()

