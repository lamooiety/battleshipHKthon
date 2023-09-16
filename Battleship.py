import random
GRIDSIZE = 10

# storage == [] or storage[0] == 1 : hunting
# storage[0] == 2: cross search

def ShipLogic(round, yourMap, yourHp, enemyHp, p1ShotSeq, p1PrevHit, storage):
    

    # hunting for the battelship
    if not p1PrevHit and (storage == [] or storage[0] == 1):
        if storage == []:
            storage.append(1)

        # get available coordinates
        blackboard = []
        whiteboard = []
        for i in range(1, GRIDSIZE+1):
            for j in range(1, GRIDSIZE+1):
                if (i + j) % 2 == 0:
                    blackboard.append([i,j]) 
                else:
                    whiteboard.append([i,j])
        
        for prev in p1ShotSeq:
            if prev in blackboard:
                blackboard.remove(prev)
            else:
                whiteboard.remove(prev)

        # if the blackboard is empty, we have to chooce from the whiteboard
        if blackboard != []:
            coord = random.choice(blackboard)
        else:
            coord = random.choice(whiteboard)

        return coord, storage
    
    # first hit an object
    elif p1PrevHit and (storage == [] or storage[0] == 1):
        # update the storage to step 2
        storage = []
        storage.append(2)

        # get the previous coordinate
        prevCoord = p1ShotSeq[-1]
        prevX, prevY = prevCoord

        crossboard = []
        if prevX != 1:
            crossboard.append([prevCoord[0]-1, prevCoord[1]])
        if prevX != 10:
            crossboard.append([prevCoord[0]+1, prevCoord[1]])
        if prevY != 1:
            crossboard.append([prevCoord[0], prevCoord[1]-1])
        if prevY != 10:
            crossboard.append([prevCoord[0], prevCoord[1]+1])
        
        coord = random.choice(crossboard)
        crossboard.remove(coord)
        storage.append(crossboard)

        # store the success coordinate
        successHit = []
        successHit.append(prevCoord)
        storage.append(successHit)

        return coord, storage
    
    # test the crossboard until hit again
    elif storage[0] == 2:
        if p1PrevHit:
            # move to step 3
            storage[0] == 3

            prevCoord = p1ShotSeq[-1]
            prevX = prevCoord[0]
            prevY = prevCoord[1]
            prevprevCoord = p1ShotSeq[-2]
            prevprevX = prevprevCoord[0]
            prevprevY = prevprevCoord[1]

            # add success coordinate
            storage[2].append(prevCoord)

            # check it's following the columns or rows
            if prevX == prevprevX:
                # following rows
                for 

            else:
                # followng columns
            



        else:
            crossboard = storage[1]
            coord = random.choice(crossboard)
            crossboard.remove(coord)
            storage[1] = crossboard

            return coord, storage


    # continue hit until both sides are empty
    elif storage[0] == 3:
    # check crossboard (step 3)
    # elif storage[0] == 2:
    #     if p1PrevHit:



    else:
        x = random.randint(1,10)
        y = random.randint(1,10)
        return [x,y], storage