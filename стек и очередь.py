class Stack():
    def __init__(self):
        self.stack=[]
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()
    def size(self):
        return len(self.stack)
a=Stack()
a.push('&')
print(a.size())
print(a.pop())
print(a.pop())
