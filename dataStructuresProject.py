# Dallin Duke
# The Dictionary and remove queue
 
# Masons add to queue function
 
customerQueue = []
 
customerDictionary = {}
for x in range(100):
    order = order()
 
    customer = Customer(order)
 
    customerQueue.append(customer)
 
for x in range(len(customerQueue)) :
    customerDictionary[customer] = x
    customerQueue.pop(0)
 
listSortedCustomers = sorted(customerDictionary.items(), key=lambda x: x[1], reverse=True) 
for x in range(len(customerDictionary), 1) :
    print(listSortedCustomers(0,1))
