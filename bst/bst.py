class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
# helper methods
def insertNode(tree,node):
    if node.data <= tree.data:
            if tree.left:
                insertNode(tree.left,node)
            else:
                tree.left = node
                return
    else:
        if tree.right:
            insertNode(tree.right,node)
        else:
            tree.right = node
            return

# print in-order
def in_order(tree):
    if tree.left:
        in_order(tree.left)
    print(tree.data)
    if tree.right:
        in_order(tree.right)

# Binary Search Tree
class BST:
    def __init__(self):
        self.root = None

    def insert(self,data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            insertNode(self.root,new_node)

if __name__ == "__main__":
    t = BST()
    t.insert(2)
    t.insert(4)
    t.insert(1)
    t.insert(5)
    t.insert(33)
    t.insert(11)
    in_order(t.root)        
