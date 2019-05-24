#
#Part1
#Make a pythonFile that asks the user for their name
#Display that name
#
#Part2
#Take the users input and display it
#
#Part3
#When you get the users name have that saved to a new file with the (usersname).py

#Part4
#At the top of the new file have it say the DATE a space, and then the usersname


name = input("What is your name?\n")
print("welcome", name)

from datetime import date
today = str(date.today())
print(today, name)

print(name, today, file=open(name + ".py", "a"))




