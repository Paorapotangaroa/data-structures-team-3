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
    
    return output
    
# take each item from the dictionary and add it to a list sorted on values in descending order
output = createOutput(custTotals)
print(output)