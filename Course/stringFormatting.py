# String formatting

print('Today I had {0} cups of {1}'.format(3, "coffee"))
print('price: ({x}, {y}, {z})'.format(x = 2.0, y = 1.5, z = 5))
print("The {vehicle} had {0} crashes in {1} months".format(5, 6, vehicle = 'car'))

# Specify character which replace the empty spaces and the number of spaces that the string will occupy.
# If that number is smaller than the string length then the string will be printed out without allignment.

print('{:<20}'.format("text"))
print('{:>20}'.format("text"))

# Binary
print('{:b}'.format(21))

# Hexadecimal
print('{:x}'.format(21))

# Decimal
print('{:}'.format(21))

# Octal
print('{:o}'.format(21))