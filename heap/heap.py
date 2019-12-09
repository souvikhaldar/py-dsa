
class Heap:
    def __init__(self,limit):
        self.next = None 
        self.heap = []
    
    def left_child(self,pos):
        try:
            return 2*pos 
        except IndexError as e:
            print(e)

    def right_child(self,pos):
        try:
            return 2*pos+1
        except IndexError as e:
            print(e)

    def parent(self,pos):
        try:
            return pos//2
        except IndexError as e:
            print(e)

    def restructure(self,data,pos):

    def insert(self,data):
        self.heap[self.next] = data  

