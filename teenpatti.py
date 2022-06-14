
from deck import Deck
from player import Player
from teenpattirules import Rules

## creating players:
player1 = Player("sunny")
player2 = Player("smith")
player3 = Player("vicky")


##asking all the registered players whether they want to play the game, if yes, the credit of "50" will be deducted
for player in Player.total_player_list:
    answer = input(f"Hey {player.name},  Do you want to play game? answer in y or n :")
    if answer == "y":
        player.credit = player.credit - 50
        ## adding player to the new list:
        Player.new_player_list.append(player)


deck = Deck()  # creating a deck


deck.start()    #staring the game and issuing the cards to all the players

deck.show_result()

