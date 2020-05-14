width = 0
height = 0
path = '-|+'
endPath = 'X'
theSameCells = []
aroundCells = {}
curX = 0
curY = 0
nextX = 0
nextY = 0
prevX = 0
prevY = 0

def line(grid):
    global curX, curY, nextX, nextY, prevX, prevY

    width = len(grid[0])
    height = len(grid) 

    # Find the Beginning
    for i in range(len(grid)):
        for b in range(len(grid[i])):
            if grid[i][b] == 'X':
                curX = i
                curY = b
                prevX = curX
                prevY = curY
                break
    print('The Beginning X on ({};{})'.format(curX, curY))
    # Check around for paths while not ended
    while True:
        print('[NEXT CELL]')
        clearAroundCells()
        
        for i in [-1, 1]:
            for j in [-1, 1]:
                nextX = curX - i
                nextY = curY - j
                # Check for borders 
                if not inBorders(nextX, nextY):
                    continue
                else:
                    # Check around paths
                    if grid[nextX][nextY] in path:
                        # If cell is not the same add to check
                        if not cellIsTheSame(nextX, nextY):
                            addAroundCells(grid[nextX][nextY], nextX, nextY)
        
        print('AROUND CELLS')
        print(aroundCells)
        
        if len(aroundCells) == 0:
            return False

        # Check around cells for next correct path
        if grid[curX][curY] == '-':
            if len(aroundCells < 1):
                return False
            rCell = getCellByDir('r', curX, curY)
            lCell = getCellByDir('l', curX, curY)
            uCell = getCellByDir('u', curX, curY)
            dCell = getCellByDir('d', curX, curY)
            if rCell['img'] == '|' or lCell['img'] == '|':
                return False   
            elif uCell['img'] is not None or dCell['img'] is not None:
                return False
            else:
                if cellIsTheSame(rCell['x'], rCell['y']):
                    moveNext(lCell['x'], lCell['y'])
                elif cellIsTheSame(rCell['x'], rCell['y']) and cellIsTheSame(lCell['x'], lCell['y']):
                    return False
                else:
                    moveNext(rCell['x'], lCell['y'])
        elif grid[x][y] == '|':
            if len(aroundCells) < 1:
                return False
               
        elif grid[x][y] == '+':
            if len(aroundCells) < 2:
                return False
        else:
            pass
                            
    # Or die! ...

def moveNext(newX, newY):
    global curX, curY
    addTheSame(curX, curY)
    curX = newX
    curY = newY

def getCellByDir(direction, x, y):
    cell = { 'img': None, 'x': 0, 'y': 0 }
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

def addAroundCells(img, x, y):
    aroundCells.append({ 'img': img, 'x': x, 'y': y })

def clearAroundCells():
    aroundCells = {}

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