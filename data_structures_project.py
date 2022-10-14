# import random library
import random

# Create Order class
class Order :
    def __init__(self):
        # call randomBurgers method in the constructor
        self.burger_count = self.randomBurgers()
        
    # randomBurgers method created
    def randomBurgers(self) :
        burger_count = random.randint(1, 20)
        # Choose random number between 1 and 20 and assign it to the variable burger_count
        return(burger_count)
    
# Create Person class
class Person :
    def __init__(self):
        # call randomName method in constructor
        self.customer_name = self.randomName()

    # randomName method created
    def randomName(self) :
        asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        # Choose a random name from the above list
        customer_name = random.choice(asCustomers)
        return(customer_name)

# Create customer class that inherits from Person
class Customer(Person) :
    def __init__(self) :
        super().__init__ ()
        # create order object
        self.order = Order()