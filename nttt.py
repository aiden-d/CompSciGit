print("Hello, lets plat Tic Tac Toe:\n")
name1 = input("Player 1, enter your name:\n")
name2 = input("Player 2, enter your name:\n")
Board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
Game_Over = False
 
def win1():
                global Game_Over, name1
                print("Game over, "+ name1 +" wins!")
                Game_Over = True
def win2():
                global Game_Over, name2
                print("Game over, "+ name2 +" wins!")
                Game_Over = True
def tie():
                global Game_Over
                print("Tied Game!")
                Game_Over = True
def end_game():
                global Game_Over
                Game_Over = True         
 
while Game_Over == False:
                if (Board[0][0] == "X" and Board[0][1] == "X" and Board[0][2] == "X") or (Board[1][0] == "X" and Board[1][1] == "X" and Board[1][2] == "X") or (Board[2][0] == "X" and Board[2][1] == "X" and Board[2][2] == "X") or (Board[0][0] == "X" and Board[1][0] == "X" and Board[2][0] == "X") or (Board[0][1] == "X" and Board[1][1] == "X" and Board[2][1] == "X") or (Board[0][2] == "X" and Board[1][2] == "X" and Board[2][2] == "X") or (Board[0][0] == "X" and Board[1][1] == "X" and Board[2][2] == "X") or (Board[0][2] == "X" and Board[1][1] == "X" and Board[2][0] == "X"):
                                win1()
                elif (Board[0][0] == "X" or Board[0][0] == "O") and (Board[0][1] == "X" or Board[0][1] == "O") and (Board[0][2] == "X" or Board[0][2] == "O") and (Board[1][0] == "X" or Board[1][0] == "O") and (Board[1][1] == "X" or Board[1][1] == "O") and (Board[1][2] == "X" or Board[1][2] == "O") and (Board[2][0] == "X" or Board[2][0] == "O") and (Board[2][1] == "X" or Board[2][1] == "O") and (Board[2][2] == "X" or Board[2][2] == "O"):
                                tie()
                if (Board[0][0] == "O" and Board[0][1] == "O" and Board[0][2] == "O") or (Board[1][0] == "O" and Board[1][1] == "O" and Board[1][2] == "O") or (Board[2][0] == "O" and Board[2][1] == "O" and Board[2][2] == "O") or (Board[0][0] == "O" and Board[1][0] == "O" and Board[2][0] == "O") or (Board[0][1] == "O" and Board[1][1] == "O" and Board[2][1] == "O") or (Board[0][2] == "O" and Board[1][2] == "O" and Board[2][2] == "O") or (Board[0][0] == "O" and Board[1][1] == "O" and Board[2][2] == "O") or (Board[0][2] == "O" and Board[1][1] == "O" and Board[2][0] == "O"):
                                win2
                elif Game_Over == True:
                                end_game()
               
                row = int(input(name1 + " pick a row number 0-2: \n"))
                column = int(input(name1 +" pick a column number 0-2: \n"))
                if Board[row][column] == "X" or Board[row][column] == "O":  
                                while Board[row][column] == "X" or Board[row][column] == "O":
                                                print("Sorry, cant place here")
                                                row = int(input(name1 + " pick a row number 0-2: \n"))
                                                column = int(input(name1 +" pick a column number 0-2: \n"))
                                else:
                                                Board[row][column] = 'X'
                else:
                                Board[row][column] = 'X'
               
                for row in range(0,3):
                    for column in range(0,3):
                        print(Board[row][column], end=" ")
                    print("\n")
                   
                if (Board[0][0] == "X" and Board[0][1] == "X" and Board[0][2] == "X") or (Board[1][0] == "X" and Board[1][1] == "X" and Board[1][2] == "X") or (Board[2][0] == "X" and Board[2][1] == "X" and Board[2][2] == "X") or (Board[0][0] == "X" and Board[1][0] == "X" and Board[2][0] == "X") or (Board[0][1] == "X" and Board[1][1] == "X" and Board[2][1] == "X") or (Board[0][2] == "X" and Board[1][2] == "X" and Board[2][2] == "X") or (Board[0][0] == "X" and Board[1][1] == "X" and Board[2][2] == "X") or (Board[0][2] == "X" and Board[1][1] == "X" and Board[2][0] == "X"):
                                win1()
                elif (Board[0][0] == "X" or Board[0][0] == "O") and (Board[0][1] == "X" or Board[0][1] == "O") and (Board[0][2] == "X" or Board[0][2] == "O") and (Board[1][0] == "X" or Board[1][0] == "O") and (Board[1][1] == "X" or Board[1][1] == "O") and (Board[1][2] == "X" or Board[1][2] == "O") and (Board[2][0] == "X" or Board[2][0] == "O") and (Board[2][1] == "X" or Board[2][1] == "O") and (Board[2][2] == "X" or Board[2][2] == "O"):
                                tie()
                if (Board[0][0] == "O" and Board[0][1] == "O" and Board[0][2] == "O") or (Board[1][0] == "O" and Board[1][1] == "O" and Board[1][2] == "O") or (Board[2][0] == "O" and Board[2][1] == "O" and Board[2][2] == "O") or (Board[0][0] == "O" and Board[1][0] == "O" and Board[2][0] == "O") or (Board[0][1] == "O" and Board[1][1] == "O" and Board[2][1] == "O") or (Board[0][2] == "O" and Board[1][2] == "O" and Board[2][2] == "O") or (Board[0][0] == "O" and Board[1][1] == "O" and Board[2][2] == "O") or (Board[0][2] == "O" and Board[1][1] == "O" and Board[2][0] == "O"):
                                win2
                elif Game_Over == True:
                                end_game()
               
                row2 = int(input(name2+ " pick a row number 0-2: \n"))
                column2 = int(input(name2+" pick a column number 0-2: \n"))
                if Board[row2][column2] == "O" or Board[row2][column2] == "X":
                                while Board[row2][column2] == "O" or Board[row2][column2] == "X":
                                                print("Sorry, cant place here")
                                                row2 = int(input(name2+ " pick a row number 0-2: \n"))
                                                column2 = int(input(name2+" pick a column number 0-2: \n"))
                                else:
                                                Board[row2][column2] = 'O'
                else:
                    Board[row2][column2] = 'O'
               
                for row2 in range(0,3):
                    for column2 in range(0,3):
                        print(Board[row2][column2], end=" ")
                    print("\n")
else:
                if Game_Over == True:
                                if (Board[0][0] == "X" and Board[0][1] == "X" and Board[0][2] == "X") or (Board[1][0] == "X" and Board[1][1] == "X" and Board[1][2] == "X") or (Board[2][0] == "X" and Board[2][1] == "X" and Board[2][2] == "X") or (Board[0][0] == "X" and Board[1][0] == "X" and Board[2][0] == "X") or (Board[0][1] == "X" and Board[1][1] == "X" and Board[2][1] == "X") or (Board[0][2] == "X" and Board[1][2] == "X" and Board[2][2] == "X") or (Board[0][0] == "X" and Board[1][1] == "X" and Board[2][2] == "X") or (Board[0][2] == "X" and Board[1][1] == "X" and Board[2][0] == "X"):
                                                win1()
                                elif (Board[0][0] == "X" or Board[0][0] == "O") and (Board[0][1] == "X" or Board[0][1] == "O") and (Board[0][2] == "X" or Board[0][2] == "O") and (Board[1][0] == "X" or Board[1][0] == "O") and (Board[1][1] == "X" or Board[1][1] == "O") and (Board[1][2] == "X" or Board[1][2] == "O") and (Board[2][0] == "X" or Board[2][0] == "O") and (Board[2][1] == "X" or Board[2][1] == "O") and (Board[2][2] == "X" or Board[2][2] == "O"):
                                                tie()
                                if (Board[0][0] == "O" and Board[0][1] == "O" and Board[0][2] == "O") or (Board[1][0] == "O" and Board[1][1] == "O" and Board[1][2] == "O") or (Board[2][0] == "O" and Board[2][1] == "O" and Board[2][2] == "O") or (Board[0][0] == "O" and Board[1][0] == "O" and Board[2][0] == "O") or (Board[0][1] == "O" and Board[1][1] == "O" and Board[2][1] == "O") or (Board[0][2] == "O" and Board[1][2] == "O" and Board[2][2] == "O") or (Board[0][0] == "O" and Board[1][1] == "O" and Board[2][2] == "O") or (Board[0][2] == "O" and Board[1][1] == "O" and Board[2][0] == "O"):
                                                win2
                                elif Game_Over == True:
                                                end_game()       