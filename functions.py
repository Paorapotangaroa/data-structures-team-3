def process_queue(customerQueue):
    customerDictionary = {}
    for x in range(0, len(customerQueue)) :
        cust = customerQueue.pop(0)
        if cust.customer_name in customerDictionary:
            customerDictionary[cust.customer_name] += cust.order.burger_count
        else:
            customerDictionary[cust.customer_name] = cust.order.burger_count
    return customerDictionary