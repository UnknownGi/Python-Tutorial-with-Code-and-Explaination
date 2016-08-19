# Chapter 3.1.1 - Numbers

# There are 2 Types of Number in Computers
# Integer (int for short) - These numbers are represented as Whole Numbers (1, 0, -32, 501002)
# Floating Point (float for short) - These numbers are represented by Decimal or Exponents (10.3211, 10.5, 2e19)

# ---------- OPERATORS -----------
# The Plus(+) Operator is used to Add Numbers
# 5 + 3 = 8
print("Addition")
result = 5+3
print("5 + 3 = " , result)        # Why Didn't "5 + 3 = " print? It's because 5 + 3 are treated as a String (Sentence) and not a Number
print()        # This print is written just to make the output more visible by displaying a new line (CRLF)

# The Minus(-) Operator is used to Subtract Numbers
# 3 - 2 = 1
print("Subtraction")
result = 3-2
print("3 - 2 = " , result)
print()

# The Star(*) Operator is used to Multiply Operators
# 10 * 10 = 100
print("Multiplication")
result = 10*10
print("10 * 10 = " , result)
print()

# The Forward Slash(/) Operator is used to Divide Operators
# 10 / 2 = 5
print("Division")
result = 10/2
print("10 / 2 = " , result)
print()

# The Percentage(%) Operator is used to Get The Remainder Between 2 Numbers
# 5 % 3 = 2
print("Modulus")
result = 5%3
print("5 % 3 = " , result)
print()



# ---------- DIVISION TYPES -----------

# Division always returns a float
# To Discard Anything after the Decimal Point(.), then use the (//) To Divide
# Modulus(%) is also a part of Division, this returns remainder between divisor and quotient

print()
print("Division Types")
print("17 / 3 = " , 17/3)
print("17 // 3 = " , 17//3)
print("17 % 3 = " , 17%3)


# ---------- POWER CALCULATION -----------

# Power is a Number that is multipled by itself N number of times
# This is achieved by using a double star(**) operator
# We can Also root a number by using the 2nd number as a reciprocal/fraction (a/b)

print()
print("Power Calculation")
print("2 power 3 = " , 2**3)
print("5^2 = " , 5**2)
print("square root 16 = " , 16**(1/2))


# ---------- Variable Initializing & Assignment -----------

# A variable(character or sequence of character) can store data in python
# Initializing variable means that a variable has been declared and can be used throughout coding
# Assignment means that a variable has a value assigned to it

print()
print("Variable Initialization & Assignment")

result
print("Initializing Result = " , result)

result = 10
print("Assignment Result = " , result)


# ---------- Real and Imaginary Numbers ----------

# These numbers are created when numbers that can't exist in this realm are to be used.
# Example root(-1) will generate an error since it can't be resolved but using imaginary number -1 is converted to j square(j**2) and then rooted : result(j)
# Format = a + bj where a & b are numbers
# Operators Apply To Such Numbers as Any Number

print()
print("Real Numbers")
number = 5+3j
print("Example: " , number)

another_number = 10+2j
print("Addition: " , number+another_number)
print("Subtraction: " , number-another_number)
print("Multiplication: " , number*another_number)
print("Division: " , number/another_number)