# Unordere, changeable and indexed. No DuplicateSectionError

# Create dict
person = {
    'first name' : 'John',
    'last name' : 'Doe',
    'age' : 30
}

# Use constructor
#person2 = dict(firstName = 'Sara', lastName = 'Williams')

# Get value
print(person['first name'])
print(person.get('last name'))

# Add key/value
person['phone'] = '999-999-9999'

# Get dict keys
print(person.keys())

# Get dict items
print(person.items())

# Copy dict
person2 = person.copy()
person2['city'] = 'Boston'

# Remove item
del(person['age'])
person.pop('phone')

# Clear dictionary
person.clear()

# Get Length
print(len(person2))

# List of dict
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 35}
]

print(person)
print(people[1]['name'])