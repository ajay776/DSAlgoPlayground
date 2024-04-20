
class LinkedList:

    def __init__(self, value, nextNode=None) -> None:
        self.value = value
        self.nextNode = None


def countnodes(node):
    count = 1
    current_node = node
    while current_node.nextNode is not None:
        current_node = current_node.nextNode
        count += 1
    return count


def find_maximum(node):
    maxi = 0
    current_node = node
    while current_node.nextNode != None:
        if current_node.value > maxi:
            maxi = current_node.value
        current_node = current_node.nextNode
    else:
        if current_node.value > maxi:
            maxi = current_node.value
    return maxi


node = LinkedList(10)
node1 = LinkedList(4)
node2 = LinkedList(2)
node3 = LinkedList(11)
node.nextNode = node1
node1.nextNode = node2
node2.nextNode = node3
node3.nextNode = None

# print(find_maximum(node))


"""------------------------------------------------PRACTICE  SETS ----------------------------------------------------"""
"""
from typing import Optional
# Definition for singly-linked list.

l1 = [4, 7]
l2 = [2, 8, 9]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]):
    node = ListNode()
    current = node
    carry = 0
    while (l1 != None or l2 != None or carry != 0):
        import pdb
        pdb.set_trace()
        print(node)
        l1_val = l1.val if l1 else 0
        l2_val = l2.val if l2 else 0
        total = l1_val + l2_val + carry
        current.next = ListNode(total % 10)
        carry = total // 10
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        current = current.next
    return node.next


print(addTwoNumbers(l1, l2))

"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self, node):
        self.node = node

    def traverseList(self):
        return_array = []
        current_node = self.node
        while current_node:
            return_array.append(current_node.val)
            current_node = current_node.next
        return return_array

    def insertElementAtEnd(self, node):
        current_node = self.node
        while current_node.next:
            current_node = current_node.next if current_node.next else current_node
        else:
            current_node.next = node
        return self.traverseList()

    def insertElementAtStart(self, node):
        node.next = self.node
        self.node= node
        return self.traverseList()
    
    def insertAtPostion(self, node, position):
        if position == 0:
            return self.insertElementAtStart(node)
        else:
            index_count = 0
            current_node = self.node
            while index_count<position and current_node:
                if index_count +1 == position:
                    node.next = current_node.next if current_node.next else None    
                    current_node.next =  node
                current_node = current_node.next
                index_count +=1
            result = self.traverseList()
            if position> len(result):
                raise ValueError("index out of range")
        return result
                
    def deleteNodebyValue(self, value):
        current_node = self.node

        if current_node.val == value:
            self.node = current_node.next
            return self.traverseList()
        
        prev_node = None
        while current_node:
            if current_node.val == value and prev_node !=None:
                prev_node.next = current_node.next if current_node.next else None
                return self.traverseList()
            prev_node = current_node
            current_node = current_node.next

    def sortingChecker(self):
        current_node = self.node
        min_val = current_node.val
        while current_node:
            if min_val > current_node.next.val if current_node.next else None:
                return False
            current_node = current_node.next
        return True

    def removeDuplicates(self):
        pass

    def reverseLinkedList(self):
        current_node = self.node
        reverse_node = None
        prev_node = None
        
        while current_node:
            next_node = current_node.next if current_node.next else None
            reverse_node = current_node
            reverse_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.node = reverse_node
        return self.traverseList()
            



a = Node(2)
c = Node(4)
d = Node(3)
b = Node(5)
a.next = b
b.next = c
c.next = d
window_traverser = LinkedList(a)

# print(window_traverser.traverseList())

"""inserting node's at the end with printing it """
# print(window_traverser.insertElementAtEnd(Node(14)))
# print(window_traverser.insertElementAtEnd(Node(19)))
# print(window_traverser.insertElementAtEnd(Node(100)))



# window_traverser.insertElementAtStart(Node(6))
# window_traverser.insertElementAtStart(Node(7))
# print(window_traverser.insertElementAtStart(Node(8)))

# window_traverser.insertElementAtEnd(Node(0))
# print(window_traverser.insertAtPostion(node=Node(50), position=0))
# print(window_traverser.insertAtPostion(Node(10), 4))

# print(window_traverser.deleteNodebyValue(50))


print(window_traverser.sortingChecker())
# print(window_traverser.traverseList())
