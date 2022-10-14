import random

class Order :
    def __init__(self):
        self.burger_count = self.randomBurgers()
        

    def randomBurgers(self) :
        burger_count = random.randint(1, 20)
        return(burger_count)
    

class Person :
    def __init__(self):
        self.customer_name = self.randomName()

    def randomName(self) :
        asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        customer_name = random.choice(asCustomers)
        return(customer_name)


class Customer(Person) :
    def __init__(self) :
        super().__init__ ()
        self.order = Order()