## Caroline S. Lee, 03/04/18
## CS Foundations
## Solutions to practice problems in Lesson5.py



## Which coin?

## Write a program that asks the user for the value of a coin. Output the type of 
## coin he/she/they entered. If the user inputs 25, your program should identify that 
## this is a quarter. 

coin_val = int(raw_input("What is the value of your coin? "))

if coin_val == 25:
	print "You have a quarter!"
elif coin_val == 10:
	print "You have a dime!"
elif coin_val == 5:
	print "You have a nickel!"
elif coin_val == 1:
	print "You have a penny!"
else:
	print "That's not a coin from 'round here, is it?"



###########################################

## Magic Eight Ball

## Write a program that outputs at least 4 different results of a magic 8 ball. 

## HINT: use modulus OR the random number library to determine the output.

import random

raw_input("Ask me a yes/no question: ")

outcome = random.randint(1,4)

if outcome == 4:
	print "You may rely on it"
elif outcome == 3:
	print "As I see it, yes"
elif outcome == 2:
	"Ask again later"
else:
	"Outlook not so good"

## alternate answer using modulus

raw_input("Ask me a yes/no question: ")
outcome = int(raw_input("Choose any number: ")) % 4

if outcome == 3:
  print "You may rely on it"
elif outcome == 2:
  print "As I see it, yes"
elif outcome == 1:
  print "Ask again later"
else:
  print "Outlook not so good"

###########################################

## Die roll with a friend

## Write a program that generates die rolls for you and a friend, and  
## subsequently determines the winner.

## HINT: use the random library OR modulus..

import random 

your_score = random.randint(1,6)
print "You rolled a", your_score

friend_score = random.randint(1,6)
print "Your friend rolled a", friend_score

if your_score > friend_score: 
  print "You win!"
elif your_score == friend_score:
  print "Tie"
else:
  print "You lose..."
