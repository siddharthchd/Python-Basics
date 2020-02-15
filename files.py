# Open a file
myFile = open('myfile.txt', 'w')

# Get some info on file
print('Name : ', myFile.name)
print('Is Closed : ', myFile.closed)
print('Opening Mode : ', myFile.mode)

# Write to file
myFile.write('I am doing this from python')
myFile.write(' and this is fun')
myFile.close()

# Append to file
myFile = open('myFile.txt', 'a')
myFile.write('. I also like Java')
myFile.close()

# Read from file
myFile = open('myFile.txt', 'r+')
text = myFile.read(100)
print(text)