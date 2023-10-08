class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def append_left(self, item):
        self.items.insert(0, item)

    def append_right(self, item):
        self.items.append(item)

    def pop_left(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "Deque is empty"

    def pop_right(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Deque is empty"

    def peek_left(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return "Deque is empty"

    def peek_right(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Deque is empty"

    def size(self):
        return len(self.items)
if __name__ == '__main__':
    deque = Deque()
    deque.append_left(1)
    deque.append_right(2)
    deque.append_left(3)
    print(deque.items) # 3 1 2