import random

# Random Selection
def ShipLogic(round, yourMap, yourHp, enemyHp, p1ShotSeq, p1PrevHit, storage):
    x = random.randint(1,10)
    y = random.randint(1,10)
    return [x,y], storage

# # Checkerboard and Cross
# def ShipLogic(round, yourMap, yourHp, enemyHp, p1ShotSeq, p1PrevHit, storage):
#     if (p1PrevHit):
#         storage = Hunt(p1ShotSeq[-1], storage)
#     else:
#         tuple = RandCoordGen(p1ShotSeq)

#     if (len(storage) == 0):
#         return tuple, storage
#     else:
#         for i in storage:
#             if i in p1ShotSeq:
#                 storage.remove(i)
#             else:
#                 tuple = i
#                 storage.remove(i)
#                 break
#     return tuple, storage

# def RandCoordGen(p1ShotSeq):
#     if (random.getrandbits(1) == 1):
#         x = random.randrange(1,10,2)
#         y = random.randrange(1,10,2)
#     else:
#         x = random.randrange(2,11,2)
#         y = random.randrange(2,11,2)

#     tuple = [x, y]

#     if tuple in p1ShotSeq:
#         RandCoordGen(p1ShotSeq)
    
#     #print(tuple)
#     return tuple

# def Hunt(latestShot, storage):
#     potentialTargets = [(latestShot[0] + 1, latestShot[1]), (latestShot[0], latestShot[1] + 1), 
#                         (latestShot[0] - 1, latestShot[1]), (latestShot[0], latestShot[1] - 1)]
#     for i in potentialTargets:
#         if (i[0] > 0 and i[0] <= 10 and i[1] > 0 and i[1] <= 10):
#             storage.append(i)
#     return storage

# # Wide Spanning Cross
# def ShipLogic(round, yourMap, yourHp, enemyHp, p1ShotSeq, p1PrevHit, storage):
#     if (p1PrevHit and len(storage) == 0):
#         # storage = Hunt(p1ShotSeq[-1], storage)
#         storage.append(p1ShotSeq[-1]) #center shot
#         storage.append(1) #step number
#         storage.append(1) #direction
#     elif (p1PrevHit and len(storage) != 0):
#         storage[1] =  storage[1] + 1 # current direction, additional step
#     elif (not p1PrevHit and len(storage) != 0):
#         if (storage[2] < 4): # if direction is less than 4, change direction
#             storage[2] = storage[2] + 1
#         else:
#             storage.clear() # if direction is more than or equal to 4, clear storage and generate new random coordinate 
#             tuple = RandCoordGen(p1ShotSeq)
#     else:
#         tuple = RandCoordGen(p1ShotSeq)

#     if (len(storage) == 0):
#         return tuple, storage
#     else:
#         # generate the next coordinate based on the direction and step number
#         if (storage[2] == 1):
#             tuple = (storage[0][0] + storage[1], storage[0][1])
#         elif (storage[2] == 2):
#             tuple = (storage[0][0], storage[0][1] + storage[1])
#         elif (storage[2] == 3):
#             tuple = (storage[0][0] - storage[1], storage[0][1])
#         elif (storage[2] == 4):
#             tuple = (storage[0][0], storage[0][1] - storage[1])
#         # if the next coordinate is out of bound, clear storage and generate new random coordinate
#         if (tuple[0] > 10 or tuple[0] < 1 or tuple[1] > 10 or tuple[1] < 1):
#             storage.clear()
#             tuple = RandCoordGen(p1ShotSeq)
            
#     return tuple, storage