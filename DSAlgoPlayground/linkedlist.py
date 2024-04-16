
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

