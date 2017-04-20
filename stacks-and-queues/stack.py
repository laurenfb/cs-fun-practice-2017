#  let's make a stack

class Stack(object):

    def __init__(self):
        self.stack = list()
    
    def __repr__(self):
        i = len(self.stack) - 1
        string = "stack"
        while i >= 0:
            string += "\n----\n"
            string += str(self.stack[i])
            i -= 1
        return string

    def __len__(self):
        return len(self.stack)

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        item = self.stack[-1]
        del self.stack[-1]
        return item


def put_a_string_in_a_stack_and_reverse_it(string):
    stack = Stack()
    for letter in string:
        stack.push(letter)
    new_string = ""
    while len(stack) is not 0:
        new_string += stack.pop()
    return new_string

string = "my name is a cat and your name is a dog"
print string
print put_a_string_in_a_stack_and_reverse_it(string)


stack_friend = Stack()
stack_friend.push(5)
stack_friend.push(100)
stack_friend.push(3985)
stack_friend.push(2393)
stack_friend.push(3)
print stack_friend

stack_friend.pop()

print stack_friend
