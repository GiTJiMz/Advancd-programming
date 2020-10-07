def merge(xs, ys):
    """ Merges two sorted lists

    >>> merge([], [])
    []
    >>> merge([], [1,2])
    [1, 2]
    >>> merge([1,2], [])
    [1, 2]
    >>> merge([1,3], [2,4])
    [1, 2, 3, 4]
    """

    # Recursive

    if not xs:
        return ys
    if not ys:
        return xs
    
    x, *xs_rest = xs
    y, *ys_rest = ys
    if x < y:
        return [x] + merge(xs_rest, ys)
    else:
        return [y] + merge(xs, ys_rest)
    
    # Iterative


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("Damn I'm good")