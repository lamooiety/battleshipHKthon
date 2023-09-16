# import random
# def ShipLogic(round, yourMap, yourHp, enemyHp, p1ShotSeq, p1PrevHit, storage):

#     direction = 0

#     if (p1PrevHit):
#         storage = Hunt(p1ShotSeq[-1], storage, p1PrevHit, p1ShotSeq)
#     else:
#         tuple = RandCoordGen(p1ShotSeq)
#         storage.append(1)
#         storage[0] = 0

#     if (storage[0] == 0):
#         return tuple, storage
#     else:
#         for i in storage:
#             if type(i) is tuple:
#                 direction += 1
#                 if i in p1ShotSeq:
#                     storage.remove(i)
#                 else:
#                     tuple = i
#                     storage.remove(i)
#                     storage[0] = direction
#                     break

#     # for i in range(len(p1ShotSeq)):
#     #     if tuple in p1ShotSeq:
#     #         tuple = RandCoordGen()
#     #     else: 
#     #         break
   
#     return tuple, storage
# ''

def RandCoordGen(p1ShotSeq):
    if (random.getrandbits(1) == 1):
        x = random.randrange(1,10,2)
        y = random.randrange(1,10,2)
    else:
        x = random.randrange(2,11,2)
        y = random.randrange(2,11,2)

    tuple = [x, y]

    if tuple in p1ShotSeq:
        RandCoordGen(p1ShotSeq)
    
    #print(tuple)
    return tuple

# def TupleGen(p1ShotSeq):
#     tuple = RandCoordGen()

#     if tuple in p1ShotSeq:
#         TupleGen(p1ShotSeq)
    
#     return tuple  

# def Hunt(latestShot, storage, p1PrevHit, p1ShotSeq):
#     if p1PrevHit and storage[0] != 0:
#         for i in storage:
#             if type(i) is tuple:
#                 storage.remove(i)
#     if p1PrevHit and storage[0] == 1:
#         storage.append(latestShot[0] + 1, latestShot[1])
#         for i in range(5):
#             if (latestShot[0] - i, latestShot[1]) not in  p1ShotSeq:
#                 storage.append(latestShot[0] - i, latestShot[1])
#                 break
#     elif p1PrevHit and storage[0] == 2:
#         storage.append(latestShot[0], latestShot[1] + 1)
#         for i in range(5):
#             if (latestShot[0] , latestShot[1] - i) not in  p1ShotSeq:
#                 storage.append(latestShot[0] , latestShot[1] - i)
#                 break
#     elif p1PrevHit and storage[0] == 3:
#         storage.append(latestShot[0] - 1, latestShot[1])
#         for i in range(5):
#             if (latestShot[0] + i, latestShot[1]) not in  p1ShotSeq:
#                 storage.append(latestShot[0] + i, latestShot[1])
#                 break
#     elif p1PrevHit and storage[0] == 4:
#         storage.append(latestShot[0], latestShot[1] - 1)
#         for i in range(5):
#             if (latestShot[0] , latestShot[1] + i) not in  p1ShotSeq:
#                 storage.append(latestShot[0] , latestShot[1] + i)
#                 break
#     else:
#         storage[0] = 1
#         potentialTargets = [(latestShot[0] + 1, latestShot[1]), (latestShot[0], latestShot[1] + 1), 
#                             (latestShot[0] - 1, latestShot[1]), (latestShot[0], latestShot[1] - 1)]
#     for i in potentialTargets:
#         if (i[0] > 0 and i[0] <= 10 and i[1] > 0 and i[1] <= 10):
#             storage.append(i)
#     return storage

import random
def ShipLogic(round, yourMap, yourHp, enemyHp, p1ShotSeq, p1PrevHit, storage):
    if (p1PrevHit):
        storage = Hunt(p1ShotSeq[-1], storage)
    else:
        tuple = RandCoordGen(p1ShotSeq)

    if (len(storage) == 0):
        return tuple, storage
    else:
        for i in storage:
            if i in p1ShotSeq:
                storage.remove(i)
            else:
                tuple = i
                storage.remove(i)
                break
    return tuple, storage

def Hunt(latestShot, storage):
    potentialTargets = [(latestShot[0] + 1, latestShot[1]), (latestShot[0], latestShot[1] + 1), 
                        (latestShot[0] - 1, latestShot[1]), (latestShot[0], latestShot[1] - 1)]
    for i in potentialTargets:
        if (i[0] > 0 and i[0] <= 10 and i[1] > 0 and i[1] <= 10):
            storage.append(i)
    return storage
