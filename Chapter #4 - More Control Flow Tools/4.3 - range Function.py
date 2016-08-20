# 4.3 - range Function

# The range() function allows for an arithmetic progressive series that allows to iterate over that particular elements in the series
# A range() function can take in 3 paramaters at max and 1 at min.
# Parameters are recognizes as:
    # range ( start, end, increment/decrement) or range ( start )

# The function starts@start and end@end-1 (one less of end)
# It is equivalent to the for loop in C/C++/Java
# for ( int i=start; i<end; ++increment/--decrement )

print("Iterating From 0-4")
for i in range(5):
    print(i)


print()
print("Iterating From 3-10")
for i in range(3, 11):
    print(i)


print()
print("Iterating from 0-25 with Multiples of 5")
for i in range(0, 26, 5):
    print(i)


# Instead of just climbing the ladder ( going forward in positive axis ) we can also climb down from ladder ( going backwards in negative axis )

print()
print("Reverse Loop")
for i in range(10, -1, -1):
    print(i)


# We can also iterate over DataStructures

# Strings

string = "My name"
print()
print("String Traversing")
for index in range(len(string)):
    print(string[index])


# Lists

print()
print("List Traversing")
animals = ['cat', 'dog', 'horse']
for index in range(len(animals)):
    print(animals[index])


# Range can also be used to create a List instead of traversing over them

print()
print("Creating a List Using range(5)")
print(list(range(5)))