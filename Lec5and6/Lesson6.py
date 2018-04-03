
## Caroline Lee, 03/03/2018
## CS Foundations, Lecture 5

## Corresponds to While loop slide#84

# initialize some variable
counter = 0

while counter < 5:
	print "counter =", counter
	# now update the value of counter
	counter += 1

## should print 5 times


## Corresponds to while loop practice problem, regarding calculation of exponents. 
base = int(raw_input("Enter the base: "))
exp = int(raw_input("Enter the exponent: "))

counter = 0
result = 1

while counter < exp:
	result = result * base 
	print result
	counter += 1

## While loop factorial problem
fac = 5
counter = 4

while counter > 0:
	fac *= counter
	print fac
	counter -= 1

## While loop even-odd counter problem

counter = 0

while counter < 5:
	print counter
	if (counter % 2) == 0:
		print "Fizz!"
	else:
		print "Buzz!"
	counter += 1

###########################################

## WHILE LOOP HW Problems!

###########################################

## 

###########################################

## Rethinking iterative problems

## Recall a problem we solved together, where we took 3 or more
## user-inputted variables and calculated the sum and average. 
## Use your knowledge of while loops to rewrite your program.

## Hint: loops are used to perform repetitive tasks.
## Which task are we repeating in this problem? 

###########################################




