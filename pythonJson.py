# JSON is commonly used with data APIs. Parse JSON into a python dictionary

import json

# Sample json
userJSON = '{"first_name" : "Siddharth", "last_name": "Choudhary", "age": 22}'

# Parse to dictionary
user = json.loads(userJSON)

print(user)
print(user['first_name'])

car = {'make' : 'Ford', 'model': 'Mustand', 'year': 1970}
carJSON = json.dumps(car)
print(carJSON)
