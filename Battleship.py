from random import randint

#Definition of Varibles
isPrinted=[False,False,False,False]
mpSurface:list[list[int]]=[[0 for j in range(10)] for i in range(10)]
mpBelow: list[list[int]]=[[0 for j in range(10)] for i in range(10)]
lengthTable={"Carrier":4,"Submarine":3}
shipTable={"Carrier":'C',"Submarine":'S'}

#Definition of Functions
def isupper(s):
    return s.isupper()

def checkShip(x,y,depth,ori,type):
    x = int(x)
    y = int(y)
    depth = int(depth)
    if depth == 1:
        if ori == "vertical":
            for i in range(0, lengthTable[type]):
                if mpSurface[x + i][y] != 0:
                    return False
        else:
            for i in range(0, lengthTable[type]):
                if mpBelow[x][y + i] != 0:
                    return False
    else:
        if ori == "vertical":
            for i in range(0, lengthTable[type]):
                if mpBelow[x + i][y] != 0:
                    return False
        else:
            for i in range(0, lengthTable[type]):
                if mpBelow[x][y + i] != 0:
                    return False
    return True

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
    return True

def placeBotShip(x,y,depth,ori,type):
    x = int(x)
    y = int(y)
    depth = int(depth)
    if depth == 1:
        if ori == "vertical":
            for i in range(0, lengthTable[type]):
                mpSurface[x + i][y] = shipTable[type].casefold()
        else:
            for i in range(0, lengthTable[type]):
                mpSurface[x][y + i] = shipTable[type].casefold()
    else:
        if ori == "vertical":
            for i in range(0, lengthTable[type]):
                mpBelow[x + i][y] = shipTable[type].casefold()
        else:
            for i in range(0, lengthTable[type]):
                mpBelow[x][y + i] = shipTable[type].casefold()
    return True

def isShipValid(x,y,depth,ori,type):
    x=int(x)
    y=int(y)
    boardsize=10
    shipLength=lengthTable[type]

    if ((type=="Carrier"and depth!=0)or(type=="Submarine"))and((ori=="vertical")and(0<=x+shipLength-1 and x+shipLength-1 <boardsize))or((ori=="horizontal")and(0<=y+shipLength-1 and y+shipLength-1 <boardsize))and(ori=="horizontal" or ori=="vertical")and(0<=x and x<boardsize)and(0<=y and y<boardsize):
        if checkShip(x,y,depth,ori,type):
            placeShip(x,y,depth,ori,type)
            return True
        else:
            return False
    else:
        return False

def isBotShipValid(x,y,depth,ori,type):
    x = int(x)
    y = int(y)
    boardsize = 10
    shipLength = lengthTable[type]

    if ((type == "Carrier" and depth != 0) or (type == "Submarine")) and (
            (ori == "vertical") and (0 <= x + shipLength - 1 and x + shipLength - 1 < boardsize)) or (
            (ori == "horizontal") and (0 <= y + shipLength - 1 and y + shipLength - 1 < boardsize)) and (
            ori == "horizontal" or ori == "vertical") and (0 <= x and x < boardsize) and (0 <= y and y < boardsize):
        if checkShip(x, y, depth, ori, type):
            placeBotShip(x, y, depth, ori, type)
            return True
        else:
            return False
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
        for j in range(0,10):
            print(mpSurface[i][j],end=" ")
        print("", end="\n")
    print("Below\n")
    for i in range(0,10):
        for j in range(0,10):
            print(mpBelow[i][j],end=" ")
        print("",end="\n")

def getUserAttack():
    x, y, depth = input("Input the attack coord(line,col,depth):").split()
    x = int(x)
    y = int(y)
    depth = int(depth)
    while True:
        if isCoordValid(x, y, depth):
            if depth == 1:
                # mpSurface[x][y]=1
                if mpSurface[x][y] != 0 and isupper(mpSurface[x][y])==False:
                    print(f"Hit@{x},{y},{depth}!")
                    mpSurface[x][y] = 1
                elif mpSurface[x][y] != 0 and isupper(mpSurface[x][y])==True:
                    print("Watch Your Fire! You Hit Yourself!")
                else:
                    print("Attack Miss!")
            else:
                #mpBelow[x][y] = 1
                if mpBelow[x][y] != 0 and isupper(mpBelow[x][y])==False:
                    print(f"Hit@{x},{y},{depth}!")
                    mpBelow[x][y] = 1
                elif mpBelow[x][y] != 0 and isupper(mpBelow[x][y])==True:
                    print("Watch Your Fire! You Hit Yourself!")
                else:
                    print("Attack Miss!")
            break
        else:
            x, y, depth = input("Input the coord(line,col,depth):").split()
            x = int(x)
            y = int(y)
            depth = int(depth)

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

def checkMap():
    flagBotCarrier,flagBotSubmarine,flagUserCarrier,flagUserSubmarine=False,False,False,False
    for i in range(0,10):
        for j in range(0,10):
            if mpSurface[i][j]=='C':
                flagUserCarrier=True
            elif mpSurface[i][j]=='S':
                flagUserSubmarine=True
            elif mpSurface[i][j]=='c':
                flagBotCarrier=True
            elif mpSurface[i][j]=='s':
                flagBotSubmarine=True
    for i in range(0,10):
        for j in range(0,10):
            if mpBelow[i][j]=='C':
                flagUserCarrier=True
            elif mpBelow[i][j]=='S':
                flagUserSubmarine=True
            elif mpBelow[i][j]=='c':
                flagBotCarrier=True
            elif mpBelow[i][j]=='s':
                flagBotSubmarine=True

    if flagBotCarrier==False and isPrinted[0]==False:
        print("Bot Carrier has sunk")
        isPrinted[0]=False
    elif flagBotSubmarine==False and isPrinted[1]==False:
        print("Bot Submarine has sunk")
        isPrinted[1]=False
    elif flagUserCarrier==False and isPrinted[2]==False:
        isPrinted[2]=False
        print("User Carrier has sunk")
    elif flagUserSubmarine==False and isPrinted[3]==False:
        isPrinted[3]=False
        print("User Submarine has sunk")
    if flagBotCarrier==False and flagBotSubmarine==False:
        print("You win!")
        return True
    if flagUserCarrier==False and flagUserSubmarine==False:
        print("You lose!")
        return False
    return None

def getBotShip():
    print("[Bot]Placing ship")
    x, y, depth = randint(0,9),randint(0,9),randint(0,1)
    ori=randint(0,1)
    if ori==0:
        ori="vertical"
    else:
        ori="horizontal"
    while True:
        if isBotShipValid(x, y, depth, ori, "Carrier"):
            print("[Bot]Carrier placed")
            break
        x, y, depth = randint(0, 9), randint(0, 9), randint(0, 1)
        ori = randint(0, 1)
        if ori == 0:
            ori = "vertical"
        else:
            ori = "horizontal"
    x, y, depth = randint(0, 9), randint(0, 9), randint(0, 1)
    ori = randint(0, 1)
    if ori == 0:
        ori = "vertical"
    else:
        ori = "horizontal"
    while True:
        if isBotShipValid(x, y, depth, ori, "Submarine"):
            print("[Bot]Submarine placed")
            break
        x, y, depth = randint(0, 9), randint(0, 9), randint(0, 1)
        ori = randint(0, 1)
        if ori == 0:
            ori = "vertical"
        else:
            ori = "horizontal"

def getBotAttack():
    x, y, depth = randint(0,9),randint(0,9),randint(0,1)
    while True:
        if isCoordValid(x, y, depth):
            if depth == 1:
                # mpSurface[x][y]=1
                if mpSurface[x][y] != 0 and isupper(mpSurface[x][y]) == True:
                    print(f"[Bot]Hit@{x},{y},{depth}!")
                    mpSurface[x][y] = 1
                elif mpSurface[x][y] != 0 and isupper(mpSurface[x][y]) == False:
                    print("[Bot]Watch Your Fire! You Hit Yourself!")
                else:
                    print("[Bot]Attack Miss!")
            else:
                # mpBelow[x][y] = 1
                if mpBelow[x][y] != 0 and isupper(mpBelow[x][y]) == True:
                    print(f"[Bot]Hit@{x},{y},{depth}!")
                    mpBelow[x][y] = 1
                elif mpBelow[x][y] != 0 and isupper(mpBelow[x][y]) == False:
                    print("[Bot]Watch Your Fire! You Hit Yourself!")
                else:
                    print("[Bot]Attack Miss!")
            break
        else:
            x, y, depth = randint(0,9),randint(0,9),randint(0,1)

#Main programme starts here
getInitInput()
getBotShip()
printMap()
while True:
    getUserAttack()
    getBotAttack()
    if checkMap() is not None:
        break
