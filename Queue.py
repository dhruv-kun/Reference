"""
This contains different queue implementations i did or learned
Do not copy and paste this. This may not be accurate.

1. ArrayQueue
"""


class ArrayQueue:
    def __init__(self, iterable=None):
        self.q = []
        if iterable:
            self.q = list(iterable)
        self.tail = len(self.q)
        self.head = -1

    def put(self, val):
        self.q.append(val)
        self.tail += 1

    def get(self):
        self.head += 1
        try:
            return self.q[self.head]
        except IndexError:
            print('Getting element from empty queue')
            return

    def empty(self):
        return self.head + 1 == self.tail

    def __str__(self):
        return ' -> '.join([str(i) for i in self.q])


