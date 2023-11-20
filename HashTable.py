from ListMapping import ListMapping

class HashTable:
    def __init__(self):
        self._htsize = 5      #initial size of hash table
        self._buckets_array = #initialize bucket array of size _htsize
        self._n = 0         #number of items added in map

    def put(self, key, value):
        """ put the key-value pair in the right bucket. """
        #Evaluate the address of bucket to hold key-value pair
        bucket = self._get_bucket(key)
        pass


    def get(self, key):
        """ Returns the value associated with key from the right bucket. """
        pass

    def _get_bucket(self, key):
        """ Returns the right jth bucket depending on key. """
        #calculate jth index with the help of hash function as discussed in class
        pass

    def remove(self,key):
        """ Remove the object associated with key. """
        #After removing, decrease the size of entries in map


    def _double(self):
        """ Doubles the size of hash table. """
        #Create a new hash table with size double the original one
        #After creating a new double-sized hash table, add the contents
        #of original hash table in it.
        pass



if __name__ == "__main__":
    HM = HashTable()

    HM.put(1, "one")
    HM.put(2, "two")
    HM.put(3, "three")
    HM.put(4, "four")
    HM.put(5, "five")
    HM.put(6, "six")
    HM.put("ten", 10)

    assert(HM.get(2) == "two")
    assert(HM.get(4) == "four")
    assert(HM.get("ten") == 10)
    assert(HM._htsize == 10)
    assert(HM._n == 7)
    print("PASSED")
