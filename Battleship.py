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

        # make sure it is not hit before
        while (coord in p1ShotSeq and crossboard != []):
            coord = random.choice(crossboard)
            crossboard.remove(coord)

        # return to hunt
        if crossboard == []:
            return coord, []

        storage.append(crossboard)

        # store the success coordinate
        successHit = []
        successHit.append(prevCoord)
        storage.append(successHit)

        return coord, storage
    
    # test the crossboard until hit again
    elif storage[0] == 2:

        # hit the crossboard
        if p1PrevHit:
            # move to step 3
            storage[0] = 3

            prevCoord = p1ShotSeq[-1]
            prevX = prevCoord[0]
            prevY = prevCoord[1]
            prevprevCoord = p1ShotSeq[-2]
            prevprevX = prevprevCoord[0]
            prevprevY = prevprevCoord[1]

            # add success coordinate
            storage[2].append(prevCoord)

            # back to hunting if it meet the length
            if len(storage[2]) >= 5:
                return p1ShotSeq[-1], []


            # check it's following the columns or rows
            # following columns
            if prevX == prevprevX:
                min = 10
                max = 1
                for cod in storage[2]:
                    if cod[1] < min:
                        min = cod[1]
                    if cod[1] > max:
                        max = cod[1]
                
                # check if the both sides are hit or not
                if min == 1 or [prevX, min-1] in p1ShotSeq:
                    if max == 10 or [prevX, max+1] in p1ShotSeq:
                        # back to hunting
                        storage = []
                        return [prevX, max+1], storage
                    else:
                        return [prevX, max+1], storage
                else:
                    return [prevX, min-1], storage
                
            # followng rows
            else:
                min = 10
                max = 1
                for cod in storage[2]:
                    if cod[0] < min:
                        min = cod[0]
                    if cod[0] > max:
                        max = cod[0]
                
                # check if the both sides are hit or not
                if min == 1 or [min-1, prevY] in p1ShotSeq:
                    if max == 10 or [max+1, prevY] in p1ShotSeq:
                        # back to hunting
                        return [max+1, prevY], []
                    else:
                        return [max+1, prevY], storage
                else:
                    return [min-1, prevY], storage


        # does not hit the crossboard
        else:
            crossboard = storage[1]
            coord = random.choice(crossboard)
            crossboard.remove(coord)

            # make sure it is not hit before
            while (coord in p1ShotSeq and crossboard != []):
                coord = random.choice(crossboard)
                crossboard.remove(coord)
            
            # return to hunt
            if crossboard == []:
                return coord, []

            storage[1] = crossboard

            return coord, storage


    # continue hit until both sides are empty
    elif storage[0] == 3:

        # hit the side
        prevCoord = p1ShotSeq[-1]
        prevX = prevCoord[0]
        prevY = prevCoord[1]
        prevprevCoord = p1ShotSeq[-2]
        prevprevX = prevprevCoord[0]
        prevprevY = prevprevCoord[1]

        # add success coordinate
        if p1PrevHit:
            storage[2].append(prevCoord)

        # back to hunting if it meet the length
        if len(storage[2]) >= 5:
            return p1ShotSeq[-1], []


        # check it's following the columns or rows
        # following columns
        if prevX == prevprevX:
            min = 10
            max = 1
            for cod in storage[2]:
                if cod[1] < min:
                    min = cod[1]
                if cod[1] > max:
                    max = cod[1]
            
            # check if the both sides are hit or not
            if min == 1 or [prevX, min-1] in p1ShotSeq:
                if max == 10 or [prevX, max+1] in p1ShotSeq:
                    # back to hunting
                    storage = []
                    return [prevX, max+1], storage
                else:
                    return [prevX, max+1], storage
            else:
                return [prevX, min-1], storage
            
        # followng rows
        else:
            min = 10
            max = 1
            for cod in storage[2]:
                if cod[0] < min:
                    min = cod[0]
                if cod[0] > max:
                    max = cod[0]
            
            # check if the both sides are hit or not
            if min == 1 or [min-1, prevY] in p1ShotSeq:
                if max == 10 or [max+1, prevY] in p1ShotSeq:
                    # back to hunting
                    storage = []
                    return [max+1, prevY], storage
                else:
                    return [max+1, prevY], storage
            else:
                return [min-1, prevY], storage

    else:
        x = random.randint(1,10)
        y = random.randint(1,10)
        return [x,y], []