def prodof(numbers):
    
    product = 1
    
    # product should containt the
    # product of all numbers seen so far.
    for number in numbers:
        product = product * number
    
    return product

def indexof(lst, item):
    index = -1
    
    # index should see the index of the
    # first item in the list equal to item.
    for (i, l) in enumerate(lst):
        if index != -1 and l == item:
            index = i
    
    return index
            
def count_positive(numbers):
    if not numbers: return 0
    
    head, *rest = numbers
    if head > 0:
        return count_positive(rest) + 1
    else:
        return count_positive(rest)
    
def count_positive_for(numbers):
    count = 0
    for head in numbers:
        if head > 0:
            count += 1
    return count
