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
        if self.root is None:
            self.root = BSTNode(data)
        else:
            self._add_child(data, self.root)
        #use helper _add_child method to add children to existing parent


    def _add_child(self, data, p_node):
        if data == p_node.data: #duplicate items cannot be added
            return
        if data < p_node.data:
            if p_node.left:
                self._add_child(data, p_node.left)
            else:
                p_node.left = BSTNode(data, p_node)
        else:
            if p_node.right:
                self._add_child(data, p_node.right)
            else:
                p_node.right = BSTNode(data, p_node)


        #implement logic to recursively add a node at appropriate location
       

    def get_max(self):
        if self.root:
            return self._get_right_child(self.root)
        else:
            return None
        #retrieve the appropriate node with the help of
        # helper method _get_right_child
        

    def _get_right_child(self, node):
        #helper method to retrieve right node recursively
        if node.right:
            return self._get_right_child(node.right)
        return node.data

    def get_min(self):
        #retrieve the appropriate node with the help of
        # helper method _get_left_child
        if self.root:
            return self._get_left_child(self.root)
        else:
            return None

    def _get_left_child(self, node):
        #helper method to retrieve left node recursively
        if node.left:
            return self._get_left_child(node.left)
        return node.data
    
    def _get_predecessor(self, node):
        if node.right:
            return self.get_predecessor(node.right)

        return node


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
        if node == None:
            return
        if data < node.data:
            self._remove_node(data, node.left)
        elif data > node.data:
            self._remove_node(data, node.right)
        else:
            if node.left == None and node.right == None:
                j = node.parent
                if j != None:
                    if j.right == node:
                        j.right = None
                    if j.left == node:
                        j.left = None
                else:
                    self.root = None

                del node
            elif node.left != None and node.right == None:
                j = node.parent
                if j != None:
                    if j.right == node:
                        j.right = node.right
                    if j.left == node:
                        j.left = node.right
                else:
                    self.root = node.right
                node.right.parent = j
                del node
            else:
                z = self._get_predecessor(node.left)
                z.data, node.data = node.data, z.data
                self._remove_node(data, z)


    
    def traverse_in_order(self, node, traversed_data):
        #traverse the tree in in-order fashion and keep
        #adding the elements in the traversed_data list
        if node != None:
            self.traverse_in_order(node.left, traversed_data)
            traversed_data.append(node.data)
            self.traverse_in_order(node.right, traversed_data)

    ################ Task 2 ################
    def traverse_pre_order(self, node, traversed_data):
        #traverse the tree in pre-order fashion and keep
        #adding the elements in the traversed_data list
        if node != None:
            traversed_data.append(node.data)
            self.traverse_pre_order(node.left, traversed_data)
            self.traverse_pre_order(node.right, traversed_data)
    def traverse_post_order(self, node, traversed_data):
        #traverse the tree in post-order fashion and keep
        #adding the elements in the traversed_data list
        if node != None:
            self.traverse_post_order(node.left, traversed_data)
            self.traverse_post_order(node.right, traversed_data)
            traversed_data.append(node.data)



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
