# Python has functions for creating, reading, updating, and deleting files.

# Open a file
myFile_am = open('myFile_am.txt', 'w') #in here it write the myFile_am.txt 

# Get some info
print('Name: ', myFile_am.name)
print('Is Closed : ', myFile_am.closed)
print('Opening Mode: ', myFile_am.mode)

# Write to file
myFile_am.write('I love Python')
myFile_am.write(' and JavaScript')
myFile_am.close()

# Append to file
myFile_am = open('myFile_am.txt', 'a')
myFile_am.write(' I also like PHP')
myFile_am.close()

# Read from file
myFile_am = open('myFile_am.txt', 'r+')
text = myFile_am.read(100)
print(text)