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


import random

a = [1,2,3,4,5]
print(a)
random.shuffle(a)


print(a)
print(b)






