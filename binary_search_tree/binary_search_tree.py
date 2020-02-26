# import sys
# sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        node = self

        while True:
            if node.value > value:
                if node.left:
                    node = node.left
                else:
                    node.left = BinarySearchTree(value)
                    break
            else:
                if node.right:
                    node = node.right
                else:
                    node.right = BinarySearchTree(value)
                    break

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, value, node=0):
        # found = False

        if node == 0:
            node = self

        if node == None:
            return False
        if node.value == value:
            return True

        if value > node.value:
            return self.contains(value, node.right)
        else:
            return self.contains(value, node.left)

        # return found

    # Return the maximum value found in the tree
    def get_max(self, node=0):
        if node == 0:
            node = self

        if node.right == None:
            return node.value
        return self.get_max(node.right)

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb, node=False):

        if node:
            self = node

        cb(self.value)
        if self.left:
            cb(self.left.value)
            self.for_each(cb, self.left)
        if self.right:
            cb(self.right.value)
            self.for_each(cb, self.right)

    # DAY 2 Project -----------------------

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

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
