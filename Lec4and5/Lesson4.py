## Caroline Lee, 02/28/2018
## CS Foundations, Lecture 4

## Next blocks are answers to the type-casting problem

# cast values obtained from raw_input because the default behavior stores the values as strings.
january = int(raw_input("How much in January? "))
feb = int(raw_input("How much in February? "))
march = int(raw_input("How much in March? "))

# calculate the sum and average of your values.
total = january + feb + march
mean_bud = total/3

# print your calculations to the console.
print "Sum =", total
print "Mean =", mean_bud

## Next block is an alternate answer to the type-casting problem
jan = raw_input("How much in January? ")
febr = raw_input("How much in February? ")
mar = raw_input("How much in March? ")

# cast your strings here instead
sum_3 = int(jan) + int(febr) + int(mar)
avg = sum_3/3

# print to screen
print "Sum =", sum_3
print "Mean =", avg

## NOTE: if you want to accept floats (decimal numbers) from the user, you must cast as float, not int.

##########################################

## Next blocks correspond to the one-way and two-way if statements slides.

x = 5
 
# one-way if statement
if x > 10:
    print "x is greater than 10!"
# should not print here because the expression evaluates to False.

# two-way if statement
if x > 10:
    print "x is greater than 10!"
else:
    print "x is less than or equal to 10!"
# should execute else block

###########################################

## Two-way if statements practice problem
y = 5
if (y % 2) == 0:
    print "Fizz"
else:
    print "Buzz"

# alternate solution (inspired by someone in the class, cannot remember who...)
y = 5
y_mod = y % 2

if y_mod == 0:
    print "Fizz"
else:
    print "Buzz"


###########################################

## Duck, duck, goose!

## Store your own name in a variable. Ask the user for his/her/their name. Print goose if the user's name matches yours;
## otherwise, print duck. The point of this exercise is to familiarize ourselves with string comparisons.
## Up until now, we have only compared numeric values. Please think about other intances in which string comparisons
## can be useful.

###########################################

## Cash register

## Ask the user to input the prices of 3 items and type of dollar he/she/they wish to use. Let the user know if the amount
## given is enough.

## Hint: account for excess change, just enough change, and too few change.

###########################################

## Chore assignment

## Let's say you want to randomly assign one of three types of chores (sweeping the floor, dishes, dusting the piano,
## etc.) to your friends and family members. Have the user input his/her/their name and an integer between 1 and 99.
## Based on this number, you will assign a task to the user by printing out his/her/their name and the task.

###########################################

## Lost pet...

## You are searching for your missing pet, whose name and species I leave up to you. Suppose people have been
## calling you to report lost pets they have found. Get the name and species of the pet in question, and
## compare these answers to your missing pet's name and species. Generate appropriate output.

###########################################

## Letter grade calculation

## Ask the user for 3 exam grades, which you will need to store as floating point numbers. Calculate the
## average of 3 grades and its corresponding letter grade. You may use A, B, C, D, without accounting for
## pluses/minuses. Example: user inputs 88.3, 95.7, and 96. He/she/they will then receive a letter grade of A.
## You may choose to print out the average AND the letter grade for debugging purposes.

## Hint: we did NOT learn about elif statements yet, but we did learn about logic operators, which can be used
## to evaluate two or more boolean expressions at once.

###########################################

## Lab assignment

## Rohini suggested a wonderful idea for the class to begin solving lab problems with our current programming
## expertise. Please choose a self-report questionnaire, screening questionnaire, or questions we ask during
## study visits, and devise a series of if statements pertaining to the outcomes of your chosen questionnaire.
## Bring your results to class next week, and share your code with your classmates.



