class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class singly_linked_list:
    def __init__(self):
        self.head = None 
    # insert a new node at the beginning of the linked list
    def insert_at_beg(self,data):
        new_node = node(data)
        if self.head != None:
            new_node.next = self.head
        self.head = new_node
    # insert a node at the end of the linked list
    def insert_at_end(self,data):
        new_node = node(data)
        temp = self.head
        while (temp.next):
            temp = temp.next
        temp.next = new_node

    # insert a node after nth position, position starts from 0
    def insert_after(self,data,n):
        new_node = node(data)
        temp = self.head
        counter = 0
        while temp:
            if counter == n:
                break
            else:
                counter+=1
                temp = temp.next
        if counter != n:
            print("{} is not a valid position".format(n))
            return
        new_node.next = temp.next
        temp.next = new_node

    # delete from the beginning
    def delete_from_beg(self):
        if self.head is not None:
            self.head = self.head.next

    # delete at the end
    def delete_at_end(self):
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None

    # delete after position n, postion starts from 0
    def delete_after_n(self,n):
        counter = 0
        temp = self.head
        while temp:
            if counter == n:
                break
            counter +=1 
            temp = temp.next
        if counter != n:
            print("{} is not valid postion".format(n))
        temp.next = temp.next.next

    def forward_print(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

