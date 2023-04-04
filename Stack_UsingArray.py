class ArrayStack:
    def __init__(self, ar_size):
        self.arr = [None] * ar_size
        self.p = -1

    def push(self, elem):
        if self.p == len(self.arr):
            raise Exception("STACK OVERFLOW!")

        self.p += 1
        self.arr[self.p:] = [elem]

    def pop(self):
        if self.arr is None:
            raise Exception("STACK UNDERFLOW!")

        popped = self.arr[self.p]
        self.arr[self.p] = None
        self.p -= 1
        return popped

    def peek(self):
        print(self.arr[self.p])

    def is_empty(self):
        if self.arr[0] is None:
            print("Stack is empty")
        else:
            print('Stack is filled')

    def prints(self):
        for i in self.arr:
            print(i, end='-->')
        print()


expression = input()
a = ArrayStack(len(expression))
a.is_empty()
a.push(1)
a.push(2)
a.push(3)
a.push(4)
a.push(5)
a.peek()
a.prints()
a.pop()
# a.pop()
a.peek()
a.prints()
a.is_empty()
