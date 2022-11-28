class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self,head):
        self.head = head
    
    def print_nodes(self):
        current = self.head or None
        while current != None:
            print(current.val)
            current = current.next
        return
    
    def append(self,val,next=None):
        new_node = Node(val,next=next)
        if self.head is None:
            self.head = new_node
            return
        end = self.head
        while end!=None:
            end = end.next
        end.next = new_node

    def prepend(self,val):
        new_node = Node(val)

        new_node.next = self.head
        self.head = new_node

    def insert_after(self,prev_node,val):
        if not prev_node:
            return f'{prev_node} is not in the linked list'

        new_node = Node(val)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self,val):
        current = self.head

        if current.val == val:
            current.next = self.head
            current = None
            return

        while current and current.val != val:
            previous = current
            current = current.next

        if not current:
            return f'{val} not in linked list'

        previous.next = current.next
        current = None

    def delete_position(self,pos):
        if self.head:
            current = self.head
            if pos == 0:
                self.head = self.head.next
                return
        count = 0
        while count < pos and current:
            previous = current
            current = current.next
            count +=1

        if not current:
            return f'{pos} not in linked list'

        previous.next = current.next
        current = None
        