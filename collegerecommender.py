questions = ["do u have a small pp? ", "are u vibing? ", "howz life? ", "bruh moment "]
points = [0, 0, 0, 0, 0]
answers0 = ["yes", "no", "maybe", "pp", "PP"]
answers1 = ["yes", "no", "maybe", "vibing away", "vibe rater"]
answers2 = ["good", "bad", "kys", "kms", "stfu"]
answers3 = ["bruh", "BRUH", "bRuH", "bruhh", "*bruh*"]
answers = [answers0, answers1, answers2, answers3]
universities = ["MIT", "Harvard", "Cainbridge", "Oxford", "yale"]
def questionsFunc(i):
    print(questions[i])
    answerList = answers[i]
    i =0
    for answer in answerList:
        print ("Answer " + str(i) +" is " + answer)
        i+=1
    pointNum = int(input("Which answer number do u choose: "))
    points[pointNum] +=1
i = 0
for question in questions:
    print(" ")
    questionsFunc(i)
    i+=1
print (" ")
if (points[0] > points[1] and points[0] > points[2] and points[0] > points[3] and points[0] > points[4]):
    print ("You are going to " + universities[0])
elif (points[1] > points[2] and points[1] > points[3] and points[1] > points[4]):
    print ("You are going to " + universities[1])
elif (points[2] > points[3] and points[2] > points[4]):
    print ("You are going to " + universities[2])
elif (points[3] > points[4]):
    print ("You are going to " + universities[3])
else:
    print ("You are going to " + universities[4])
print (" ")




