# Single line comment
letter = 'Z'                # A string could be a single character or a bunch of texts
print('letter: ',letter)               # Z
print('length: ', len(letter))          # 1
hello_world = 'Hello, World!'  # String could be  a single or double quote,"Hello, World!"
print('hello_world: ',hello_world)             # Hello, World!
print('length: ', len(hello_world))        # 13
learn = "Learn basic python in 10 days"
print('learn: ', learn)

# Multiline String
multiline_string = '''Learn python language within 10 days.
Here you will master the basics programming for beginners python applicable exercises every day.'''
print('multiline_string: ', multiline_string)

# String Concatenation
first_name = 'Python'
last_name = 'ID'
space = '_'
full_name = first_name  +  space + last_name
print('full_name: ', full_name) # Print 'Python_ID'
# Checking length of a string using len() builtin function
print('length first_name: ',len(first_name))  # 6
print('length last_name: ',len(last_name))   # 2
print('Compare length: ',len(first_name) > len(last_name)) # True
print('length full_name: ',len(full_name)) # 9

#### Unpacking characters 
language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t 
print(d) # h
print(e) # o
print(f) # n

# Accessing characters in strings by index
language = 'Python'
first_letter = language[0]
print(first_letter) # P
second_letter = language[1]
print(second_letter) # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n

# If we want to start from right end we can use negative indexing. -1 is the last index
language = 'Python'
last_letter = language[-1]
print(last_letter) # n
second_last = language[-2]
print(second_last) # o

# Slicing

language = 'Python'
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
last_three = language[3:6]
print(last_three) # hon
# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon

# Skipping character while splitting Python strings
language = 'Python'
pto = language[0:6:2] # 
print(pto) # pto

# Escape sequence
print('I really like learning python.\nDo you ?') # line break
print('Days\tTopics\tExercises')
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')

## String Methods
# capitalize(): Converts the first character the string to Capital Letter

challenge = 'ten days of python'
print(challenge.capitalize()) # 'Ten days of python'

# count(): returns occurrences of substring in string, count(substring, start=.., end=..)

challenge = 'ten days of python'
print(challenge.count('y')) # 2
print(challenge.count('y', 7, 14)) # 1
print(challenge.count('th')) # 1

# endswith(): Checks if a string ends with a specified ending

challenge = 'ten days of python'
print(challenge.endswith('on'))   # True
print(challenge.endswith('lon')) # False

# expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument

challenge = 'ten\tdays\tof\tpython'
print(challenge.expandtabs())   # 'ten  days    of      python'
print(challenge.expandtabs(10)) # 'ten    days      of        python'

# find(): Returns the index of first occurrence of substring

challenge = 'ten days of python'
print(challenge.find('y'))  # 6
print(challenge.find('t')) # 0

# format()	formats string into nicer output    
first_name = 'Python'
last_name = 'ID'
job = 'Learn'
country = '10 day'
sentence = '{}_{}. {} python in {}.'.format(first_name, last_name, job, country)
print(sentence) #Python_ID.Learn python in 10 day.


