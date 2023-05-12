

correct1 = ("12")
question1 = ("How many is a dozen?")

correct2 = ("No")
question2 = ("Is carrot a fruit?")

correct3 = ("Patrick")
question3 = ("Who is Spongebob's best friend")
player = None

name = input("What is your name?\n").capitalize()
print("Hello,", name +"!" , "Welcome to this mini quiz. There are only 3 questions, answer them correctly. Goodluck! \n")

player = input(question1 + '\n')
if player == correct1:
    print("Correct!")
else:
    print("Nope, actually its 12")

player = input(question2 + '\n').capitalize()
if player == correct2:
    print("Correct!")
elif player == "Yes" or " ":
    print("Sorry, actually its not a fruit")

player = input(question3 + '\n').capitalize()
if player == correct3:
    print("Yes!")
else:
    print("Wrong, its Patrick!")

print("Hope you had fun! Tata for now ~")
