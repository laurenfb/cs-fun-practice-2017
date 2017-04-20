def reverse_not_in_place(linked_list):
    current_old = linked_list.head
    new_list = LinkedList(current_old.data)
    while current_old.next is not None:
        current_old = current_old.next
        current_new = new_list.head
        new_list.head = Node(current_old.data)
        new_list.head.next = current_new
    return linked_list, new_list


def palindrome_check(old):
    old, new_list = reverse_not_in_place(old)
    current_old = old.head
    current_new = new_list.head
    while current_old is not None: && current_new is not None:
        if current_old.data != current_new.data
            return False
        current_old =  current_old.next
        current_new = current_new.next
    return True
