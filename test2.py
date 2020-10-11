import random
days31_months = [1, 3, 5, 7, 8, 10, 12]
days30_months = [4 , 6, 9, 11]
days28_months = [2]
all_months = [1,2,3,4,5,6,7,8,9,10,11,12]
player_health = 5
player_distancefromoregon = 2000
player_food = 500
player_startday =  3
player_startmonth = 1
player_distancetravelled = random.randint(30,60)
player_daystakentotravel = random.randint(3,7)
healthloss = random.randint(1,3)
restinghunting = random.randint(2,5)
randomday = (1,28)
user_input = (input(" what would you like to do? "))
isAlive = True
def variables ():
    global player_health
    global player_distancefromoregon
    global player_food
    global player_startday
    global player_startmonth
    global player_distancetravelled
    global player_daystakentotravel
    global healthloss
    global randomday
    global restinghunting
    global user_input
    global isAlive
     
def askList ():
    print("Your command options are: askTravel, askRest, askHunt, askStatus, askHelp, askQuit" )
       
def quit ():
    if user_input == 'quit' or user_input == 'askQuit':
        print('You have decided to quit the game')
        isAlive==False
 

     
def askTravel ():
    if user_input == 'askTravel' or user_input == 'travel':
        player_food = player_food - player_daystakentotravel * 5
        player_distancefromoregon = player_distancefromoregon - player_distancetravelled
        player_startday = player_startday - player_daystakentotravel
        print(player_startday,player_startday,)
         
def hunt ():
    if user_input == 'hunt':
        player_food = player_food + 100
        player_startday = player_startday + player_daystakentotravel
def monthchange ():
    if player_startday == 31 and  player_startmonth in days31_months:
            whichmonth = days31_months.index(player_startmonth)
            player_startmonth = days31_months[whichmonth + 1]
            player_startday = player_startday**0
            print(player_startday, player_startday)
    elif player_startday == 30 and player_startmonth in days30_months:
            whichmonth = days30_months.index(player_startmonth)
            player_startmonth=days30_months[whichmonth + 1]
            player_startday = player_startday**0
            print(player_startday, player_startmonth)
    elif player_startday == 28 and player_startmonth == 4:
            player_startmonth = player_startmonth + 1
            player_startday = player_startday**0
            print(player_startday, player_startmonth)
def status ():
    if user_input == 'status' or user_input == 'askStatus':
        print(player_startday, player_startmonth,player_distancefromoregon, player_health, player_food )
def rest ():
    if user_input == 'rest' or user_input == 'askRest':
        player_food = player_food - player_daystakentotravel * 5
        player_startday = player_startday - player_daystakentotravel
        player_health = player_health + 1
def randomhealthloss ():
    for player_startmonth in  all_months :
        player_health = player_health - healthloss
        print(player_health)
   










while(isAlive==True):
    user_input = input(" what would you like to do? ")
    if (user_input == 'askList' or user_input== 'list'): askList()
    if (user_input == 'askTravel' or user_input == 'travel'): askTravel()
    if (user_input == 'quit' or user_input =='askQuit'): quit()
    if (user_input == 'hunt'): hunt()
    if (user_input == 'status' or user_input == 'askStatus'): status()
    if (user_input == 'rest' or user_input == 'askRest'): rest()
   
    monthchange()
    randomhealthloss ()
 