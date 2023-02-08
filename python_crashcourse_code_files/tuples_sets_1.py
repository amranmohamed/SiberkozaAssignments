# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create tuple
fruits_am = ('Apples', 'Oranges', 'Grapes')

# Using a constructor
# fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

# Single value needs trailing comma
fruits2_am = ('Apples',)

# Get value
print(fruits_am[1])

# Can't change value
fruits_am[0] = 'Pears'

# Delete tuple
del fruits2_am

# Get length
print(len(fruits_am))


# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if in set
print('Apples' in fruits_set_am)

# Add to set
fruits_set_am.add('Grape')

# Remove from set
fruits_set_am.remove('Grape')

# Add duplicate
fruits_set_am.add('Apples')

# Clear set
fruits_set_am.clear()

# Delete
del fruits_set_am

print(fruits_set_am)
