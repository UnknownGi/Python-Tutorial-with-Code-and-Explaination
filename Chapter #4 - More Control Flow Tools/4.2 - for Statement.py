# 4.2 - for Statement

# A for statement is used to iterate over a data container like Strings, List, Sets etc.
# A for statement can iterate from the start of the list or from the end of the list depending on the condition

animals = ['cats', 'dogs', 'mouse']
for animal in animals:
    print(animal, animal.__len__())
    
# The animal in animals, is used to assign it self a value each time the loop runs.
# for the first iteration animal = cats, then after it comes back to the loop it becomes animal = dogs and so on...