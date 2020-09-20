import os
import sys
import random


Rooms = [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
         (0, 2), (1, 2), (2, 2), (3, 3), (4, 4),
         (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),]
         
room = 2
floor = 1
sword = "sword"
monster = "monster"
magicstone = "magicstone"
ladderUp = "lUp"
ladderDown = "lDown"
nothing = "n"
bossmonster = "bossmonster"
inventory = "i"
yes = "y"
no = "n"
items = []
board = [ [sword,monster,monster,monster,ladderUp], [ladderDown,magicstone,nothing,ladderUp], [nothing,monster,bossmonster,sword,nothing]]

floor1 = [sword,monster,monster,monster,ladderUp]
floor2 = [ladderDown,magicstone,nothing,ladderUp]
floor3 = [nothing,monster,bossmonster,sword,nothing]
totalfloors = [floor1,floor2,floor3]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
   
print("Welcome to the DUNGEON!")
print("You are in a lost in a dungeon annd the only way to escape is to kill the *BOSS MONSTER*\nto get to him you will have to fight of monsters that you need a sword in order to kill\nthe dungeon is composed of 3 floors which contain 5 linear rooms which could contain :\na sword, a monster, a magic stone, ladder up, ladder down, or nothing ")
input("Press return to start! ")
clear_screen()

def Moveplayer(player, move):

    x, y = player

    if move == 'L':
        x -= 1

    if move == 'R':
        x += 1

    if move == 'LU':
        y -= 1

    if move == 'LD':
        y += 1

    return x, y

def movingOptions(player):
   
   
    moves = ['L', 'R', 'LU', 'LD']

    x, y = player

    if x == 0:
        moves.remove('L')

    if x == 4:
        moves.remove('R')

    if y == 1:
        moves.remove('LU')

    if y == 3:
        moves.remove('LD')

       
def death():
    print("YOUR TRASH KID, YOU JUST DIED!!!!")
   
def winning():
    print("LETS GOOO CHAMP, YOU WON!!!1")
   
def checkItems(check):
    b = False
    for i in items:
        if(i == check):
            b = True
    return b        

def fightBoss():
    if(board[floor][room] == bossmonster):
        if(checkItems(sword) and checkItems(magicstone)):
            winning()
        else:
            death()
           
def fightNormal():
    if(board[floor][room] == monster):
        if(checkItems(sword)):
           print("You have killed the monster that was in your way, Congrats :)")
           items.append(sword)
        else:
            death()
           
           
def treasure():
    if(len(items) >= 3):
        print("There are too many items in your inventory..")
       
    elif(board[floor][room] == sword):
        pickup = input("Would you like to pick up this item (y/n)?\nYou currently have" + str(len(items)) + "out of 3" )
        if(pickup == "y"):
            items.append(sword)
            
        elif(pickup == 'n' ):
            print("An item was left behind")
       
     
    elif(board[floor][room] == magicstone):
        pickup = input("Would you like to pick up this item (y/n)?")
        
        if(pickup == "y"):
            items.append(sword)
            
        elif(pickup == 'n' ):
            print("An item was left behind")
        print("You currently have " + str(len(items)) + " out of 3 : " )
       
def position():
    global room
    global floor
    print("\nYou are in room" + str(room-1) + " and on floor " + str(floor))
   
    t = input("Where would you like to go? :")
    if(t == "L"):
        room = room-1
    elif(t == "R"):
        room = room+1
    elif(t == "LU"):
        floor = floor+1
    elif(t == "LD"):
        floor = floor-1
   
    
    treasure()
    fightBoss()
    fightNormal()
    position()
   
       
   
 
   
position()    