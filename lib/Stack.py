class Stack:
    def __init__(self, items=None, limit=100):
        if items is None:
            self.items = []
        else:
            self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            raise ValueError("Stack is full. Cannot push item.")

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            raise ValueError("Stack is empty. Cannot pop from an empty stack.")

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            raise ValueError("Stack is empty. No items to peek.")

    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) == self.limit

    def search(self, target):
        if target in self.items:
            return len(self.items) - self.items.index(target) - 1
        else:
            return -1
