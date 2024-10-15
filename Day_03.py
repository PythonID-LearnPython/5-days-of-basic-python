#Get familiar with operators with simple calculations
print('Addition: ', 5 + 3) 
print('Subtraction: ', 10 - 2)
print('Multiplication: ', 5 * 2)
print ('Division: ', 15 / 3)                     
print('Division: ', 9 / 2)
print('Division without the remainder: ', 7 // 2)   
print('Modulus: ', 5 % 2)                           
print('Exponential: ', 9 ** 2)                   

# Floating numbers
print('Floating Number,PI', 3.14)
print('Floating Number, gravity', 9.81)

#Get familiar with comparison operators
print(5 > 2)     # True, because 5 is greater than 2
print(5 >= 2)    # True, because 5 is greater than 2
print(5 < 2)     # False,  because 5 is greater than 2
print(2 < 5)     # True, because 2 is less than 5
print(2 <= 5)    # True, because 2 is less than 5
print(3 == 6)    # False, because 3 is not equal to 6
print(3 != 6)    # True, because 3 is not equal to 6
print(len('red') == len('green'))  # False
print(len('red') != len('green'))  # True
print(len('red') < len('green'))   # True
print(len('green') != len('white'))      # False
print(len('green') == len('white'))      # True
print(len('orange') > len('black'))   # False

# Boolean comparison
print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)
print('True and True: ', True and True)
print('True or False:', True or False)

print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statement is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False


