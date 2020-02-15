# Create class

class User:
    #Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email 
        self.age = age
        
    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'
    
    def hasBirthday(self):
        self.age += 1
        
# Extend class
class Customer(User):
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email= email
        self.age = age
        self.balance = 0
        
    def setBalance(self, balance):
        self.balance = balance
    
    
# Init user object
sid = User('Siddharth Choudhary', 'siddharth@gmail.com', 22)

# Init user object
janet = Customer('Janet Johnson', 'Janet@yahoo.com', 25)

janet.setBalance(500)
print(janet.greeting())

sid.hasBirthday()
print(sid.greeting())