class Node():
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node
        print "initialized new node with data: " + str(data)

class LinkedList():
    def __init__(self, data):
        self.head = Node(data)

cat = LinkedList(1)
