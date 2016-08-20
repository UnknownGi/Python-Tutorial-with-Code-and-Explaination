# 3.1.3 - Lists

# A List is a Data Structure that groups data into one variable name.
# Each data in this list can be accessed through indexing
# A list can be expanded with more data or be removed.
# They are useful when gathering data with common properties
# A list can be created with square backets []

squares = [1, 4, 9, 16, 25]
print("List")
print("Squares List: " , squares)
print("Squares Index 0: " , squares[0])
print("Squares Index -4: " , squares[-4])
print("Squares Slicing 3 and Above: " , squares[3:])


# ---------- LIST CONCATENATION ------------

# Lists also support concatenation using + or * operation

print()
print("List Concatenation")
squares += [36, 49, 64, 81, 100]
print("Concatenation: " , squares)
squares = squares + (2*[121])
print("Concatenation: " , squares)


# ---------- MUTABLE LISTS ----------

# Unlike Strings, Lists are mutable i.e their elements can be changed by using indexes
# string[x] = 'X' will generate an error as strings are immutable but
# squares[len(squares)-1] = 144, won't as they are mutable

print()
print("Mutable Data Type")
squares[11] = 144
print("New List: " , squares)


# ---------- SHALLOW COPY ----------

# In Python 2 Types of Variable Copying Exist
# Shallow Copy - 2 Different Variables that Operate on their own
# Deep Copy - 2 Different Variables that Operate on same memory (change to any, changes the other one)

print()
print("Shallow and Deep Copy")

deepsq = squares
shallowsq = squares[:]
print("Deep Copy: " , deepsq)
print("Shallow Copy: " , shallowsq)

print()
print("Adding 169 to the Squares List")
squares += [13**2];
print("Deep Copy: " , deepsq)           # Value added due to same Memory Address
print("Shallow Copy: " , shallowsq)         # Different Memory, so its values aren't changed


# ---------- APPEND ----------

# To add a new element to the list, the append() function is used to add items at the end of the list
# append( val ) takes in a value and adds it to the end of the list

print()
print("Appending to a List")
squares.append(14**2)
squares.append(225)
print("New Squares: " , squares)


# ---------- SLICING ----------

# Slicing means to access a number of index from a start to an end point in a list using the [start:end] index operator
# Since lists are mutable, we can change the list using the slicing technique instead of changing them 1 at a time

print()
print("Slicing Lists")
letters = ['a', 'b', 'c', 'd', 'e' , 'f', 'g']
print("Original List: " , letters)
letters[2:5] = ['C', 'D', 'E']
print("After Changes [2:5]: " , letters)
letters[3:5] = []
print("After Removing [3:5]: " , letters)
letters[:] = []
print("Empty List: " , letters)


# ---------- LENGTH -----------

# Size/Length of a list determines the number of elements in a list
# it can be found using the len(list) function

print()
print("Length of a List")
print("Length of Letters: " , len(letters))
print("Length of Deep Copy: " , len(deepsq))
print("Length of Shallow Copy: " , len(shallowsq))


# ---------- NESTING LISTS ----------

# It means a list that can hold more than 1 list.
# or A collection of lists
# A 2d list contains 2 lists, a 3d list contains 3 lists and so on.
# To Access list elements, we first go to the list that we want to that and then to the element
# If We want to access the 2nd list the first index should be [1] and if we want to access the 1st item of that list then we go to index [0]
# to access 2d list, we use dual square brackters list[i][j] 

print()
print("Nesting Lists")
alpha = ['a', 'b', 'c']
numeric = [1, 2, 3]
alphanumeric = [ alpha, numeric ]
print("Nested 2D List: " , alphanumeric)
print("Accesing Alpha: ", alphanumeric[0])
print("Accessing Numeric: " , alphanumeric[1])
print("Accessing Alpha Char 'b': " , alphanumeric[0][1])
print("Accessing Numeric Number 3: " , alphanumeric[1][2])


