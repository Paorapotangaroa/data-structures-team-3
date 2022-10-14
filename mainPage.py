from createOutput import createOutput
from data_structures_project import Customer

customerQueue = []
customerDictionary = {}

for x in range(100):
    customer = Customer()
    customerQueue.append(customer)
for x in range(0, len(customerQueue)) :
    cust = customerQueue.pop(0)
    if cust.customer_name in customerDictionary:
        customerDictionary[cust.customer_name] += cust.order.burger_count
    else:
        customerDictionary[cust.customer_name] = cust.order.burger_count
# take each item from the dictionary and add it to a list sorted on values in descending order

output = createOutput(customerDictionary)
print(output)