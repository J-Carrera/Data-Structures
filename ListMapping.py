class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return str(self.key) + " : " + str(self.value)

class ListMapping:
    def __init__(self):
        self._entries = []

    def put(self, key, value):
        """ Add key-value entry. """
        #If key already exist, update its value
        #else add the new key-value pair
        pass
        #To remove


    def get(self, key):
        """ Returns the value associated with key. """
        #scan through the list with the help of _entry() method
        #Raise KeyError if the input key does not exist
        pass


    def remove(self, key):
        """ Remove the object associated with key. """
        pass


    def _entry(self, key):
        """ Scan through all entries in the list. """
        #Returns the entry if the key exists.
        #Otherwise return None
        pass



    def __len__(self):
        """ Returns total number of entries added in the list. """
        return len(self._entries)

    def __contains__(self, key):
        """ Returns True if key exist, else returns False. """
        if self._entry(key) is None:
            return False
        else:
            return True

    def items(self):
        """ Returns an iterator over the key-value pairs as tuples. """
        return ((e.key, e.value) for e in self._entries)


if __name__ == "__main__":
    map = ListMapping()
    map.put(1, "one")
    map.put(2, "two")
    map.put(3, "three")
    map.put(4, "four")
    print(map.get(1))
    print(map.get(3))
    print(map.get(4))
