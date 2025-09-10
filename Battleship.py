#Definition of Varibles
mpSurface:list[list[int]]=[[0 for j in range(10)] for i in range(10)]
mpBelow: list[list[int]]=[[0 for j in range(10)] for i in range(10)]
lengthTable={"Carrier":4,"Submarine":3}
shipTable={"Carrier":6,"Submarine":5}

#Definition of Functions

def placeShip(x,y,depth,ori,type):
    x=int(x)
    y=int(y)
    depth=int(depth)
    if depth==1:
        if ori=="vertical":
            for i in range(0,lengthTable[type]):
                if mpSurface[x+i][y]==0:
                    mpSurface[x+i][y]=shipTable[type]
                else:
                    return False
        else:
            for i in range(0,lengthTable[type]):
                if mpBelow[x][y+i]==0:
                    mpSurface[x][y+i]=shipTable[type]
                else:
                    return False
    else:
        if ori=="vertical":
            for i in range(0,lengthTable[type]):
                if mpBelow[x+i][y]==0:
                    mpBelow[x+i][y]=shipTable[type]
                else:
                    return False
        else:
            for i in range(0,lengthTable[type]):
                if mpBelow[x][y+i]==0:
                    mpBelow[x][y+i]=shipTable[type]
                else:
                    return False
    return True

def isShipValid(x,y,depth,ori,type):
    x=int(x)
    y=int(y)
    boardsize=10
    shipLength=lengthTable[type]

    if ((type=="Carrier"and depth!=0)or(type=="Submarine"))and((ori=="vertical")and(0<=x+shipLength-1 and x+shipLength-1 <boardsize))or((ori=="horizontal")and(0<=y+shipLength-1 and y+shipLength-1 <boardsize))and(ori=="horizontal" or ori=="vertical")and(0<=x and x<boardsize)and(0<=y and y<boardsize):
        print("Valid Coord...Placing Ship")
        return placeShip(x,y,depth,ori,type)
    else:
        print("Invalid Coord!")
        return False

def isCoordValid(x,y,depth):
    x=int(x)
    y=int(y)
    depth=int(depth)
    return (x in range(0,10))and(y in range(0,10))and(depth in range(0,2))

def printMap():
    print("Surface")
    for i in range(0,10):
        print(mpSurface[i])
    print("Below")
    for i in range(0,10):
        print(mpBelow[i])


# noinspection PyShadowingNames
def getInitInput():
    print("--------========####BATTLESHIP_GAME####========--------")
    x,y,depth,ori =input('Please enter coord of Carrier (line, col, depth) and orientation(vertical/horizontal): ').split()
    while True:
        if isShipValid(x, y, depth, ori,"Carrier"):
            print("Carrier placed")
            break
        x,y,depth,ori = input('Please enter coord of Carrier (line, col, depth) and orientation(vertical/horizontal): ').split()
    x,y,depth,ori = input('Please enter coord of Carrier (line, col, depth) and orientation(vertical/horizontal): ').split()
    while True:
        if isShipValid(x, y, depth, ori, "Submarine"):
            print("Submarine placed")
            break
        x,y,depth,ori = input('Please enter coord of Carrier (line, col, depth) and orientation(vertical/horizontal): ').split()


#Main programme starts here
getInitInput()
x,y,depth=input("Input the attack coord(line,col,depth):").split()
x=int(x)
y=int(y)
depth=int(depth)

while True:
    if isCoordValid(x,y,depth):
        if depth==1:
            mpSurface[x][y]=1
        else:
            mpBelow[x][y]=1
        printMap()
        break
    else:
        x,y,depth=input("Input the coord(line,col,depth):").split()
        x=int(x)
        y=int(y)
        depth=int(depth)
