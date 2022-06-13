#
# shape = ["heart", "diamond" , "club", "spade"]
# rank = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10 ,11 ,12 ,13]
# name =  ["Ace" ,"2" ,"3" ,"4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"10" ,"Jack" ,"Queen", "King"]
# dict= {}


# very naive method
# a= {}
# for val in rank:
#     for nam in name:
#         for shap in shape:
#             a[(nam, shap)] = val
#         name.remove(nam)
#         break

# a = {(name[i]): rank[i] for i in range(len(rank))}


# print(a)
# print(len(a))

var = {5: ('Ace', 1, 'heart'), 1: ('Ace', 1, 'diamond'), 2: ('Ace', 1, 'club'), 3: ('Ace', 1, 'spade'),
       4: ('2', 2, 'heart'), 0: ('2', 2, 'diamond'), 6: ('2', 2, 'club'), 7: ('2', 2, 'spade'), 8: ('3', 3, 'heart'),
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

var2 = {0: ('Ace', 1, {'heart': 1}), 1: ('Ace', 1, {'diamond': 2}), 2: ('Ace', 1, {'club': 3}),
       3: ('Ace', 1, {'spade': 4}), 4: ('2', 2, {'heart': 1}), 5: ('2', 2, {'diamond': 2}), 6: ('2', 2, {'club': 3}),
       7: ('2', 2, {'spade': 4}), 8: ('3', 3, {'heart': 1}), 9: ('3', 3, {'diamond': 2}), 10: ('3', 3, {'club': 3}),
       11: ('3', 3, {'spade': 4}), 12: ('4', 4, {'heart': 1}), 13: ('4', 4, {'diamond': 2}), 14: ('4', 4, {'club': 3}),
       15: ('4', 4, {'spade': 4}), 16: ('5', 5, {'heart': 1}), 17: ('5', 5, {'diamond': 2}), 18: ('5', 5, {'club': 3}),
       19: ('5', 5, {'spade': 4}), 20: ('6', 6, {'heart': 1}), 21: ('6', 6, {'diamond': 2}), 22: ('6', 6, {'club': 3}),
       23: ('6', 6, {'spade': 4}), 24: ('7', 7, {'heart': 1}), 25: ('7', 7, {'diamond': 2}), 26: ('7', 7, {'club': 3}),
       27: ('7', 7, {'spade': 4}), 28: ('8', 8, {'heart': 1}), 29: ('8', 8, {'diamond': 2}), 30: ('8', 8, {'club': 3}),
       31: ('8', 8, {'spade': 4}), 32: ('9', 9, {'heart': 1}), 33: ('9', 9, {'diamond': 2}), 34: ('9', 9, {'club': 3}),
       35: ('9', 9, {'spade': 4}), 36: ('10', 10, {'heart': 1}), 37: ('10', 10, {'diamond': 2}),
       38: ('10', 10, {'club': 3}), 39: ('10', 10, {'spade': 4}), 40: ('Jack', 11, {'heart': 1}),
       41: ('Jack', 11, {'diamond': 2}), 42: ('Jack', 11, {'club': 3}), 43: ('Jack', 11, {'spade': 4}),
       44: ('Queen', 12, {'heart': 1}), 45: ('Queen', 12, {'diamond': 2}), 46: ('Queen', 12, {'club': 3}),
       47: ('Queen', 12, {'spade': 4}), 48: ('King', 13, {'heart': 1}), 49: ('King', 13, {'diamond': 2}),
       50: ('King', 13, {'club': 3}), 51: ('King', 13, {'spade': 4})}


# print (var[next(iter(var))])
# import random
# a = {0:10,1:11,2:12,3:13,4:14,5:15}
# b={}
# print(len(a))
# for i,j in a.items():
#
#        randomnum = random.randint(0,5)
#        while randomnum in b:
#               random2 = random.randint(0,5)
#
#               if random2 not in b:
#                      b[random2] = j
#                      break
#        if randomnum not in b:
#               b[randomnum] = j
#
#
#
#
# print(a)
# print(b)
#


# import random
# shape_to_num = {"heart": 1, "diamond":2 , "club":3, "spade":4}
# rank = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# name =  ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen", "King"]
#
# dict= dict()
# def creatingdeck():
#        i = 0
#        for rank_val in rank:
#
#               for name_val in name:
#
#                      for shap_val_name, shap_val_Val in shape_to_num.items():
#                             dict[(i)] = (name_val, rank_val, {shap_val_name: shap_val_Val})
#                             i += 1
#                      name.remove(name_val)
#                      break
#        return dict
#
# print(creatingdeck())


a = {"a": 5, "b": 50, "c": 10}



print(b)