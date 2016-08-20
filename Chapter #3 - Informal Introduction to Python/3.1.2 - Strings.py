# 3.1.2 - Strings

# Besides numbers, Python can also manipulate strings, which can be expressed in several ways.
# They can be enclosed in single quotes ('...') or double quotes ("...") with the same result.

print('String Quotes (Single or Double)')
print('spam eggs')
print('doesn\'t')   # Why doesn't it print doesn\'t? Because if we use print('doesn't') the function would end at print('doesn' and would generate an error
print("doesn't")
print('Yes, "he said"')
print("Yes, \"he said\"")
print('Isn\'t, she said')


# ---------- Strings as Variables ----------

# Variable can also store Strings besides Numbers
# Strings can store a word, a sentence, sentences, a paragraph or an essay

print()
print("Strings as Variables")

string = "This is a String"
print("String: " , string)

string = "He said \"What are you doing?\""
print("String: " , string)

string = "This string has 2 lines.\nThis is another line"   # \n is a Special Character that denotes a new line feed
print("String: " , string)


# ---------- Multiple Line Print Spanning ----------

# A print function can take many lines as arguement the \ character is used to denote a multiline print paramaters

print()
print("Multiline Print Spanning")
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")


# ---------- String Concatenation ----------

# The + operator is used to join 2 strings a + b = ab
# The * operator is used to join 2 strings x times a + x(b) = abbb (if x = 3)
# Automatic concatenation is also achieved if two strings are consecutive
# Strings can be concatenated if put together in Paranthesis (

print()
print("String Concatenation")

string_A = "ab"
string_B = "cd"

print("Concatenation using +: " , string_A+string_B)
print("Concatenation using *: " , string_A+(3*string_B))

python = "Py" "thon"
print("Python: " , python)
print("Python + String_A = " , python+string_A)

set = ('this ' 'is ' 'a ' 'string')
print("Set: " , set)


# ---------- Indexing Strings ----------

# By indexing we mean to access a specific position(place) in string
# A number is used to access a string
# Index Starts from zero(0) and goes as string length increases
# Index Number can be Negative or Greater than the string length
# Many Characters can be selected using the indexed style string[start:end] where start and end aren't compulsory

# +---+---+---+---+---+---+
# | P | y | t | h | o | n |
# +---+---+---+---+---+---+
# 0   1   2   3   4   5   6
#-6  -5  -4  -3  -2  -1

print()
print("String Indexing")
word = "Python"
print("Index 0: " , word[0])
print("Index 5: " , word[5])
print("Index -1" , word[-1])

print()
print("Index 0-2: " , word[0:2])
print("Index 2-: " , word[2:])
print("Index -2: " , word[:2])
print("Index: " , word[:])

print()
print("Joining Indexes: " , word[:2]+word[2:])
print("New String: " , 'J'+word[1:])


# ---------- LENGTH OF A STRING ----------

# Length of a String is returned from a function of len()
# It takes the paramater as a string and returns the number of characters in it
# It is useful when iterating(going through) the complete string

print()
print("Length of a String")
print("Length of Python: " , len(word))

