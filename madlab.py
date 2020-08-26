
print('Hello and welcome to Madlibs, I am going to make a custom story for you. First enter the required fields...')
object1 = input("Enter a noun: ")
object2 = input("Enter a noun: ")
object3 = input("Enter a noun: ")
place1 = input("Enter a place: ")
place2 = input("Enter a place: ")
character1 = input("Enter a proper noun: ")
character2 = input("Enter a proper noun: ")
#use -ing
verb1 = input("Enter a verb that ends with -ing: ")
#present tense
verb2 = input("Enter a verb in present tense: ")
#past tense
verb3 = input("Enter a verb in past tense: ")
adjective1 = input("Enter an adjective: ")
adjective2 = input("Enter an adjective: ")
adjective3 = input("Enter an adjective: ")
story = "One day the " + adjective1 + " " + character1 + " was " + verb1 + " a " + object1 + " when " + character2 + " appeared out of thin air and asked him to " +  verb2 + " with him, so they went to " + place1 + " on the way they ran into a " + adjective2 + " " + object2 + " who stopped them and asked for a(n)" + adjective3+ " " + object3 + " however they did not have the " + adjective3 + " " + object3 + " so they " + verb3 + " the " + object3 + "... THE END"
print(story)