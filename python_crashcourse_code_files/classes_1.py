# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class
class User:

  # Constructor : is basically a function that runs when you instantiate an object from a class.
  def __init__(self_am, name_am, email_am, age_am):
    self_am.name_am = name_am
    self_am.email_am = email_am
    self_am.age_am = age_am
    
    # Adding Encapsulation of variables... Encapsulation is the concept of making the variables non-accessible or accessible upto some extent from the child classes
    self_am._private = 1000 # Encapsulated variables are declares with '_' in the constructor.

  def greeting(self_am):
      return f'My name_am is {self_am.name_am} and I am {self_am.age_am}'

  def has_birthday(self_am):
      self_am.age_am += 1
 
 #function for encap variable
  def print_encap(self_am):
      print(self_am._private)

# Extend class
class Customer(User):
  # Constructor
  def __init__(self_am, name_am, email_am, age_am):
      User.__init__(self_am, name_am, email_am, age_am) #Called proper parent class constructor to make this as proper child inehriting all methods.
      self_am.name_am = name_am
      self_am.email_am = email_am
      self_am.age_am = age_am
      self_am.balance = 0

  def set_balance(self_am, balance):
      self_am.balance = balance

  def greeting(self_am):
      return f'My name_am is {self_am.name_am} and I am {self_am.age_am} and my balance is {self_am.balance}'

#  Init user object
brad = User('Brad Traversy', 'brad@gmail.com', 37)
# Init customer object
janet = Customer('Janet Johnson', 'janet@yahoo.com', 25)

janet.set_balance(500)
print(janet.greeting())

brad.has_birthday()
print(brad.greeting())

#Encapsulation -->
brad.print_encap()
brad._private = 800 #Changing for brad
brad.print_encap()

# Method inherited from parent
janet.print_encap() #Changing the variable for brad doesn't affect janets variable --> Encapsulation
janet._private = 600
janet.print_encap()

#Similary changing janet's doesn't affect brad's variable.
brad.print_encap()
