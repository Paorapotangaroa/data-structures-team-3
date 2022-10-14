customerQueue = []
customerDictionary = {}
from data_structures_project import Customer
for x in range(100):
    customer = Customer()
    customerQueue.append(customer)
for x in range(0, len(customerQueue)) :
    cust = customerQueue.pop(0)
    customerDictionary[cust.customer_name] = cust.order.burger_count
