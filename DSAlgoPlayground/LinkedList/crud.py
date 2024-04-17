class Node:
    def __init__(self, val) -> None:
        self.val = val 
        self.next = None


class LinkedList:
    def _init_(self, node):
        pass

    def traverseList(self):
        pass

    def insertElementAtEnd(self, node):
        pass


a = Node(2)

window_traverser = LinkedList(a)
window_traverser.insertElementAtEnd(Node(4))
window_traverser.insertElementAtEnd(Node(6))
window_traverser.insertElementAtEnd(Node(0))

print(window_traverser.traverseList())