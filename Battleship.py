
mp=[[0 for j in range(10)] for i in range(10)]
lengthTable={"Carrier":4,"Submarine":3}

def isShipValid(x,y,ori,shipLength):
    x=int(x)
    y=int(y)
    boardsize=10

    if ((ori=="horizontal")and(0<=x+shipLength-1 and x+shipLength-1 <boardsize))or((ori=="vertical")and(0<=y+shipLength-1 and y+shipLength-1 <boardsize))and(ori=="horizontal" or ori=="vertical")and(0<=x and x<boardsize)and(0<=y and y<boardsize):
        print("Valid")
        return True
    else:
        print("Invalid")
        return False

def isCoordValid(x,y):
    x=int(x)
    y=int(y)
    print("Valid coord!")
    return (x in range(0,10))and(y in range(0,10))

def printMap():
    for i in range(0,10):
        print(mp[i])

print("###PLACING THE SHIPS###")
x,y,ori,type=input("Please input the coord(line,col),ori,type of the ship:").split()
while True:
    if isShipValid(x,y,ori,lengthTable[type]):
        break
    x,y,ori,type=input("Please input the coord(line,col),ori,type of the ship:").split()
    
x,y=input("Input the coord(line,col):").split()
x=int(x)
y=int(y)

while True:
    if isCoordValid(x,y):
        mp[x][y]=1
        printMap()
        break
    else:
        x,y=input().split()
