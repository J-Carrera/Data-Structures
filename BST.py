class BSTNode:
    def __init__(self, data, parent = None):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    ################ Task 1 ################
    def insert(self, data):
        pass
        #use helper _add_child method to add children to existing parent


    def _add_child(self, data, p_node):
        if data == p_node.data: #duplicate items cannot be added
            return

        #implement logic to recursively add a node at appropriate location
        pass

    def get_max(self):
        #retrieve the appropriate node with the help of
        # helper method _get_right_child
        pass

    def _get_right_child(self, node):
        #helper method to retrieve right node recursively
        pass

    def get_min(self):
        #retrieve the appropriate node with the help of
        # helper method _get_left_child
        pass

    def _get_left_child(self, node):
        #helper method to retrieve left node recursively
        pass

    def traverse_in_order(self, node, traversed_data):
        #traverse the tree in in-order fashion and keep
        #adding the elements in the traversed_data list
        pass

    def delete(self, data):
        #starting from root node, pass the data and node
        #to be deleted to the helper node _remove_node
        if self.root:
            self._remove_node(data, self.root)

    def _remove_node(self, data, node):
        #remove the specified node
        #separate cases for deleting leaf node, node with one child and
        #node with two children

        #For deleting root node with two children, use the
        #helper method _get_predecessor to get the predecessor
        pass

    def _get_predecessor(self, node):
        if node.right:
            return self.get_predecessor(node.right)

        return node

    ################ Task 2 ################
    def traverse_pre_order(self, node, traversed_data):
        #traverse the tree in pre-order fashion and keep
        #adding the elements in the traversed_data list
        pass

    def traverse_post_order(self, node, traversed_data):
        #traverse the tree in post-order fashion and keep
        #adding the elements in the traversed_data list
        pass



if __name__ == "__main__":
    BST = BinarySearchTree()

    random_data = [12, 4, 20, 8, 1, 16, 27]
    for data in random_data:
        BST.insert(data)

    print("Testing Max...")
    assert(BST.get_max() == 27)
    print("PASSED!")

    print()
    print("Testing Min...")
    assert(BST.get_min() == 1)
    print("PASSED!")

    print()
    print("Testing In-order Traversal...")
    traversed_data = []
    BST.traverse_in_order(BST.root, traversed_data)
    assert(traversed_data == [1, 4, 8, 12, 16, 20, 27])
    print("PASSED!")

    print()
    print("Testing Deletion of root node with two child...")
    BST.delete(12)
    traversed_data = []
    BST.traverse_in_order(BST.root, traversed_data)
    assert(traversed_data == [1, 4, 8, 16, 20, 27])
    print("PASSED!")

    print()
    print("Checking new root after deletion...")
    assert(BST.root.data == 8)
    print("VERIFIED!")

    ########## Task2 ##########
    print()
    print("########## Task 2 ##########")
    BST2 = BinarySearchTree()
    #            12
    #       4         20
    #     1   8    16   27
    random_data = [12, 4, 20, 8, 1, 16, 27]
    for data in random_data:
        BST2.insert(data)

    print()
    print("Testing Pre-order Traversal...")
    traversed_data = []
    BST2.traverse_pre_order(BST2.root, traversed_data)
    assert(traversed_data == [12, 4, 1, 8, 20, 16, 27])
    print("PASSED!")

    print()
    print("Testing Post-order Traversal...")
    traversed_data = []
    BST2.traverse_post_order(BST2.root, traversed_data)
    assert(traversed_data == [1, 8, 4, 16, 27, 20, 12])
    print("PASSED!")
