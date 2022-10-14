# Names: Dallin Duke, Emily Reyes, Mason Hunter, and Toa Pita
# Section: 003
# Project Description: Simulate a resturant order line using dictionaries, lists, and objects

# Import all our custom stuff
from classes import Customer
from functions import createOutput
from functions import process_queue

# Create customer queue
customerQueue = []
# Add 100 customers
for x in range(100):
    # create customer and append
    customer = Customer()
    customerQueue.append(customer)

# Create a customer dictionary while processing the queue
customerDictionary = process_queue(customerQueue)

# take each item from the dictionary and add it to a list sorted on values in descending order
output = createOutput(customerDictionary)

# print out our final product
print(output)