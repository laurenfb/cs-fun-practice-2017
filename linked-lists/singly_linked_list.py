# linked list whattup

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

    def remove(self, data):
        current = self.head
        previous = None
        while current is not None:
            if current.data != data:
                previous = current
                current = current.next_node
            else:
                previous.next_node = current.next_node
                current = None
                print "removed %s from linked list" % str(data)
        print self

def test():
    cat = LinkedList(1)
    print cat
    cat.add(12)
    cat.add(25)
    cat.add(12)
    cat.add(1)
    return cat


def reverse_not_in_place(linked_list):
    current_old = linked_list.head
    new_list = LinkedList(current_old.data)
    while current_old.next_node is not None:
        current_old = current_old.next_node
        current_new = new_list.head
        new_list.head = Node(current_old.data)
        new_list.head.next_node = current_new
    return linked_list, new_list


def palindrome_check(old):
    old, new_list = reverse_not_in_place(old)
    current_old = old.head
    current_new = new_list.head
    while current_old is not None and current_new is not None:
        if current_old.data != current_new.data:
            return False
        current_old =  current_old.next_node
        current_new = current_new.next_node
    return True

cat = test()
yo, second_cat = reverse_not_in_place(cat)

print palindrome_check(cat)
