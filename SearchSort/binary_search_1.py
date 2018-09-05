"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    """Your code goes here."""
    search_array = input_array
    while True:
        if len(search_array) == 1:
            if value == search_array[0]:
                counter = 0
                for val in input_array:
                    if value == val:
                        return counter
                    counter = counter + 1       
            else:
                break;
        else:
            mid_point = len(search_array)/2
            if value == search_array[mid_point]:
                return mid_point
            if value < search_array[mid_point]:
                search_array = search_array[:mid_point]
            else:
                search_array = search_array[mid_point+1:]
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
#should print -1
print binary_search(test_list, test_val1)
#should print 4
print binary_search(test_list, test_val2)
