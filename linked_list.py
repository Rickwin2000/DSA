
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

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
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)

        if not self.head:
            self.head = node
            return
        
        last = self.head

        while last.next:
            last = last.next
        
        node.prev = last
        last.next = node
    
    def delete(self, data):

        if not self.head:
            return

        if self.head.data == data:
            self.head = None
        
        last = self.head

        while last:
            if last.data == data:
                previous = last.prev
                next = last.next
                
                if next:
                    next.prev = previous
                if previous:
                    previous.next = next

            last = last.next
    
    def print_ln(self):
        current = self.head

        while current:
            # print("current val_____ ", current.data)
            if current.prev:
                print("prev value_______ ", current.data, current.prev.data)
            else:
                print("prev value_______", current.data, None)
            current = current.next


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)

        if not self.head:
            self.head = node
            self.head.prev = node
            self.head.next = node
            return
        
        last = self.head.prev
        last.next = node
        node.prev = last
        node.next = self.head
        self.head.prev = node
    
    def print_ln(self):
        current = self.head

        if not self.head:
            return

        current = self.head
        while True:
            print(f"Node: {current.data}, Prev: {current.prev.data}, Next: {current.next.data}")
            current = current.next
            if current == self.head:
                break


def trigger_single_linked_list():
    obj = SingleLinkedList()   
    obj.insert(10)
    obj.insert(20)
    obj.insert(30)
    obj.insert(40)
    obj.delete(10)
    print(obj.get(20))

def trigger_doubly_linked_list():
    obj = DoublyLinkedList()
    obj.insert(10)
    obj.insert(20)
    obj.delete(20)
    obj.insert(30)
    obj.print_ln()

def trigger_circular_linked_list():
    obj = CircularLinkedList()
    obj.insert(10)
    obj.insert(20)
    obj.insert(30)
    obj.print_ln()

trigger_circular_linked_list()