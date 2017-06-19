class ResizingArrayStack:
    """
    This is a stack implementation using resizing array.
    Stack will expand to it's double when full.
    And it will shrink to 1/2 it's size when it's 1/4th full.

    """

    def __init__(self, iterable=None):
        self.s = []
        if iterable:
            self.s = list(iterable)
        self.top = len(self.s)
        self.size = len(self.s)

    def pop(self):
        try:
            val = self.s[self.top - 1]
            self.top -= 1
            if self.size / 4 > self.top:
                self._shrink()
            return val
        except IndexError:
            print('Stack underflow.')
            return

    def push(self, val):
        if self.full():
            self._expand()
        self.top += 1
        self.s[self.top - 1] = val

    def top(self):
        try:
            return self.s[self.top]
        except IndexError:
            print('Stack underflow')

    def empty(self):
        return self.top == 0

    def full(self):
        return self.top == self.size

    def _expand(self):
        newsize = self.size * 2 + 1
        tmp = [0] * newsize
        for i in range(self.size):
            tmp[i] = self.s[i]
        self.s = tmp
        self.size = newsize

    def _shrink(self):
        newsize = self.size // 2
        tmp = [0] * newsize
        for i in range(newsize):
            tmp[i] = self.s[i]
        self.s = tmp
        self.size = newsize

    def __str__(self):
        string = ' -> '.join([str(self.s[i]) for i in range(self.top)])
        string += ' (top)'
        return string


if __name__ == '__main__':
    s = ResizingArrayStack()
    for i in range(16):
        s.push(i)
        print(s.size)

    for i in range(16):
        j = s.pop()
        print(s.size)
