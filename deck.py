import random
from player import Player
from teenpattirules import Rules


class Deck:
    shape_to_num = {"heart": 1, "diamond": 2, "club": 3, "spade": 4}
    rank = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    name = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    dict = {}

    def __init__(self):
        self.totalnumofcards = 52
        self.createadeck = self.creatingdeck()
        self.__deck = {
            0: ('Ace', 1, ['heart', 1]), 1: ('Ace', 1, ['diamond', 2]), 2: ('Ace', 1, ['club', 3]),
            3: ('Ace', 1, ['spade', 4]), 4: ('2', 2, ['heart', 1]), 5: ('2', 2, ['diamond', 2]),
            6: ('2', 2, ['club', 3]), 7: ('2', 2, ['spade', 4]), 8: ('3', 3, ['heart', 1]), 9: ('3', 3, ['diamond', 2]),
            10: ('3', 3, ['club', 3]), 11: ('3', 3, ['spade', 4]), 12: ('4', 4, ['heart', 1]),
            13: ('4', 4, ['diamond', 2]), 14: ('4', 4, ['club', 3]), 15: ('4', 4, ['spade', 4]),
            16: ('5', 5, ['heart', 1]), 17: ('5', 5, ['diamond', 2]), 18: ('5', 5, ['club', 3]),
            19: ('5', 5, ['spade', 4]), 20: ('6', 6, ['heart', 1]), 21: ('6', 6, ['diamond', 2]),
            22: ('6', 6, ['club', 3]), 23: ('6', 6, ['spade', 4]), 24: ('7', 7, ['heart', 1]),
            25: ('7', 7, ['diamond', 2]), 26: ('7', 7, ['club', 3]), 27: ('7', 7, ['spade', 4]),
            28: ('8', 8, ['heart', 1]), 29: ('8', 8, ['diamond', 2]), 30: ('8', 8, ['club', 3]),
            31: ('8', 8, ['spade', 4]), 32: ('9', 9, ['heart', 1]), 33: ('9', 9, ['diamond', 2]),
            34: ('9', 9, ['club', 3]), 35: ('9', 9, ['spade', 4]), 36: ('10', 10, ['heart', 1]),
            37: ('10', 10, ['diamond', 2]), 38: ('10', 10, ['club', 3]), 39: ('10', 10, ['spade', 4]),
            40: ('Jack', 11, ['heart', 1]), 41: ('Jack', 11, ['diamond', 2]), 42: ('Jack', 11, ['club', 3]),
            43: ('Jack', 11, ['spade', 4]), 44: ('Queen', 12, ['heart', 1]), 45: ('Queen', 12, ['diamond', 2]),
            46: ('Queen', 12, ['club', 3]), 47: ('Queen', 12, ['spade', 4]), 48: ('King', 13, ['heart', 1]),
            49: ('King', 13, ['diamond', 2]), 50: ('King', 13, ['club', 3]), 51: ('King', 13, ['spade', 4])}

    @property
    def deck(self):
        return self.__deck

    @staticmethod
    def creatingdeck():
        i = 0
        for rank_val in Deck.rank:

            for name_val in Deck.name:
                for shape, shape_val in Deck.shape_to_num.items():
                    Deck.dict[i] = (name_val, rank_val, [shape, shape_val])
                    i += 1
                Deck.name.remove(name_val)
                break
        return Deck.dict

    def shuffle(self):
        # shuffle the dictionary using shuffle methods from random module
        keys = list(self.deck.keys())

        random.shuffle(keys)
        shuffled_deck = {}
        for key in keys:
            shuffled_deck.update({key: self.__deck[key]})
        self.__deck = shuffled_deck
        return self.__deck

        # There is a function to suffle the dictionary using the suffle method in random module, hence depricating this
        # this fun will take deck and suffle all the cards in it
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
        self.__deck = {0: ('Ace', 1, ['heart', 1]), 1: ('Ace', 1, ['diamond', 2]), 2: ('Ace', 1, ['club', 3]),
                       3: ('Ace', 1, ['spade', 4]), 4: ('2', 2, ['heart', 1]), 5: ('2', 2, ['diamond', 2]),
                       6: ('2', 2, ['club', 3]), 7: ('2', 2, ['spade', 4]), 8: ('3', 3, ['heart', 1]),
                       9: ('3', 3, ['diamond', 2]), 10: ('3', 3, ['club', 3]), 11: ('3', 3, ['spade', 4]),
                       12: ('4', 4, ['heart', 1]), 13: ('4', 4, ['diamond', 2]), 14: ('4', 4, ['club', 3]),
                       15: ('4', 4, ['spade', 4]), 16: ('5', 5, ['heart', 1]), 17: ('5', 5, ['diamond', 2]),
                       18: ('5', 5, ['club', 3]), 19: ('5', 5, ['spade', 4]), 20: ('6', 6, ['heart', 1]),
                       21: ('6', 6, ['diamond', 2]), 22: ('6', 6, ['club', 3]), 23: ('6', 6, ['spade', 4]),
                       24: ('7', 7, ['heart', 1]), 25: ('7', 7, ['diamond', 2]), 26: ('7', 7, ['club', 3]),
                       27: ('7', 7, ['spade', 4]), 28: ('8', 8, ['heart', 1]), 29: ('8', 8, ['diamond', 2]),
                       30: ('8', 8, ['club', 3]), 31: ('8', 8, ['spade', 4]), 32: ('9', 9, ['heart', 1]),
                       33: ('9', 9, ['diamond', 2]), 34: ('9', 9, ['club', 3]), 35: ('9', 9, ['spade', 4]),
                       36: ('10', 10, ['heart', 1]), 37: ('10', 10, ['diamond', 2]), 38: ('10', 10, ['club', 3]),
                       39: ('10', 10, ['spade', 4]), 40: ('Jack', 11, ['heart', 1]), 41: ('Jack', 11, ['diamond', 2]),
                       42: ('Jack', 11, ['club', 3]), 43: ('Jack', 11, ['spade', 4]), 44: ('Queen', 12, ['heart', 1]),
                       45: ('Queen', 12, ['diamond', 2]), 46: ('Queen', 12, ['club', 3]),
                       47: ('Queen', 12, ['spade', 4]), 48: ('King', 13, ['heart', 1]),
                       49: ('King', 13, ['diamond', 2]), 50: ('King', 13, ['club', 3]), 51: ('King', 13, ['spade', 4])}

        return self.__deck

    def deal(self, player):
        # get the first card from the deck and return it

        first_key = next(iter(self.deck))
        first_value = self.deck[next(iter(self.deck))]
        del self.__deck[first_key]
        # time.sleep(1)
        player.hascard.update({first_key: first_value})
        player.cards.append(first_value)
        return [first_key, first_value]

    def start(self):

        new_player_list = Player.new_player_list  # list of players who wants to play the game

        random_player_list = random.sample(new_player_list, len(new_player_list))  # randomise the player list:

        total_players = len(random_player_list)  # total number of players

        assert total_players < 14, "total num of players must be less than 14 "
        assert total_players >= 2, "maximum of 2 players are required"
        self.shuffle()
        for i in range(3):
            for player in random_player_list:
                self.deal(player)

        # for player in Player.new_player_list:
        #     # print(player.name, player.getcards())
        #     pass

    @staticmethod
    def check_result():
        playerswithcards = []
        for player in Player.new_player_list:
            playercards = player.getcards()

            highestcardvalue = Rules.gethighcard(playercards)["highestcard"]

            secondhighestcardvalue = Rules.getsecondhighcard(playercards)["secondhighcard"]

            thirdhighestcardvalue = Rules.getthirdhighcard(playercards)["thirdhighcard"]

            isstraightflush = Rules.isSraightFlush(playercards)
            if isstraightflush["isSraightFlush"]:
                playerswithcards.append({"playername": player.name, "value": 100, "winnincombination": isstraightflush})
                continue
            isThreeofaKind = Rules.isThreeofaKind(playercards)
            if isThreeofaKind["isThreeofaKind"]:
                playerswithcards.append({"playername": player.name, "value": 90,
                                         "winnincombination": [highestcardvalue, secondhighestcardvalue,
                                                               thirdhighestcardvalue]})
                continue
            isStraight = Rules.isStraight(playercards)
            if isStraight["isStraight"]:
                playerswithcards.append({"playername": player.name, "value": 80,
                                         "winnincombination": [highestcardvalue, secondhighestcardvalue,
                                                               thirdhighestcardvalue],
                                         "winnincombinationvalue": isStraight["valueofsequence"]})
                continue
            isFlush = Rules.isFlush(playercards)
            if isFlush["isFlush"]:

                playerswithcards.append({"playername": player.name, "value": 70,
                                         "winnincombination": [highestcardvalue, secondhighestcardvalue,
                                                               thirdhighestcardvalue]})
                continue
            isPair = Rules.isPair(playercards)
            if isPair["isPair"]:
                playerswithcards.append({"playername": player.name, "value": 60,
                                         "winnincombination": [highestcardvalue, secondhighestcardvalue,
                                                               thirdhighestcardvalue]})
                continue
            playerswithcards.append(
                {"playername": player.name, "value": 50,
                 "winnincombination": [highestcardvalue, secondhighestcardvalue, thirdhighestcardvalue]})

        highestvalue = None
        playerwithsamevalue = []
        for playerwithwinningcard in playerswithcards:
            print(playerwithwinningcard)

            checkvalue = playerwithwinningcard["value"]
            if highestvalue is not None:
                if highestvalue > checkvalue:
                    continue
                if highestvalue < checkvalue:
                    highestvalue = checkvalue
                    playerwithsamevalue.clear()
                    if "winnincombinationvalue" in playerwithwinningcard.keys():
                        playerwithsamevalue.append(
                            {"playername": playerwithwinningcard["playername"],
                             "value": playerwithwinningcard["value"],
                             "winnincombination": playerwithwinningcard["winnincombination"],
                             "winnincombinationvalue": playerwithwinningcard["winnincombinationvalue"]})
                        continue

                    playerwithsamevalue.append(
                        {"playername": playerwithwinningcard["playername"], "value": playerwithwinningcard["value"],
                         "winnincombination": playerwithwinningcard["winnincombination"]})
                    continue
                if highestvalue == checkvalue:
                    highestvalue = checkvalue
                    if "winnincombinationvalue" in playerwithwinningcard.keys():
                        playerwithsamevalue.append(
                            {"playername": playerwithwinningcard["playername"],
                             "value": playerwithwinningcard["value"],
                             "winnincombination": playerwithwinningcard["winnincombination"],
                             "winnincombinationvalue": playerwithwinningcard["winnincombinationvalue"]})
                        continue
                    playerwithsamevalue.append(
                        {"playername": playerwithwinningcard["playername"], "value": playerwithwinningcard["value"],
                         "winnincombination": playerwithwinningcard["winnincombination"]})
                    continue

            highestvalue = checkvalue
            if "winnincombinationvalue" in playerwithwinningcard.keys():
                playerwithsamevalue.append(
                    {"playername": playerwithwinningcard["playername"],
                     "value": playerwithwinningcard["value"],
                     "winnincombination": playerwithwinningcard["winnincombination"],
                     "winnincombinationvalue": playerwithwinningcard["winnincombinationvalue"]})
                continue
            playerwithsamevalue.append(
                {"playername": playerwithwinningcard["playername"], "value": playerwithwinningcard["value"],
                 "winnincombination": playerwithwinningcard["winnincombination"]})

        # print("playerwithsamevalue: this is the player with same value card", playerwithsamevalue)

        if len(playerwithsamevalue) == 1:
            return playerwithsamevalue

        if len(playerwithsamevalue) > 1:
            value = playerwithsamevalue[0]["value"]
            if value == 50:
                winhand = None
                playerwinner = []
                for player in playerwithsamevalue:
                    if winhand is not None:
                        if winhand > player["winnincombination"]:
                            continue
                        if winhand < player["winnincombination"]:
                            playerwinner.clear()
                            playerwinner.append(
                                {"playername": player["playername"], "winnincombination": player["winnincombination"]})
                            continue
                    winhand = player["winnincombination"]
                    playerwinner.append(
                        {"playername": player["playername"], "winnincombination": player["winnincombination"]})
                return playerwinner

            if value == 60:
                winhand = None
                playerwinner = []
                for player in playerwithsamevalue:
                    if winhand is not None:
                        if winhand > player["winnincombination"]:
                            continue
                        if winhand < player["winnincombination"]:
                            playerwinner.clear()
                            playerwinner.append(
                                {"playername": player["playername"], "winnincombination": player["winnincombination"]})
                            continue
                        if winhand == player["winnincombination"]:
                            playerwinner.append(
                                {"playername": player["playername"], "winnincombination": player["winnincombination"]})
                            continue

                    winhand = player["winnincombination"]
                    playerwinner.append(
                        {"playername": player["playername"], "winnincombination": player["winnincombination"]})

                if len(playerwinner) == 1:
                    return playerwinner
                if len(playerwinner) > 1:
                    return [{"message": "there are more than 2 player with same hand combinations",
                             "playerwinner": playerwinner}]

            if value == 70:
                winhand = None
                playerwinner = []
                for player in playerwithsamevalue:
                    if winhand is not None:
                        if winhand > player["winnincombination"]:
                            continue
                        if winhand < player["winnincombination"]:
                            playerwinner.clear()
                            playerwinner.append(
                                {"playername": player["playername"], "winnincombination": player["winnincombination"]})
                            continue
                    winhand = player["winnincombination"]
                    playerwinner.append(
                        {"playername": player["playername"], "winnincombination": player["winnincombination"]})
                return playerwinner

            # if value == 75: winhand = None playerwinner = [] for player in playerwithsamevalue: if winhand is not
            # None: if winhand > player["winnincombination"]: continue if winhand < player["winnincombination"]:
            # playerwinner.clear() playerwinner.append( {"playername": player["playername"], "winnincombination":
            # player["winnincombination"]}) continue if winhand == player["winnincombination"]: playerwinner.append(
            # {"playername": player["playername"], "winnincombination": player["winnincombination"]}) continue
            #
            #         winhand = player["winnincombination"]
            #         playerwinner.append(
            #             {"playername": player["playername"], "winnincombination": player["winnincombination"]})
            #
            #     if len(playerwinner) == 1:
            #         return playerwinner
            #     if len(playerwinner) > 1:
            #         return [{"message": "there are more than 2 player with same hand combinations",
            #                  "playerwinner": playerwinner}]

            if value == 80:
                winhand = None
                playerwinner = []

                for player in playerwithsamevalue:
                    if winhand is not None:
                        if winhand > player["winnincombinationvalue"]:
                            continue
                        if winhand < player["winnincombinationvalue"]:
                            winhand = player["winnincombinationvalue"]
                            playerwinner.clear()
                            playerwinner.append(
                                {"playername": player["playername"], "winnincombination": player["winnincombination"]})
                            continue
                        if winhand == player["winnincombinationvalue"]:
                            playerwinner.append(
                                {"playername": player["playername"], "winnincombination": player["winnincombination"]})
                            continue
                    winhand = player["winnincombinationvalue"]
                    playerwinner.append(
                        {"playername": player["playername"], "winnincombination": player["winnincombination"]})
                return playerwinner

            if value == 90:
                winhand = None
                playerwinner = []
                for player in playerwithsamevalue:
                    if winhand is not None:
                        if winhand > player["winnincombination"]:
                            continue
                        if winhand < player["winnincombination"]:
                            playerwinner.clear()
                            playerwinner.append(
                                {"playername": player["playername"], "winnincombination": player["winnincombination"]})
                            continue
                    winhand = player["winnincombination"]
                    playerwinner.append(
                        {"playername": player["playername"], "winnincombination": player["winnincombination"]})
                return playerwinner

            if value == 100:
                return ["given players have same value sequence but of different color", playerwithsamevalue]

    def show_result(self):
        winner = self.check_result()
        print(winner)
