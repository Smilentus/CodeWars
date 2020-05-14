width = 0
height = 0
path = '-|+'
startEndPath = 'X'
theSameCells = []
aroundCells = 0
lastCrossX = 0
lastCrossY = 0
curX = 0
curY = 0
nextX = 0
nextY = 0
prevX = 0
prevY = 0

def line(grid):
    global curX, curY, nextX, nextY, prevX, prevY, path, theSameCells, aroundCells, width, height, startEndPath, lastCrossX, lastCrossY

    grid = grid.reverse()

    width = len(grid[0])
    height = len(grid) 

    # Find the Beginning
    for i in range(len(grid)):
        for b in range(len(grid[i])):
            if grid[i][b] == startEndPath:
                curX = i
                curY = b
                prevX = curX
                prevY = curY
                addTheSame(curX, curY)
                break
    print('The Beginning X on ({};{})'.format(curX, curY))
    # Check around for paths while not ended
    while True:
        print('[NEXT CELL]')
        clearAroundCells()
        
        # for i in [-1, 0, 1]:
        #     for j in [-1, 0, 1]:
        #         nextX = curX - i
        #         nextY = curY - j
        #         # Check for borders 
        #         if not inBorders(nextX, nextY):
        #             continue
        #         else:
        #             # Check around paths
        #             if grid[nextX][nextY] in path:
        #                 # If cell is not the same add to check
        #                 if not cellIsTheSame(nextX, nextY):
        #                     addAroundCells(grid[nextX][nextY], nextX, nextY)
        

        # Get around cells
        rCell = getCellByDir('r', curX, curY)
        lCell = getCellByDir('l', curX, curY)
        uCell = getCellByDir('u', curX, curY)
        dCell = getCellByDir('d', curX, curY)

        if rCell['img'] is not ' ':
            aroundCells += 1
        if lCell['img'] is not ' ':
            aroundCells += 1
        if uCell['img'] is not ' ':
            aroundCells += 1
        if dCell['img'] is not ' ':
            aroundCells += 1

        print('AROUND CELLS')
        print('Counter: {}'.format(aroundCells))
        print(rCell)
        print(lCell)
        print(uCell)
        print(dCell)

        if aroundCells == 0:
            return False

        # Check around cells for next correct path
        if grid[curX][curY] == '-':
            if aroundCells < 1:
                return False
            if rCell['img'] == '|' or lCell['img'] == '|':
                return False   
            if uCell['img'] is not ' ' or dCell['img'] is not ' ':
                return False
            if cellIsTheSame(rCell['x'], rCell['y']) and cellIsTheSame(lCell['x'], lCell['y']):
                return False
            elif cellIsTheSame(rCell['x'], rCell['y']):
                moveNext(lCell['x'], lCell['y'])
            else:
                moveNext(rCell['x'], lCell['y'])
                
        elif grid[curX][curY] == '|':
            if aroundCells < 1:
                return False
            if rCell['img'] is not ' ' or lCell['img'] is not ' ':
                return False
            if uCell['img'] == '-' or dCell['img'] == '-':
                return False
            if cellIsTheSame(uCell['x'], uCell['y']) and cellIsTheSame(dCell['x'], dCell['y']):
                return False
            elif cellIsTheSame(dCell['x'], dCell['y']):
                moveNext(uCell['x'], uCell['y'])
            else:
                moveNext(dCell['x'], dCell['y'])

        elif grid[curX][curY] == '+':
            if aroundCells < 2:
                return False
            if uCell['img'] in '-' or rCell['img'] in '|' or dCell['img'] in '-' or lCell['img'] in '|':
                return False
            if cellIsTheSame(uCell['x'], uCell['y']) and cellIsTheSame(dCell['x'], dCell['y']) and cellIsTheSame(lCell['x'], lCell['y']) and cellIsTheSame(rCell['x'], rCell['y']):
                return False

        else: # Means the Beginning => X
            if aroundCells == 0:
                return False
            if uCell['img'] in '-' or rCell['img'] in '|' or dCell['img'] in '-' or lCell['img'] in '|':
                return False 
            if uCell['img'] is not ' ':
                moveNext(uCell['x'], uCell['y'])
            elif dCell['img'] is not ' ':
                moveNext(dCell['x'], dCell['y'])
            elif lCell['img'] is not ' ':
                moveNext(lCell['x'], lCell['y'])
            elif rCell['img'] is not ' ':
                moveNext(rCell['x'], rCell['y'])
                            
    # Or die! ...
    return True

def moveNext(newX, newY):
    global curX, curY, prevX, prevY
    addTheSame(curX, curY)
    prevX = curX
    prevY = curY
    curX = newX
    curY = newY
    print('Moved from [{}] ({}:{}) to [{}] ({};{})'.format(grid[prevX][prevY], prevX, prevY, grid[newX][newY], curX, curY))

def getCellByDir(direction, x, y):
    cell = { 'img': ' ', 'x': 0, 'y': 0 }
    if direction == 'r':
        if inBorders(x + 1, y):
            cell['x'] = x + 1
            cell['y'] = y
            cell['img'] = grid[x + 1][y]
    elif direction == 'l':
        if inBorders(x - 1, y):
            cell['x'] = x - 1
            cell['y'] = y
            cell['img'] = grid[x - 1][y]
    elif direction == 'u':
        if inBorders(x, y - 1):
            cell['x'] = x
            cell['y'] = y - 1
            cell['img'] = grid[x][y - 1]
    elif direction == 'd':
        if inBorders(x, y + 1):
            cell['x'] = x
            cell['y'] = y + 1
            cell['img'] = grid[x][y + 1]
            
    return cell

def cellIsTheSame(x, y):
    for cell in theSameCells:
        if cell[0] == x and cell[1] == y:
            return True
    return False

def addTheSame(x, y):
    theSameCells.append([x, y])

def clearAroundCells():
    aroundCells = 0

def inBorders(x, y):
    if x < 0 or x >= width or y < 0 or y >= height:
        return False
    else:
        return True

grid = ["           ",
        "X---------X",
        "           ",
        "           "]
print(line(grid))