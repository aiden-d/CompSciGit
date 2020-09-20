import sys
intro = "\n**MONSTER SLAYER**\n You find your self lost in a dungeon with no memory of your previous life, besides the feeling that there is treasure to be found. You have no resources or weapons, to kill 1 monster you will need a sword and to kill the treasure guarder you will need 1 sword and 1  magic stone. The boss monster is on the 3rd floor, each floor contains 5 linear rooms and each room either contains: a sword, a monster, magic stones, up-stairs, down-stairs or nothing. Good Luck! \n"
boss_monster = "boss_monster"
monster = "monster"
sword = "sword"
magic_stone = "magic_stone"
stairs_up = "stairs_up"
stairs_down = "stairs_down"
left = "left"
right = "right"
restart_game = "restart_game"
nothing  = "nothing"
check_inventory = "check_inventory"
yes = "y"
no = "n"
room = "room"
isAlive = True
user_room = 2
user_floor = 0
items = []
floor1 = [stairs_up, monster, sword, monster, monster]
floor2 = [stairs_down, sword, stairs_up, monster, magic_stone]
floor3 = [boss_monster, monster, stairs_down, monster, nothing]
floors = [floor1, floor2, floor3]

print (intro)
def restart():
    global items
    global user_room 
    global user_floor
    items = []
    user_room = 2
    user_floor = 0
    sys.exit(0)
def death():
    print("YOU ARE DEAD!!!")
    global items
    global user_room 
    global user_floor
    items = []
    user_room = 2
    user_floor = 0
    sys.exit(0)
def victory():
    print("You defeated the final monster and have finally found your treasure!!! You wake up from your dream and realise that you are looking at your computer...")
    sys.exit(0)
def movementOptions():
    print ("\nYou currenty have the following movement options: ")
    global user_room
    global user_floor
    currentFloor = floors[user_floor]
    if (user_room - 1 >=0):
        print(left)
    if (user_room + 1 <=4):
        print(right)
    if (currentFloor[user_room] == stairs_up):
        print(stairs_up)
    if (currentFloor[user_room] == stairs_down):
        print (stairs_down)
    print(restart_game)
    print(check_inventory)
    s = input("Which option do you choose? : ")
    if (s == left and user_room - 1 >=0):
        user_room = user_room-1
    elif (s == right and user_room + 1 <=4):
        user_room = user_room+1
    elif (s == stairs_up and currentFloor[user_room] == stairs_up):
        user_floor = user_floor+1
    elif (s == stairs_down and currentFloor[user_room] == stairs_down):
        user_floor = user_floor-1
    elif (s == restart_game):
        restart()
    elif(s == check_inventory):
        if (items == None):
            print ("Your inventory is empty")
        else: 
            print("\n Your inventory contains: ")
            for i in items:
                print ("a " + i)

        
        movementOptions()
    else: movementOptions()
    
def checkItem(name):
    b = False
    for i in items:
        if (i == name):
            b = True
    return b


def combat():
    if (floors[user_floor][user_room] == boss_monster):
        if (checkItem(sword) and checkItem(magic_stone)):
            victory()
        else:
            death()
    elif (floors[user_floor][user_room] == monster):
        if (checkItem(sword)):
            print ("You have successfully killed the monster and broken your sword!")
            items.remove(sword)
        else:
            death()
def printLocation():
    tempFloor1 = [room, room, room, room, room]
    tempFloor2 = [room, room, room, room, room]
    tempFloor3 = [room, room, room, room, room]
    tempFloors = [tempFloor1,tempFloor2, tempFloor3]
    tempFloors[user_floor][user_room] = "You "
    print(tempFloor3)
    print(tempFloor2)
    print(tempFloor1)


def loot():
    if (len(items)>= 3):
        "You have too many items in your inventory to pick this up!"
    elif (floors[user_floor][user_room] == sword):
        a = input("Do you want to pick up this item? You currently have " + str(len(items)) + " items out of 3. (y or n) : ")
        if (a == yes):
            items.append(sword)
        elif (a == no):
            print("you left the item")
        else: loot()

    elif (floors[user_floor][user_room] == magic_stone):
        a = input("Do you want to pick up this item? You currently have " + str(len(items)) + " items out of 3. (y or n) : ")
        if (a == yes):
            items.append(magic_stone)
        elif (a== no): 
            print("you left the item")
        else: loot()


def turn():
    printLocation()
    print ("in this room there is a " + floors[user_floor][user_room])
    combat()
    loot()
    movementOptions()

    
while (isAlive):
    turn()



























































































































































print("ur sus")