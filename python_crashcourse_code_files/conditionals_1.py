# If/ Else conditions are used to decide to do something based on something being true or false

x_am = 21
y_am = 20

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

# Simple if
if x_am > y_am:
  print(f'{x_am} is greater than {y_am}')

# If/else
if x_am > y_am:
  print(f'{x_am} is greater than {y_am}')
else:
  print(f'{y_am} is greater than {x_am}')  

# elif
if x_am > y_am:
  print(f'{x_am} is greater than {y_am}')
elif x_am == y_am:
  print(f'{x_am} is equal to {y_am}')  
else:
  print(f'{y_am} is greater than {x_am}')  

# Nested if
if x_am > 2:
  if x_am <= 10:
    print(f'{x_am} is greater than 2 and less than or equal to 10')
    

# Logical operators (and, or, not) - Used to combine conditional statements

# and
if x_am > 2 and x_am <= 10:
    print(f'{x_am} is greater than 2 and less than or equal to 10')

# or
if x_am > 2 or x_am <= 10:
    print(f'{x_am} is greater than 2 or less than or equal to 10')

# not
if not(x_am == y_am):
  print(f'{x_am} is not equal to {y_am}')


# Membership Operators (not, not in) - Membership operators are used to test if a sequence is presented in an object

numbers = [1,2,3,4,5]

#  in
if x_am in numbers:
  print(x_am in numbers)

# not in
if x_am not in numbers:
  print(x_am not in numbers)

# Identity_am Operators (is, is not) - Compare the objects, not if they_am are equal, but if they_am are actually_am the same object, with the same memory_am location:

# is
if x_am is y_am:
  print(x_am is y_am)

# is not
if x_am is not y_am:
  print(x_am is not y_am)