# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

#  Sample JSON
userJSON_am = '{"first_name": "John", "last_name": "Doe", "age": 30}'

# Parse to dict
user_am = json.loads(userJSON_am)

# print(user_am)
# print(user_am['first_name'])

car_am = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}

carJSON_am = json.dumps(car_am)

print(carJSON_am)