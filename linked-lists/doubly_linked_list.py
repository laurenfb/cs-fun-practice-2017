from singly_linked_list import Node, LinkedList

class DoubleNode(Node):
    def __init__(self, data, next_node=None, previous_node=None):
        Node.__init__(self)
        self.previous_node = previous_node


class DoublyLinkedList(LinkedList):
    def __init__(self, data):
        LinkedList.__init__(self, data)

    def __repr__(self):
        current = self.head
        print "printing list"
        printed = ""
        while current is not None:
            printed += str(current.data)
            printed += "<->"
            current = current.next_node
        printed += "None"
        return printed

    def add(self, data):
        current = self.head
        while current.next_node is not None:
            current = current.next_node
        new_node = Node(data)
        current.next_node = new_node
        new_node.previous = current
        print "added %s to linked list" % str(data)
        print self

def test():
    cat = DoublyLinkedList(5)
    print cat
    cat.add(10)
