import time
import random
from player import Player

class Deck:
    shape = ["heart", "diamond" , "club", "spade"]
    rank = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    name =  ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen", "King"]
    dict= {}
    def __init__(self):
        self.totalnumofcards = 52
        self.createadeck = self.creatingdeck()
        self.__deck = {0: ('Ace', 1, 'heart'), 1: ('Ace', 1, 'diamond'), 2: ('Ace', 1, 'club'), 3: ('Ace', 1, 'spade'),
       4: ('2', 2, 'heart'), 5: ('2', 2, 'diamond'), 6: ('2', 2, 'club'), 7: ('2', 2, 'spade'), 8: ('3', 3, 'heart'),
       9: ('3', 3, 'diamond'), 10: ('3', 3, 'club'), 11: ('3', 3, 'spade'), 12: ('4', 4, 'heart'),
       13: ('4', 4, 'diamond'), 14: ('4', 4, 'club'), 15: ('4', 4, 'spade'), 16: ('5', 5, 'heart'),
       17: ('5', 5, 'diamond'), 18: ('5', 5, 'club'), 19: ('5', 5, 'spade'), 20: ('6', 6, 'heart'),
       21: ('6', 6, 'diamond'), 22: ('6', 6, 'club'), 23: ('6', 6, 'spade'), 24: ('7', 7, 'heart'),
       25: ('7', 7, 'diamond'), 26: ('7', 7, 'club'), 27: ('7', 7, 'spade'), 28: ('8', 8, 'heart'),
       29: ('8', 8, 'diamond'), 30: ('8', 8, 'club'), 31: ('8', 8, 'spade'), 32: ('9', 9, 'heart'),
       33: ('9', 9, 'diamond'), 34: ('9', 9, 'club'), 35: ('9', 9, 'spade'), 36: ('10', 10, 'heart'),
       37: ('10', 10, 'diamond'), 38: ('10', 10, 'club'), 39: ('10', 10, 'spade'), 40: ('Jack', 11, 'heart'),
       41: ('Jack', 11, 'diamond'), 42: ('Jack', 11, 'club'), 43: ('Jack', 11, 'spade'), 44: ('Queen', 12, 'heart'),
       45: ('Queen', 12, 'diamond'), 46: ('Queen', 12, 'club'), 47: ('Queen', 12, 'spade'), 48: ('King', 13, 'heart'),
       49: ('King', 13, 'diamond'), 50: ('King', 13, 'club'), 51: ('King', 13, 'spade')}

    @property
    def deck(self):
        return self.__deck

    def creatingdeck(self):
        i=0
        for rank_val in Deck.rank:

            for name_val in Deck.name:
                for shape_val in Deck.shape:

                    Deck.dict[(i)] = (name_val, rank_val, shape_val)
                    i += 1
                Deck.name.remove(name_val)
                break
        return Deck.dict

    def shuffle(self):

        ##shuffle the dictionary using shuffle methods from random module

        keys = list(self.deck.keys())

        random.shuffle(keys)
        shuffled_deck = {}
        for key in keys:
            shuffled_deck.update({key:  self.__deck[key]})
        self.__deck = shuffled_deck
        return self.__deck

        ## There is a function to suffle the dictionary using the suffle method in random module, hence depricating this
        #this fun will take deck and suffle all the cards in it
        # suffled_deck = {}
        # for key, value in self.__deck.items():
        #     random_key = random.randint(0, len(self.__deck)-1)
        #     while random_key in suffled_deck:
        #         random_key1 = random.randint(0, len(self.__deck)-1)
        #         if random_key1 not in suffled_deck:
        #             suffled_deck[random_key]= value
        #             break
        #     if random_key not in suffled_deck:
        #         suffled_deck[random_key] = value
        # self.__deck = suffled_deck
        # return self.__deck



    def reset_deck(self):
        self.__deck = {0: ('Ace', 1, 'heart'), 1: ('Ace', 1, 'diamond'), 2: ('Ace', 1, 'club'), 3: ('Ace', 1, 'spade'),
                       4: ('2', 2, 'heart'), 5: ('2', 2, 'diamond'), 6: ('2', 2, 'club'), 7: ('2', 2, 'spade'),
                       8: ('3', 3, 'heart'),
                       9: ('3', 3, 'diamond'), 10: ('3', 3, 'club'), 11: ('3', 3, 'spade'), 12: ('4', 4, 'heart'),
                       13: ('4', 4, 'diamond'), 14: ('4', 4, 'club'), 15: ('4', 4, 'spade'), 16: ('5', 5, 'heart'),
                       17: ('5', 5, 'diamond'), 18: ('5', 5, 'club'), 19: ('5', 5, 'spade'), 20: ('6', 6, 'heart'),
                       21: ('6', 6, 'diamond'), 22: ('6', 6, 'club'), 23: ('6', 6, 'spade'), 24: ('7', 7, 'heart'),
                       25: ('7', 7, 'diamond'), 26: ('7', 7, 'club'), 27: ('7', 7, 'spade'), 28: ('8', 8, 'heart'),
                       29: ('8', 8, 'diamond'), 30: ('8', 8, 'club'), 31: ('8', 8, 'spade'), 32: ('9', 9, 'heart'),
                       33: ('9', 9, 'diamond'), 34: ('9', 9, 'club'), 35: ('9', 9, 'spade'), 36: ('10', 10, 'heart'),
                       37: ('10', 10, 'diamond'), 38: ('10', 10, 'club'), 39: ('10', 10, 'spade'),
                       40: ('Jack', 11, 'heart'),
                       41: ('Jack', 11, 'diamond'), 42: ('Jack', 11, 'club'), 43: ('Jack', 11, 'spade'),
                       44: ('Queen', 12, 'heart'),
                       45: ('Queen', 12, 'diamond'), 46: ('Queen', 12, 'club'), 47: ('Queen', 12, 'spade'),
                       48: ('King', 13, 'heart'),
                       49: ('King', 13, 'diamond'), 50: ('King', 13, 'club'), 51: ('King', 13, 'spade')}

        return self.__deck

    def deal(self, player):
        #get the first card from the deck and return it

        first_key = next(iter(self.deck))
        first_value = self.deck[next(iter(self.deck))]
        del self.__deck[first_key]
        time.sleep(1)
        player.hascard.update({first_key: first_value})
        return [first_key, first_value]


    def start(self, random_player_list, total_players ):
        assert total_players < 14, "total num of players must be less than 14 "
        assert total_players >= 2 , "maximum of 2 players are required"
        self.shuffle()
        print(self.__deck)
        for i in range(3):
            for player in random_player_list:
                a = self.deal(player)
                print(player.name, a)



