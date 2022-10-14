# Names: Dallin Duke, Emily Reyes, Mason Hunter, and Toa Pita
# Section: 003
# Project Description: Simulate a resturant order line using dictionaries, lists, and objects

# Process a queue into a dictionary
def process_queue(customerQueue):
    # create a customer dictionary
    customerDictionary = {}
    # loop through the passed in queue
    for x in range(0, len(customerQueue)) :
        # remove customer from queue
        cust = customerQueue.pop(0)
        # add customer to dictionary using name as key and burger_count as value
        # if they already exisit just update their order
        if cust.customer_name in customerDictionary:
            customerDictionary[cust.customer_name] += cust.order.burger_count
        else:
            customerDictionary[cust.customer_name] = cust.order.burger_count
    # return completed dictionary
    return customerDictionary

# create the output from a dictionary
def createOutput(custTotals):
    # take each item from the dictionary and add it to a list sorted on values in descending order
    sortedCust = sorted(custTotals.items(), key=lambda x: x[1], reverse=True)

    # Create an output variable and assign it an line break for readabilility 
    output = "\n"

    # loop through the sorted list and concatenate to create the output
    for i in sortedCust:
        # add customer name with blank spaces to add padding until all names are length 19
        # add a tab for readabillity
        # convert burger count to string and concat that value
        # add a line break for readabililty
        output += i[0].ljust(19) + "\t" + str(i[1])+"\n"
    # return the output
    return output