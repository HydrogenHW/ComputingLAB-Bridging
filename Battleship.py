mpSurface:list[list[int]]=[[0 for j in range(10)] for i in range(10)]
mpBelow: list[list[int]]=[[0 for j in range(10)] for i in range(10)]
lengthTable={"Carrier":4,"Submarine":3}
shipTable={"Carrier":6,"Submarine":5}

def isShipValid(x,y,depth,ori,type):
    x=int(x)
    y=int(y)
    boardsize=10
    shipLength=lengthTable[type]

    if ((type=="Carrier"and depth!=0)or(type=="Submarine"))and((ori=="vertical")and(0<=x+shipLength-1 and x+shipLength-1 <boardsize))or((ori=="horizontal")and(0<=y+shipLength-1 and y+shipLength-1 <boardsize))and(ori=="horizontal" or ori=="vertical")and(0<=x and x<boardsize)and(0<=y and y<boardsize):
        print("Valid")
        return True
    else:
        print("Invalid")
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

def placeShip(x,y,depth,ori,type):
    x=int(x)
    y=int(y)
    depth=int(depth)
    if depth==1:
        if ori=="vertical":
            for i in range(0,lengthTable[type]):
                mpSurface[x+i][y]=shipTable[type]
        else:
            for i in range(0,lengthTable[type]):
                mpSurface[x][y+i]=shipTable[type]
    else:
        if ori=="vertical":
            for i in range(0,lengthTable[type]):
                mpBelow[x+i][y]=shipTable[type]
        else:
            for i in range(0,lengthTable[type]):
                mpBelow[x][y+i]=shipTable[type]

print("###PLACING THE SHIPS###")
x,y,depth,ori,type=input("Please input the coord(line,col,depth),ori,type of the ship:").split()
while True:
    if isShipValid(x,y,depth,ori,type):
        placeShip(x,y,depth,ori,type)
        break
    x,y,ori,type=input("Please input the coord(line,col),ori,type of the ship:").split()
    
x,y,depth=input("Input the coord(line,col,depth):").split()
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
