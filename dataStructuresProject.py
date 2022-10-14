# Dallin Duke
# The Dictionary and remove queue
 
# Masons add to queue function
 
customerQueue = []
 
customerDictionary = {}
for x in range(100):
    order = order()
 
    customer = Customer(order)
 
    customerQueue.append(customer)
 
for x in range(0, len(customerQueue)) :
    cust = customerQueue.pop(0)
    customerDictionary[cust.customer_name] = cust.order.burger_count
   
 

