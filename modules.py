# file containing a set of functions to include in application. Core python modules, 
# Modules installed using pip package manager and custom modules

# Core modules
import datetime
from datetime import date
import time
from time import time

# Pip module
from camelcase import CamelCase

# Import custom module
import validator
from validator import validateEmail

#today = datetime.date.today() 
today = date.today()
timestamp = time()

c = CamelCase()
print(c.hump('hello there world'))

email = 'test@test.com'
if validateEmail(email):
    print('Email is valid')
else:
    print('Email is bad')

print(timestamp) 