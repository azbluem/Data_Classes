class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self,head=None):
        self.head = head
    
    def print_nodes(self):
        current = self.head or None
        while current != None:
            print(current.val)
            current = current.next
        return
    
    def append(self,val,next=None):
        new_node = Node(val,next)
        if self.head is None:
            self.head = new_node
            return
        end = self.head
        while end.next!=None:
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

    def __len__(self):
        count = 0
        current = self.head
        while current:
            current = current.next
            count += 1
        return count
    
    def recursive_len(self,node):
        if not node:
            return 0
        return 1+self.recursive_len(node.next)

    def swap_nodes(self,val1,val2):
        if val1==val2:
            return
        node1 = self.head
        prev1 = None
        node2 = self.head
        prev2 = None

        while node1 != val1 and node1:
            prev1 = node1
            node1 = node1.next
        while node2 != val2 and node2:
            prev2 = node2
            node2 = node2.next
        if not node1 and not node2:
            return f'One of your given values {val1} or {val2} is not in the linked list'

        if prev1:
            prev1.next = node2
        else:
            self.head = node2

        if prev2:
            prev2.next = node1
        else:
            self.head = node1

        node1.next,node2.next = node2.next,node1.next

    def iterative_reversal(self):
        current = self.head
        prev = None
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        self.head = prev

    def recursive_reversal(self,node):
        current = node
        if not current and not current.next:
            return current
        next_cur = self.recursive_reversal(current.next)
        current.next.next = current
        current.next = None
        return next_cur
