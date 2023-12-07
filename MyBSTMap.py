from BSTMap import BSTMap, BSTNode # provided for you

# Inherit from BSTMap, but overload `newnode` to use this one instead
class MyBSTMap(BSTMap):
   
    def newnode(self, key, value = None):
        return MyBSTNode(key, value)    # overloads the `newnode` method to use MyBSTNode() instead of BSTNode()

    # TODO: implement the three methods below
    def __eq__(self, other):
        """ADD DOCSTRING"""
             # The heavy lifting here is done in the corresponding
             # function in MyBSTNode - just tell it which node to
             # start with.

   

class MyBSTNode(BSTNode):
   
    newnode = MyBSTMap.newnode  # overloads the `newnode` method to use the correct Node class

    # TODO: implement the method below
    def __eq__(self, other):
        """ADD DOCSTRING"""