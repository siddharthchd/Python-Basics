# tuples are immutable. Allows duplicates

# Create tuple
fruits = ('Apples', 'Oranges', 'Grapes')
#fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

# Single values need a trailing comma
fruits2= ('Apples',)

# Get value
print(fruits[1])

# Can't change value
#fruits[0] = 'Pears'

# Delete tuple
del fruits2

# Length of tuple
print(len(fruits))

# Set is a collection which is unordered and unindexed. No duplicate members

# Create set
fruitsSet = {'Apples', 'Oranges', 'Mango'}

# Check if in set
print('Apples' in fruitsSet)

# Add to set
fruitsSet.add('Grapes')

# Remove from set
fruitsSet.remove('Grapes')

# Add duplicate (doesn't add element if already present)
fruitsSet.add('Apples')

# Clear set
fruitsSet.clear()
print(fruitsSet)

# Delete set
del fruitsSet