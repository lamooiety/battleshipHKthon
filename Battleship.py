import random
GRIDSIZE = 10

def ShipLogic(round, yourMap, yourHp, enemyHp, p1ShotSeq, p1PrevHit, storage):
    

    # hunting for the battelship
    if not p1PrevHit and (storage == [] or storage[0] == 1):

        # start
        if storage == []:
            storage.append(1)
            # create a heat map
            heat_map = {(x, y): random.random() for x in range(GRIDSIZE) for y in range(GRIDSIZE)}
    
            # Assign values to heat map based on previous shots (higher values for unhit areas).
            for x, y in p1ShotSeq:
                if (x, y) in heat_map:
                    heat_map[(x, y)] += 2
            
            # Assign values to heat map based on remaining HP (higher values for more HP).
            for x in range(GRIDSIZE):
                for y in range(GRIDSIZE):
                    if (x, y) in heat_map:
                        heat_map[(x, y)] += yourHp + enemyHp
            storage.append(heat_map)


        # get available coordinates
        # blackboard = []
        # whiteboard = []
        # for i in range(1, GRIDSIZE+1):
        #     for j in range(1, GRIDSIZE+1):
        #         if (i + j) % 2 == 0:
        #             blackboard.append([i,j]) 
        #         else:
        #             whiteboard.append([i,j])
        
        # for prev in p1ShotSeq:
        #     if prev in blackboard:
        #         blackboard.remove(prev)
        #     else:
        #         whiteboard.remove(prev)

        # # if the blackboard is empty, we have to chooce from the whiteboard
        # if blackboard != []:
        #     coord = random.choice(blackboard)
        # else:
        #     coord = random.choice(whiteboard)

        heat_map = storage[1]
        sorted_coordinates = sorted(heat_map.keys(), key=lambda coord: heat_map[coord], reverse=True)
    
        # Find the best coordinate that hasn't been targeted before.
        for coord in sorted_coordinates:
            if coord not in p1PrevHit:
                return coord

        return coord, storage
    
    # first hit an object
    elif p1PrevHit and (storage == [] or storage[0] == 1):
        # update the storage to step 2
        storage = [2, storage[1]]

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
            return coord, [0, storage[1]]

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
            storage[3].append(prevCoord)

            # back to hunting if it meet the length
            if len(storage[3]) >= 5:
                return p1ShotSeq[-1], [0, storage[1]]


            # check it's following the columns or rows
            # following columns
            if prevX == prevprevX:
                min = 10
                max = 1
                for cod in storage[3]:
                    if cod[1] < min:
                        min = cod[1]
                    if cod[1] > max:
                        max = cod[1]
                
                # check if the both sides are hit or not
                if min == 1 or [prevX, min-1] in p1ShotSeq:
                    if max == 10 or [prevX, max+1] in p1ShotSeq:
                        # back to hunting
                        storage = [0, storage[1]]
                        return [prevX, max+1], storage
                    else:
                        return [prevX, max+1], storage
                else:
                    return [prevX, min-1], storage
                
            # followng rows
            else:
                min = 10
                max = 1
                for cod in storage[3]:
                    if cod[0] < min:
                        min = cod[0]
                    if cod[0] > max:
                        max = cod[0]
                
                # check if the both sides are hit or not
                if min == 1 or [min-1, prevY] in p1ShotSeq:
                    if max == 10 or [max+1, prevY] in p1ShotSeq:
                        # back to hunting
                        return [max+1, prevY], [0, storage[1]]
                    else:
                        return [max+1, prevY], storage
                else:
                    return [min-1, prevY], storage


        # does not hit the crossboard
        else:
            crossboard = storage[2]
            coord = random.choice(crossboard)
            crossboard.remove(coord)

            # make sure it is not hit before
            while (coord in p1ShotSeq and crossboard != []):
                coord = random.choice(crossboard)
                crossboard.remove(coord)
            
            # return to hunt
            if crossboard == []:
                return coord, [0, storage[1]]

            storage[2] = crossboard

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
            storage[3].append(prevCoord)

        # back to hunting if it meet the length
        if len(storage[3]) >= 5:
            return p1ShotSeq[-1], [0, storage[1]]


        # check it's following the columns or rows
        # following columns
        if prevX == prevprevX:
            min = 10
            max = 1
            for cod in storage[3]:
                if cod[1] < min:
                    min = cod[1]
                if cod[1] > max:
                    max = cod[1]
            
            # check if the both sides are hit or not
            if min == 1 or [prevX, min-1] in p1ShotSeq:
                if max == 10 or [prevX, max+1] in p1ShotSeq:
                    # back to hunting
                    storage = [0, storage[1]]
                    return [prevX, max+1], storage
                else:
                    return [prevX, max+1], storage
            else:
                return [prevX, min-1], storage
            
        # followng rows
        else:
            min = 10
            max = 1
            for cod in storage[3]:
                if cod[0] < min:
                    min = cod[0]
                if cod[0] > max:
                    max = cod[0]
            
            # check if the both sides are hit or not
            if min == 1 or [min-1, prevY] in p1ShotSeq:
                if max == 10 or [max+1, prevY] in p1ShotSeq:
                    # back to hunting
                    storage = [0, storage[1]]
                    return [max+1, prevY], storage
                else:
                    return [max+1, prevY], storage
            else:
                return [min-1, prevY], storage

    else:
        x = random.randint(1,10)
        y = random.randint(1,10)
        return [x,y], [0, storage[1]]