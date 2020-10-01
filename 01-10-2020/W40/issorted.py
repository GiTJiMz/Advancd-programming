def issorted(lst):
    """Check if a list is sorted
    
    >>> issorted([])
    True
    
    >>> issorted([3])
    True

    >>> issorted([7, 9, 13])
    True
    
    >>> issorted([7, 22, 13])
    False

    """

    return False


# this helps us test the code, is only run if we
# run the module:
if __name__ == '__main__':
    import doctest
    doctest.testmod()

