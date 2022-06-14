class Rules:
    straight_order_value = {11: [1, 2, 3], 1: [2, 3, 4], 2: [3, 4, 5], 3: [4, 5, 6], 4: [5, 6, 7], 5: [6, 7, 8],
                            6: [7, 8, 9], 7: [8, 9, 10], 8: [9, 10, 11], 9: [10, 11, 12], 10: [11, 12, 13]}

    sample3card = [['diamond', 1], ['diamond', 9], ['diamond', 13]]

    def __init__(self):
        pass

    @staticmethod
    def isFlush(threecards):
        ## check if all three cards are of same color (shape)
        isflush = None
        variabletosavevalue = None
        for eachcard in threecards:
            cardshape = eachcard[0]
            if variabletosavevalue is not None:
                if cardshape != variabletosavevalue:
                    isflush = False
                    break
                isflush = True

            variabletosavevalue = cardshape
        return {"isflush": isflush}

    @staticmethod
    def isStraight(threecards):
        cardvalue = []
        for eachcard in threecards:
            cardvalue.append(eachcard[1])
        cardvalue.sort()
        for key, value in Rules.straight_order_value.items():
            if cardvalue == value:
                valueofsequence = key
                return {"isstraight": True, "valueofsequence": valueofsequence}
        return {"isstraight": False}

    @staticmethod
    def isSraightFlush(threecards):
        isflush = Rules.isFlush(threecards)
        if isflush["isflush"]:
            isstraight = Rules.isStraight(threecards)
            if isstraight["isstraight"]:
                return {"isSraightFlush": True}
        return {"isSraightFlush": False}

    @staticmethod
    def isThreeofaKind(threecards):
        eachcardvalue = None
        for eachcard in threecards:
            cardvalue = eachcard[1]
            if eachcardvalue is not None:
                if cardvalue != eachcardvalue:
                    return {"isThreeofaKind": False}
            eachcardvalue = cardvalue
        return {"isThreeofaKind": True, "valueothecard": eachcardvalue}

    @staticmethod
    def isPair(threecards):
        cardvalues = []
        for card in threecards:
            cardvalues.append(card[1])
        cardvalues.sort()
        if cardvalues[0] == cardvalues[1]:
            return {"isPair": True,"paircardvalue":cardvalues[0] , "thirdcardvalue": cardvalues[2]}
        if cardvalues[0] == cardvalues[2]:
            return {"isPair": True, "paircardvalue":cardvalues[0] ,"thirdcardvalue": cardvalues[1]}
        if cardvalues[1] == cardvalues[2]:
            return {"isPair": True, "paircardvalue":cardvalues[1] ,"thirdcardvalue": cardvalues[0]}
        return {"isPair": False}


    @staticmethod
    def gethighcard(threecards):
        cardvalues = []
        for card in threecards:
            cardvalues.append(card[1])
        cardvalues.sort(reverse=True)
        return {"highestcard": cardvalues[0]}

    @staticmethod
    def getsecondhighcard(threecards):
        cardvalues = []
        for card in threecards:
            cardvalues.append(card[1])
        cardvalues.sort(reverse=True)
        return {"secondhighcard": cardvalues[1]}

    @staticmethod
    def getthirdhighcard(threecards):
        cardvalues = []
        for card in threecards:
            cardvalues.append(card[1])
        cardvalues.sort(reverse=True)
        return {"thirdhighcard": cardvalues[2]}




                        ## for testing purpose only ##

# player = Rules()
# sample3card = [['diamond', 1], ['diamond', 9], ['heart', 13]]

# print(player.isStraight(sample3card))

# print(player.isSraightFlush(sample3card))

# print(player.isThreeofaKind(sample3card))

# print(player.isPair(sample3card))

# print(player.gethighcard(sample3card))
#
# print(player.getsecondhighcard(sample3card))
#
# print(player.getthirdhighcard(sample3card))