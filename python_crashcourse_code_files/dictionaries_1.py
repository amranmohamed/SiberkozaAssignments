
# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Create dict
person_am = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

# Use constructor
# person_am2 = dict(first_name='Sara', last_name='Williams')

# Get value
print(person_am['first_name'])
print(person_am.get('last_name'))

# Add key/value
person_am['phone'] = '555-555-5555'

# Get dict keys
print(person_am.keys())

# Get dict items
print(person_am.items())

# Copy dict
person2_am = person_am.copy()
person2_am['city'] = 'Boston'

# Remove item
del(person_am['age'])
person_am.pop('phone')

# Clear
person_am.clear()

# Get length
print(len(person2_am))

# List of dict
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]

print(people[1]['name'])
