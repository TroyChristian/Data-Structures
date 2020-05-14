"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if the incoming value is less than the current nodes value
        if value < self.value:
            # we know to go left

            if not self.left:
                #We cam park our value here if self.left is empty
                self.left = BSTNode(value)
            else:
                # We cant park here, so we go further down and to the left, by inserting on whatever is in self.left
                self.left.insert(value)
        
        else:
            #we know to go right
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        pass

    # Return the maximum value found in the tree
    def get_max(self):
        # We'll keep going right until there are no more nodes on the right side.
        if not self.right:
            return self.value
        return self.right.get_max() 

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call the fn on the value at this node
        fn(self.value)

        #pass this function to the left child
        if self.left:
            self.left.for_each(fn)

        # pass this function  to the right child
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
