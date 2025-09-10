
mp=[[0 for j in range(10)] for i in range(10)]

def isShipValid(x,y,shipLength,ori):
    x=int(x)
    y=int(y)
    boardsize=10

    if ((ori=="horizontal")and(0<=x+shipLength-1 and x+shshipLength-1 <boardsize))or((ori=="vertical")and(0<=y+shipLength-1 and y+shshipLength-1 <boardsize))and(ori=="horizontal" or ori=="vertical")and(0<=x and x<boardsize)and(0<=y and y<boardsize):
       return "Valid"
    else:
        return "Invalid"

def isCoordValid(x,y):
    x=int(x)
    y=int(y)
    print("Valid coord!")
    return (x in range(0,10))and(y in range(0,10))

def printMap():
    for i in range(0,10):
        print(mp[i])

x,y=input("Input the coord(line,col)").split()
x=int(x)
y=int(y)

while True:
    if isCoordValid(x,y):
        mp[x][y]=1
        printMap()
    else:
        x,y=input().split()
