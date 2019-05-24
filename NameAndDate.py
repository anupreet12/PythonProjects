#First off hashtags are comments
#
#Part1
#Make a pythonFile that asks the user for their name
#Display that name
#
#Part2
#When you get the users name, you should be able to take what they give you and
#reply with a 'welcome (their name)'
#
#Part3
#After you show the welcome and their name
#I want you to have it say 'Hello (their name) did you know its (date)
#So you have to look up how to show the CURRENT! date and display that

var = input("What is your name?\n")
print("welcome", var)
print('did you know its')
from datetime import date
today = str(date.today())
print(today)
