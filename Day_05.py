# Learn python using lists
fruits = ["apple", "banana", "cherry"]
print(fruits)

list_example = ["apple", 2, True, 3.5]
print(list_example)

# Ordered
fruits = ["apple", "banana", "cherry"]
print(fruits[1])  # Outputs "banana"

# Changeable
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"  # Change "banana" to "blueberry"
print(fruits)

# Allow Duplicates
fruits = ["apple", "banana", "cherry", "apple"]
print(fruits)

# List Length
fruits = ["apple", "banana", "cherry"]
print(len(fruits))  # Outputs 3

# List Items - Data Types
list1 = ["apple", "banana", "cherry"]  # Strings
list2 = [1, 2, 3, 4, 5]  # Integers
list3 = [True, False, False]  # Booleans
list4 = ["abc", 34, True, 40, "male"]  # Mixed data types

# type()
mylist = ["apple", "banana", "cherry"]
print(type(mylist))  # Outputs <class 'list'>

#The list() Constructor
fruits = list(("apple", "banana", "cherry"))  # Note the double parentheses
print(fruits)

# Python Collections (Arrays)
fruits = ["apple", "banana", "cherry"]
print(fruits)

# Copy Using list() Function
original_list = [1, 2, 3]
copied_list = list(original_list)

copied_list[0] = 100
print(original_list)  # Output: [1, 2, 3]
print(copied_list)    # Output: [100, 2, 3]

# Copy Using Slicing
original_list = [1, 2, 3]
copied_list = original_list[:]

copied_list[0] = 100
print(original_list)  # Output: [1, 2, 3]
print(copied_list)    # Output: [100, 2, 3]

# Copying Using copy() Method
original_list = [1, 2, 3]
copied_list = original_list.copy()

copied_list[0] = 100
print(original_list)  # Output: [1, 2, 3]
print(copied_list)    # Output: [100, 2, 3]

# Join Two Lists
# Creating a fLists
fLists = [10, 8, 6, 4, 2]
print("Print fLists: ")
print(fLists)

# Creating a lLists
lLists = ['Jack','David','Join', 'Alice']
print("Print lLists: ")
print(lLists)

# Using the + operator
join_list = fLists + lLists
print("\nPrint paired list: ")
print(join_list)

# Sort List Alphanumerically
lists = ["Jack", "David", "Rose", "Alice", "Jone"]
lists.sort()
print(lists)

# Sort the list alphabetically:
# lists = ['Alice', 'David', 'Jack', 'Jone', 'Rose']

#Sort Descending
lists = ["Jack", "David", "Rose", "Alice", "Jone"]
lists.sort(reverse = True)
print(lists)

# Sort the list descending:
# lists = ['Rose', 'Jone', 'Jack', 'David', 'Alice']

# Customize Sort Function
def name_function(n):
  return abs(n - 30)

lists = [200, 16, 21, 166, 131]
lists.sort(key = name_function)
print(lists)

# Sort the list based on how close the number is to 30:
# lists = [21, 16, 131, 166, 200]

# Case Insensitive Sort
lists = ["Jack", "David", "Rose", "Alice", "Jone"]
lists.sort()
print(lists)

# Sort the list alphabetically:
# lists = ['Alice', 'David', 'Jack', 'Jone', 'Rose']

# Reverse Order
lists = ["Jack", "david", "Rose", "Alice", "jone"]
lists.reverse()
print(lists)

# Reverse the order of the list items:
# lists = ['jone', 'Alice', 'Rose', 'david', 'Jack']