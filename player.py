import uuid

class Player():
    total_player_list=[]
    new_player_list = []
    def __init__(self, name):
        self.name = name
        # self.id = id(self)    #python inbuilt id function ( i am using uuid instead of the id(), no particular
        # readons)
        self.__id = self.randomidgeberator()
        self.__hascard = {}
        Player.total_player_list.append(self)
        self.credit = 500   ## all players have default credit value up to 500


    def randomidgeberator(self):
        id = uuid.uuid1()
        return id

    @property  # to set the attribute of id private and user can not change the id, id is given by the class
    def id(self):
        return self.__id

    @property
    def hascard(self):
        return self.__hascard

    @hascard.setter
    def hascard(self, value):
        self._hascard = value
