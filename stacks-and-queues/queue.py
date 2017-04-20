

class Queue(object):

    def __init__(self):
        self.queue = list()

    def __repr__(self):
        string = "queue"
        for element in self.queue:
            string += "->"
            string += str(element)
        return string

    def __len__(self):
        return len(self.queue)

    def enqueue(self, data):
        self.queue.insert(0, data)
        print self


    def dequeue(self):
        element = self.queue[-1]
        del self.queue[-1]
        print self
        return element

q = Queue()
print q
q.enqueue(5)
q.enqueue(6)
q.enqueue(8)
q.enqueue(100)

q.dequeue()
q.dequeue()
