# teenpatti
Indian card game

using python i created a teen patti game. 

Firstly, a player is created using the Player class and passing the player name. you can create as many as 14 players since more than 14 players can not play using one deck.
ex : player1 = Player("john")

once the enough players are available, create a deck by instantiating the Deck class.

After creating a deck, you can start the game by using start method in deck 
deck.start()

Deck module contatins all heavy logic

deck.check_result()
this will check all the winning possibility for the given cards for each player 

Rules Module will contain below logic. Below methods will get a single argument containing the 3 cards in list. and will return appropriate dictionary. 

1) A straight Flush: straightflush() method in Rules will check if the given cards are straight flush and return True and the value of the card
2) 3 of a Kind : threeofakind() method will check if the given cards are "3 of a Kind" and return appropriate dictionary
3) A Straight: this method will check if the given cards are Straight and return the dictioray containign the straight = True and the cardvalues
4) A Flush: this method will check if the given cards are flush and return the dictioray containign the flush = True and the cardvalues
5) Is Pair : this method will check if there is a pair in the given card and pass the values in the return 
6) High Card : this method will return the highest card value in return 


roughwork.py is not connected to the project. this is just a side work and testing done during the course of building it. 
