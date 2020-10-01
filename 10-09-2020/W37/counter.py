def collecter():
    collection = set()
    
    def inner(var):
        collection.add(var)
        return collection
    
    return inner