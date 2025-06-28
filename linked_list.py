
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
    
    def test_insert(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            return
        
        self.head.next = node
        self.head = node


    def insert(self, data):
        node = Node(data)

        if not self.head:
            self.head = node
            return
        
        last = self.head
        while last.next:
            last = last.next
        last.next = node
    
    def get(self, data):
        last = self.head
        while last:
            if last.data == data:
                return "FOUND"
            last = last.next
        return "NOT_FOUND"
        
    
    def delete(self, data):
        if not self.head:
            return

        last = self.head
        previous = None

        while last:
            if last.data == data:
                if previous:
                    previous.next = last.next
                else:
                    self.head = last.next
                return

            previous = last
            last = last.next

    
    def print_data(self):
        last = self.head
        while last:
            print("val_____", last.data)
            last = last.next  
            

obj = SingleLinkedList()   
obj.insert(10)
obj.insert(20)
obj.insert(30)
obj.insert(40)
obj.delete(10)
print(obj.get(20))

obj.print_data()
