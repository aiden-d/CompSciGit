row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']
rows = [row1, row2, row3]
player1 = ""
player2 = ""
players = [player1,player2]
letter = ['X','O']
gameOver = False
PlayerTurn = 0
message = None
def clearTerminal():
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')
def setup():
    clearTerminal()
    global row1
    global row2
    global row3
    global player1
    global player2
    global players
    row1 = [0, 0, 0]
    row2 = [0, 0, 0]
    row3 = [0, 0, 0]
    print("Hi! Welcome to Python Tic Tac Toe!")
    player1 = input("Please enter the name for player 1 (X): ")
    player2 = input("Please enter the name for player 2 (O): ")
    players = [player1,player2]
def printBoard():
    global row1
    global row2
    global row3
    print("  c1 c2 c3")
    i = 1
    for row in rows:
        s = "r"+ str(i) + " |"
        i += 1
        for x in row:
            s1 = str(x) + "|"
            s += s1
        print(s)

    
def checkIfSame(array,l):
    win = True
    for i in array:
        if (i != l):
            win = False
    return win
    
    


def checkWin(r,c):
    global rows, PlayerTurn, letter,  rows
    row1 = rows[0]
    row2 = rows[1]
    row3 = rows[2]
    l = letter[PlayerTurn]
    currentRow = rows[r]
    column = [row1[c], row2[c], row3[c]]
    
    diagonal1 = [row1[0], row2[1], row3[2]]
    diagonal2 = [row1[2], row2[1], row3[0]]

    win = checkIfSame(currentRow,l)
    if (win == True): return True

    win = checkIfSame(column,l)
    if (win == True): return True

    win = checkIfSame(diagonal1,l)
    if (win == True): return True

    win = checkIfSame(diagonal2,l)
    if (win == True): return True
    print("false")
    return False
    
def checkDraw():
    global rows
    row1 = rows[0]
    row2 = rows[1]
    row2 = rows[2]
    full = True
    for i in row1:
        if i == " ":
            full = False
            return full
    for i in row2:
        if i == " ":
            full = False
            return full
    for i in row3:
        if i == " ":
            full = False
            return full

        


clearTerminal()
setup()
printBoard()

while gameOver != True:
    clearTerminal()
    if (message!= None):
        print(message)
        message = None
    printBoard()
    s1 = players[PlayerTurn] +"(" +letter[PlayerTurn] + "). What is your next move, which row number (eg: 1,2, or 3)?"
    rNum = input(s1)
    if rNum == "reset":
        setup()
    s2 = players[PlayerTurn] +"(" +letter[PlayerTurn] + "). What is your next move, which column number (eg: 1,2 or 3)?"
    cNum = input(s2)
    
    rNum = int(rNum)
    cNum = int(cNum)
    if cNum>3 or cNum<0 or rNum>3 or rNum<0:
        message = "Invalid move, try again..."
    elif rows[rNum-1][cNum-1] != " ":
        message = "Invalid move, try again..."
    else:
        rows[rNum-1][cNum-1] = letter[PlayerTurn]
        if (checkWin(rNum-1,cNum-1)):
            clearTerminal()
            printBoard()
            print(players[PlayerTurn], " Won!")
            gameOver = True
        if (checkDraw()):
            clearTerminal()
            printBoard()
            print("Draw")
            gameOver = True
        if PlayerTurn==0:
            PlayerTurn+=1
        else:
            PlayerTurn-=1




