#Implement a Binary Tree data structure

class Binary_Node():

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class Binary_Tree():

    def __init__(self, root=None):

node15 = Binary_Node(15)
node9 = Binary_Node(9)
node38 = Binary_Node(30)
node8 = Binary_Node(8)

btree = Binary_Tree(node15)