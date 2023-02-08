# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people_am = ['John', 'Paul', 'Sara', 'Susan']

# Simple for loop
for person_am in people_am:
  print(f'Current person_am: {person_am}')

# Break
for person_am in people_am:
  if person_am == 'Sara':
    break
  print(f'Current person_am: {person_am}')

# Continue
for person_am in people_am:
  if person_am == 'Sara':
    continue
  print(f'Current person_am: {person_am}')

# range
for i_am in range(len(people_am)):
  print(people_am[i_am])

for i_am in range(0, 11):
  print(f'Number: {i_am}')

# While loops execute a set of statements as long as a condition is true.

count_am = 0
while count < 10:
  print(f'Count_am: {count_am}')
  count_am += 1