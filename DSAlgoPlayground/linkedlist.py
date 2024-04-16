
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

print(find_maximum(node))


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
