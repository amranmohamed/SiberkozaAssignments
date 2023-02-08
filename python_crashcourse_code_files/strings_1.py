# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name_am = 'Brad'
age_am = 37

# Concatenate
print('Hello, my name_am is ' + name_am + ' and I am ' + str(age_am))

# String Formatting

# Arguments by position
print('My name_am is {name_am} and I am {age_am}'.format(name_am=name_am, age_am=age_am))

# F-Strings (3.6+)
print(f'Hello, my name_am is {name_am} and I am {age_am}')

# String Methods

s_am = 'helloworld'

# Capitalize string
print(s_am.capitalize())

# Make all uppercase
print(s_am.upper())

# Make all lower
print(s_am.lower())

# Swap case
print(s_am.swapcase())

# Get length
print(len(s_am))

# Replace
print(s_am.replace('world', 'everyone'))

# Count
sub_am = 'h'
print(s_am.count(sub_am))

# Starts with
print(s_am.startswith('hello'))

# Ends with
print(s_am.endswith('d'))

# Split into a list
print(s_am.split())

# Find position
print(s_am.find('r'))

# Is all alphanumeric
print(s_am.isalnum())

# Is all alphabetic
print(s_am.isalpha())

# Is all numeric
print(s_am.isnumeric())
