from createOutput import createOutput
from data_structures_project import Customer
from functions import process_queue
customerQueue = []
for x in range(100):
    customer = Customer()
    customerQueue.append(customer)
customerDictionary = process_queue(customerQueue)
# take each item from the dictionary and add it to a list sorted on values in descending order

output = createOutput(customerDictionary)
print(output)