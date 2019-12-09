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

    # returns the node (or a tree) whose data same as 
    # that provided in the argument
    def search(self,tree,data):
        if tree == None:
            return None
        if tree.data == data:
            return tree
        elif data <= tree.data:
            return self.search(tree.left,data)
        else:
            return self.search(tree.right,data)

    # returns the node whose value if the
    # maximum in the tree
    def max_node(self,node):
        if node is None:
            return None

        if node.right is None:
            return node
        return self.max_node(node.right)

    # returns the node whose value is the 
    # minimum in the tree
    def min_node(self,node):
        if node is None:
            return None
        if node.left is None:
            return node
        return self.min_node(node.left)

    # returns the parent node of the provided tree (node)
    def getParent(self,tree,data):
        if tree is None or tree.data == data:
            return None
        if tree.left is not None:
            if tree.left.data == data:
                return tree
        if tree.right is not None:
            if tree.right.data == data:
                return tree
        if data <= tree.data:
            return self.getParent(tree.left,data)
        else:
            return self.getParent(tree.right,data)

    # delete the node whose data is same as that
    # provided in the argument
    def delete(self,data):
        node = self.search(self.root,data)
        if node is None:
            return "Data does not exist in the tree"
        
        # find the parent node of the node to be deleted
        parent = self.getParent(self.root,data)
        # if its a leaf node
        if node.left is None and node.right is None:
            if parent is None:
                return None
            if parent.left.data == data:
                parent.left = None
            elif parent.right.data == data:
                parent.right = None
        # if it has exactly one child
        elif (node.left is None and node.right is not None) or (node.right is None and node.left is not None):
            if parent.left is not None and parent.left.data == node.data:
                if node.left:
                    parent.left = node.left
                else:
                    parent.left = node.right
            else:
                if node.left:
                    parent.right = node.left
                else:
                    parent.right = node.right

        # if it has both children 
        else:
            # we can swap with either predecessor (i.e max of the left sub-tree)
            # or successor (i.e min of the right sub-tree), choosing predecessor.
            predecessor = self.max_node(node.left)

            # now delete the predecessor node

            # predecessor is a leaf node, apply the logic for leaf node
            # find parent of the predecessor node
            parent = self.getParent(self.root,predecessor.data)
            if parent is None:
                return None
            # swap the value of the predecessor with the node 
            node.data = predecessor.data
            if parent.left == predecessor:
                parent.left = None
            elif parent.right == predecessor:
                parent.right = None







if __name__ == "__main__":
    t = BST()
    t.insert(2)
    t.insert(4)
    t.insert(1)
    t.insert(5)
    t.insert(33)
    t.insert(11)
    t.insert(40)
    in_order(t.root)  
    t.delete(1)    
    print("After deletion:")
    in_order(t.root)  
    print("max: ",t.max_node(t.root).data)
    print("min: ",t.min_node(t.root).data)
