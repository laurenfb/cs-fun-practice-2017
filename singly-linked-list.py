class Node(object):
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node
        print "initialized new node with data: " + str(data)

class LinkedList(object):
    def __init__(self, data):
        self.head = Node(data)

    def __repr__(self):
        current = self.head
        print "printing list"
        printed = ""
        while current is not None:
            printed += str(current.data)
            printed += "->"
            current = current.next_node
        printed += "None"
        return printed

    def add(self, data):
        # traverse to end of list
        current = self.head
        while current.next_node is not None:
            current = current.next_node
        current.next_node = Node(data)
        print "added %s to linked list" % str(data)
        print self


cat = LinkedList(1)
print cat
cat.add(12)
