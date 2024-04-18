class Node:
    def __init__(self, val) -> None:
        self.val = val 
        self.next = None


class LinkedList:

    def __init__(self, node):
        self.node =  node 
        self.current_node = self.node
        self.result_list = [] 

    def traverseList(self):
        while self.current_node:
            self.result_list.append(self.current_node.val)
            self.current_node = self.current_node.next
        return self.result_list
        
        
    def insertElementAtEnd(self, node):
        pass


a = Node(2)
b = Node(4)
c = Node(10)
d = Node(6)
e = Node(7)
a.next = b
b.next = c
c.next = d
d.next = e

window_traverser = LinkedList(a)
print(window_traverser.traverseList())
# window_traverser.insertElementAtEnd(Node(4))
# window_traverser.insertElementAtEnd(Node(6))
# window_traverser.insertElementAtEnd(Node(0))

# print(window_traverser.traverseList())