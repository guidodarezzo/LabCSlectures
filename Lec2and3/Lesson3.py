## Caroline Lee, 02/21/2018
## CS Foundations, Lecture 3

## Today, we wrapped up print statements and moved on to user input, data types, arithmetic operations, and type casting

## The next block of code demonstrates Jenny's successful debugging adventure.
## Her original code:
    ### your_name = "Jenny"
    ### print(Jenny)
## This threw a runtime error because Jenny was not the name of the variable.
## Alternatively, she could have fixed this error by enclosing Jenny in parentheses.
## Just to drive the point home--functions take values and/or variables representing values.

## Here are both corrections:
your_name="Jenny"
print(your_name)
print("Jenny")

## The next block corresponds to the raw_input function slides.
## Please note that you must save user input in a variable if you want to reference that value later.

## Takes user response to the question, What is your name, and stores it in your_name
your_name = raw_input("What is your name? ")
## Print the value stored in the variable to the console
print "Welcome to Computer Science, ", your_name

## The next block is one possible answer to the raw_input problem.
## Store at least 2 user-inputted values in variables and subsequently print these responses to the screen.
num_siblings = raw_input("How many siblings do you have? ")
names = raw_input("What are their names? ")

print "You have", num_siblings, "siblings, and their names are", names

## The next block is one possible answer to the arithmetic problem
## Store 3 or more values in separate variables. Calculate and print both the sum and mean of these values.
january = 145.5
feb = 88
march = 210.07

total = january + feb + march
mean_bud = total/3

print "Sum =", total
print "Mean =", mean_bud

## The next block demonstrates the distinction between multiple data types in Python.
## Corresponds to the Data Types slide
var1 = "Caroline"
var2 = 10
var3 = 10.0

print(type(var1))
print(type(var2))
print(type(var3))
