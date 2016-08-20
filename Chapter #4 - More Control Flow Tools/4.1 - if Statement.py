# 4.1 - if Statement

# An if statement checks whether a given condition is true
# If the condition is true it will execute the code inside the if condition

# There are three parts in if statement
# if .... elif .... else
# the elif(else if) and else part are compulsory
# control is passed between these conditions until one of them meets to be true
# if all conditions are false then else condition is applied (if it is written in the if statement)

# In this we will check whether the input number is positive, negative or zero

number = int(input("Please Enter a Number: "))

if number == 0: print("Zero")
elif number > 0: print("Positive")
else: print("Negative")