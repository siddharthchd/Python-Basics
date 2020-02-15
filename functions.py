# Create function
def sayHello(name = 'Sam'):
    print(f'Hello {name}')
    
# Return value
def getSum(num1, num2):
    total = num1 + num2
    return total

num = getSum(3, 4)
print(num)

# Lambda function is a small anonymous function
# Can take any number of arguments, but can only have one expresison

getSum = lambda num1, num2 : num1 + num2
print(getSum(10, 3))