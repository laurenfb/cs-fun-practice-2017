# Stacks

elements added to "top" and can only be removed from the top
LIFO => last in first out

- two functions make it a Stack
  - push(element)
  - pop()

Limitations of using an array:
- with a native array, you must choose size ahead of time. perhaps you allocate too many or too few spaces
-

# Queues

elements added to back & can only be removed from the front
FIFO => first in first out

- two functions make it a Queue
  - enqueue(element)
  - dequeue()


# Abstraction
the programmer hides the implementation from the user. users don't see whether your stack is a native array or a linked list; they just use it.

Homework
1. Implement a Stack using an array to hold integer data
2. Implement a Stack using a linked list to hold integer
3. impl a queue using array
4. impl a queue using linkedlist
5. add these functions:
  - empty() --> returns bool
  - size() --> returns length
  - front() --> returns item that would be dequeued next
  - top() --> same for stack
  - min() --> min int val in data str
  - max() --> max int val in data str
