# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list
number_am = [1, 2, 3, 4, 5]
fruits_am = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Use a constructor
# number_am2 = list((1, 2, 3, 4, 5))

# Get a value
print(fruits_am[1])

# Get the last value
print(fruits_am[-1])



# Get length
print(len(fruits_am))

# Append to list
fruits_am.append('Mangos')

# Remove from list
fruits_am.remove('Grapes')

# Insert into position
fruits_am.insert(2, 'Strawberries')

# Change value
fruits_am[0] = 'Blueberries'

# Remove with pop
fruits_am.pop(2)

# Reverse list
fruits_am.reverse()

# Sort list
fruits_am.sort()

# Reverse sort
fruits_am.sort(reverse=True)

print(fruits_am)
