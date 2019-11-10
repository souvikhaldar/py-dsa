from .singly_linked_list import singly_linked_list,node

class doubly_node(node):
    def __init__(self,data):
        self.prev = None
        super().__init__(data)

class doubly_linked_list(singly_linked_list):
    def __init__(self):
        super().__init__()

    def insert_at_beg(self,data):
        new_node = doubly_node(data)
        if self.head is not None:
            new_node.next = self.head 
            self.head.prev = new_node
        self.head = new_node
    
    def insert_at_end(self,data):
        new_node = doubly_node(data)
        temp = self.head
        while temp.next:
            temp = temp.next 
        new_node.prev = temp
        temp.next = new_node
        

    def backward_print(self):
        temp = self.head
        while temp.next:
            temp = temp.next 
        while temp:
            print(temp.data)
            temp = temp.prev


        
            

