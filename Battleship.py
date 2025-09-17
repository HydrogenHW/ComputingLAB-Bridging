#Code by Hydrogen_HW
#还原侧身，以玄鸟之资缤纷此尘荏#

#Imports
from random import randint

#Definition of Varibles
isPrinted=[False,False,False,False]
mpSurface:list[list[int]]=[[0 for j in range(10)] for i in range(10)]
mpBelow: list[list[int]]=[[0 for j in range(10)] for i in range(10)]
lengthTable={"Carrier":4,"Submarine":3}
shipTable={"Carrier":'C',"Submarine":'S'}
difficulty=1

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
        print("Invalid ship input!")
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
    print("\nBelow")
    for i in range(0,10):
        for j in range(0,10):
            print(mpBelow[i][j],end=" ")
        print("",end="\n")

def findBot(x,y,depth):
    if depth==0:
        if isCoordValid(x+1, y, depth):
            if mpBelow[x+1][y] in ['c','s'] and isupper(mpBelow[x+1][y]) == False:
                print(f"[System]Enemy detected around {x},{y},{depth}!")
                return True
        if isCoordValid(x+1, y+1, depth):
            if mpBelow[x+1][y+1] in ['c','s'] and isupper(mpBelow[x+1][y+1]) == False:
                print(f"[System]Enemy detected around {x},{y},{depth}!")
                return True
        if isCoordValid(x+1, y-1, depth):
            if mpBelow[x+1][y-1] in ['c','s'] and isupper(mpBelow[x+1][y-1]) == False:
                print(f"[System]Enemy detected around {x},{y},{depth}!")
                return True
        if isCoordValid(x, y+1, depth):
            if mpBelow[x][y+1] in ['c','s'] and isupper(mpBelow[x][y+1]) == False:
                print(f"[System]Enemy detected around {x},{y},{depth}!")
                return True
        if isCoordValid(x, y-1, depth):
            if mpBelow[x][y-1] in ['c','s'] and isupper(mpBelow[x][y-1]) == False:
                print(f"[System]Enemy detected around {x},{y},{depth}!")
                return True
        if isCoordValid(x-1, y, depth):
            if mpBelow[x-1][y] in ['c','s'] and isupper(mpBelow[x-1][y]) == False:
                print(f"[System]Enemy detected around {x},{y},{depth}!")
                return True
        if isCoordValid(x-1, y+1, depth):
            if mpBelow[x-1][y+1] in ['c','s'] and isupper(mpBelow[x-1][y+1]) == False:
                print(f"[System]Enemy detected around {x},{y},{depth}!")
                return True
        if isCoordValid(x-1, y-1, depth):
            if mpBelow[x-1][y-1] in ['c','s'] and isupper(mpBelow[x-1][y-1]) == False:
                print(f"[System]Enemy detected around {x},{y},{depth}!")
                return True
    else:
        if isCoordValid(x+1, y, depth):
            if mpSurface[x+1][y] in ['c','s'] and isupper(mpSurface[x+1][y]) == False:
                print(f"[System]Enemy detected around {x},{y},{depth}!")
                return True
        if isCoordValid(x+1, y+1, depth):
            if mpSurface[x+1][y+1] in ['c','s'] and isupper(mpSurface[x+1][y+1]) == False:
                print(f"[System]Enemy detected around {x},{y},{depth}!")
                return True
        if isCoordValid(x+1, y-1, depth):
            if mpSurface[x+1][y-1] in ['c','s'] and isupper(mpSurface[x+1][y-1]) == False:
                print(f"[System]Enemy detected around {x},{y},{depth}!")
                return True
        if isCoordValid(x, y+1, depth):
            if mpSurface[x][y+1] in ['c','s'] and isupper(mpSurface[x][y+1]) == False:
                print(f"[System]Enemy detected around {x},{y},{depth}!")
                return True
        if isCoordValid(x, y-1, depth):
            if mpSurface[x][y-1] in ['c','s'] and isupper(mpSurface[x][y-1]) == False:
                print(f"[System]Enemy detected around {x},{y},{depth}!")
                return True
        if isCoordValid(x-1, y, depth):
            if mpSurface[x-1][y] in ['c','s'] and isupper(mpSurface[x-1][y]) == False:
                print(f"[System]Enemy detected around {x},{y},{depth}!")
                return True
        if isCoordValid(x-1, y+1, depth):
            if mpSurface[x-1][y+1] in ['c','s'] and isupper(mpSurface[x-1][y+1]) == False:
                print(f"[System]Enemy detected around {x},{y},{depth}!")
                return True
        if isCoordValid(x-1, y-1, depth):
            if mpSurface[x-1][y-1] in ['c','s'] and isupper(mpSurface[x-1][y-1]) == False:
                print(f"[System]Enemy detected around {x},{y},{depth}!")
                return True
    return False

def getUserAttack():
    x, y, depth = input("[System]Input the attack coord(line,col,depth):").split()
    x = int(x)
    y = int(y)
    depth = int(depth)
    while True:
        if isCoordValid(x, y, depth):
            if depth == 1:
                # mpSurface[x][y]=1
                if mpSurface[x][y] != 0 and isupper(mpSurface[x][y])==False and mpSurface[x][y] != 'X' and mpSurface[x][y] != 'x':
                    print(f"[System]Hit @ {x},{y},{depth}!")
                    mpSurface[x][y] = 'X'
                elif mpSurface[x][y] != 0 and isupper(mpSurface[x][y])==True and mpSurface[x][y] != 'X' and mpSurface[x][y] != 'x':
                    print("[System]Watch Your Fire! You Hit Yourself!")
                else:
                    print("[User]Attack Miss!")
                    if not findBot(x, y, depth):
                        print("[System]Nothing Found!")
            else:
                #mpBelow[x][y] = 1
                if mpBelow[x][y] != 0 and isupper(mpBelow[x][y])==False and mpBelow[x][y] != 'X' and mpBelow[x][y] != 'x':
                    print(f"[System]Hit@{x},{y},{depth}!")
                    mpBelow[x][y] = 'X'
                elif mpBelow[x][y] != 0 and isupper(mpBelow[x][y])==True and mpBelow[x][y] != 'X' and mpBelow[x][y] != 'x':
                    print("[System]Watch Your Fire! You Hit Yourself!")
                else:
                    print("[User]Attack Miss!")
                    if not findBot(x, y, depth):
                        print("[System]Nothing Found!")
            break
        else:
            x, y, depth = input("[System]Invalid value! Input the coord again(line,col,depth):").split()
            x = int(x)
            y = int(y)
            depth = int(depth)

# noinspection PyShadowingNames
def getInitInput():
    print("--------========================####BATTLESHIP_GAME####========================--------")

    difficulty=int(input("[System]Input the difficulty level(1-114):"))
    difficulty=max(difficulty,1)

    x,y,depth,ori =input('[System]Please enter coord of Carrier (line, col, depth) \nand orientation(vertical/horizontal): ').split()
    while True:
        if isShipValid(x, y, depth, ori,"Carrier"):
            print("[User]Carrier placed")
            break
        x,y,depth,ori = input('[System]Please enter coord of Carrier (line, col, depth) \nand orientation(vertical/horizontal): ').split()
    x,y,depth,ori = input('[System]Please enter coord of Submarine (line, col, depth) \nand orientation(vertical/horizontal): ').split()
    while True:
        if isShipValid(x, y, depth, ori, "Submarine"):
            print("[User]Submarine placed")
            break
        x,y,depth,ori = input('[System]Please enter coord of Carrier (line, col, depth) \nand orientation(vertical/horizontal): ').split()
    return difficulty

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
        print("[System]Bot Carrier has sunk")
        isPrinted[0]=True
    elif flagBotSubmarine==False and isPrinted[1]==False:
        print("[System]Bot Submarine has sunk")
        isPrinted[1]=True
    elif flagUserCarrier==False and isPrinted[2]==False:
        isPrinted[2]=True
        print("[System]User Carrier has sunk")
    elif flagUserSubmarine==False and isPrinted[3]==False:
        isPrinted[3]=True
        print("[System]User Submarine has sunk")
    if flagBotCarrier==False and flagBotSubmarine==False:
        return True
    if flagUserCarrier==False and flagUserSubmarine==False:
        return False
    return None

def getBotShip():
    print("[Bot]Placing ship")
    x, y, depth = randint(0,9),randint(0,9),1
    ori=randint(0,1)
    if ori==0:
        ori="vertical"
    else:
        ori="horizontal"
    while True:
        if isBotShipValid(x, y, depth, ori, "Carrier"):
            print("[Bot]Carrier placed")
            break
        x, y, depth = randint(0, 9), randint(0, 9), 1
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
    x,y,depth = 0,0,0
    forceHit=randint(0,114)
    if forceHit<=difficulty:
        print("[Bot]Hacking")
        depth=randint(0,1)
        if depth==0:
            for i in range(0,10):
                f=True
                for j in range(0,10):
                    if mpBelow[i][j]=="C" or mpBelow[i][j]=="S":
                        x=i
                        y=j
                        f=False
                        break
                if f==False:
                    break
        else:
            for i in range(0,10):
                f=True
                for j in range(0,10):
                    if mpSurface[i][j]=="C" or mpSurface[i][j]=="S":
                        x=i
                        y=j
                        f=False
                        break
                if f==False:
                    break
    else:
        x, y, depth = randint(0,9),randint(0,9),randint(0,1)
    if x==0 and y==0:
        print("[Bot]Fail to hack :-(")
        x, y, depth = randint(0, 9), randint(0, 9), randint(0, 1)
    while True:
        if isCoordValid(x, y, depth):
            if depth == 1:
                # mpSurface[x][y]=1
                if mpSurface[x][y] != 0 and isupper(mpSurface[x][y]) == True and mpSurface[x][y] != 'X' and mpSurface[x][y] != 'x':
                    print(f"[Bot]Hit@{x},{y},{depth}!")
                    mpSurface[x][y] = 'x'
                elif mpSurface[x][y] != 0 and isupper(mpSurface[x][y]) == False and mpSurface[x][y] != 'X' and mpSurface[x][y] != 'x':
                    print("[Bot]Watch Your Fire! You Hit Yourself!")
                else:
                    print(f"[Bot]Attack Miss @ {x},{y},{depth}!")
            else:
                # mpBelow[x][y] = 1
                if mpBelow[x][y] != 0 and isupper(mpBelow[x][y]) == True and mpBelow[x][y] != 'X' and mpBelow[x][y] != 'x':
                    print(f"[Bot]Hit@{x},{y},{depth}!")
                    mpBelow[x][y] = 'x'
                elif mpBelow[x][y] != 0 and isupper(mpBelow[x][y]) == False and mpBelow[x][y] != 'X' and mpBelow[x][y] != 'x':
                    print("[Bot]Watch Your Fire! You Hit Yourself!")
                else:
                    print(f"[Bot]Attack Miss @ {x},{y},{depth}!")
            break
        else:
            x, y, depth = randint(0,9),randint(0,9),randint(0,1)

#Main programme starts here
difficulty=getInitInput()
print("[User]This is your map")
printMap()
getBotShip()
# printMap()
while True:
    getUserAttack()
    getBotAttack()
    res=checkMap()
    if res is True:
        printMap()
        print("[System]You win!")
        break
    if res is False:
        printMap()
        print("[System]You lose!")
        break