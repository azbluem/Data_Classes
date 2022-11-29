from linkedlist import Node, LinkedList

l_list = LinkedList()
l_list.append(1)
l_list.append("A")
l_list.append(True)
l_list.print_nodes()
print(len(l_list))
print(l_list.recursive_len(l_list.head))
l_list.iterative_reversal()
l_list.print_nodes()
l_list.recursive_reversal(l_list.head)
l_list.print_nodes()