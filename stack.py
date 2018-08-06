class Stack:

    stack = []
    def __init__(self, name):
        self.name = name

    def add(self, dataval):
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False

    def peek(self):
        return self.stack[3]

AStack = Stack("Ravi")
AStack.add("Mon")
AStack.add("Tue")
AStack.add("Wed")
AStack.add("Thu")
AStack.peek()
print(AStack.peek())
print(AStack.peek())

































