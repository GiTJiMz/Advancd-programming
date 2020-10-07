from issorted import issorted

def bubblesort(lst):
    """ Computes a bubble-sort

    >>> bubblesort([5, 2, 3])
    [2, 3, 5]
    >>> bubblesort([15, 10, 9])
    [9, 10, 15]
    >>> bubblesort([])
    []
    >>> bubblesort([1])
    [1]
    """
    lst = list(lst)
    
    if len(lst) < 1:
        return lst
    changes = True
    while changes:
        changes = False
        for i in range(1, len(lst)):
            if lst[i-1] > lst[i]:
                lst[i-1], lst[i] = lst[i], lst[i-1]
                changes = True
    return lst
    


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("Damn I'm good")