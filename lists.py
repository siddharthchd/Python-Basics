# Mutable. Allows duplicate, ordered and changeable

# Create list
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Use a constructor
#numbers2 = list((1, 2, 3, 4, 5))

# Get a value
print(fruits[1])

# Get length
print(len(fruits))

# Append to list
fruits.append('Mangos')

# Remove from list
fruits.remove('Grapes')

# Insert into position
fruits.insert(2, 'Strawberries')

# Change Value
fruits[0] = 'Blueberries'

# Remove with pop
fruits.pop(2)

# Reverse List
fruits.reverse()

# Sort List
fruits.sort()

# Reverse Sort
fruits.sort(reverse=True)

print(fruits)

