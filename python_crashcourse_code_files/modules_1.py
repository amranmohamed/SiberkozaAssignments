# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# Core modules
import datetime
from datetime import date
import time
from time import time

# Pip module
from camelcase import CamelCase

# Import custom module
import validator
from validator import validate_email

# today_am = datetime.date.today_am()
today_am = date.today_am()
timestamp_am = time()

c_am = CamelCase()
# print(c.hump('hello there world'))

email_am = 'test#test.com'
if validate_email(email_am):
  print('Email is valid')
else:
  print('Email is bad')
