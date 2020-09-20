import random
health = 5
food = 500
miles = 2000
days = 305
badday1 =None
badday2 = None
currentMonth = -1
daysOfTheMonth = [31,30,31,30,31,31,30,31,30,31]
print("Hi welcome to the Oregon Trail! Your goal is to travel from NYC to Oregon (2000 miles) by Dec 31st. However, the trail is arduous. Each day costs you food and health. You can hunt and rest, but you have to get there before winter!")
name = input("Please enter your name: ")

def travel(): 
    global days
    global miles
    m = random.randint(30,60)
    d = random.randint(3,7)
    days = days -d
    miles = miles - m
    
def rest():
    global health 
    global days
    days = days - random.randint(2,5)
    health +=1
def getDayAndMonth():
    global days
    currentDays = 305-days
    b = True
    i = 0
    while (b == True):
        if (currentDays>daysOfTheMonth[i]):
            currentDays = currentDays - daysOfTheMonth[i]
            i = i+1
        else:
            b = False
    
    return [currentDays,i]
        



def badday():
    global badday1
    global badday2
    badday1 = random.randint(1,30)
    badday2 = random.randint(1,30)
    if (badday1 == badday2): badday()

def monthly():
    global badday1
    global badday2
    global currentMonth
    global health
    month = getDayAndMonth()[1]
    if (month != currentMonth):
        
        badday()
        currentMonth = month
    dayOfMonth = getDayAndMonth()[0]
    if (dayOfMonth == badday1 or dayOfMonth == badday2):
        health= health-1
        print("Your health has been decreased!!!")

def hunt():
    global food
    food = food + 100




def help():
    print("help")



    
while (health > 0 and food > 0 and days > 0 and miles > 0):
    food = food - 5
    print ("You currently have ", health, " health and ", food,  "lbs of food. There are " , miles, " miles left to travel and " ,days, " days left.")
    i = input("What do you wish to do next? travel (t), rest (r), hunt (h), help (help), quit (q)? : ")
    monthly()
    if (i == "travel" or i == "t"): travel()
    if (i == "rest" or i == "r"): rest()


    
