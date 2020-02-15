people = ['John', 'Paul', 'Sarah', 'Susan']

# simple for loop
for person in people:
    print(f'Current Person: {person}')
    
# Break
for person in people:
        if person == 'Sarah':
            break
    #print(f'Current Person: {person}')
    
# Continue
for person in people:
    if person == 'Sarah':
        continue
    #print(f'Current Person: {person}')

# Range
for i in range(len(people)):
    print(people[i])

for i in range(0, 11):
    print(f'Number: {i}')
    
# While loops

count = 0
while count <= 10:
    print(f'Count : {count}')
    count += 1