#Deque - data structure, where you can add and delete elements at left and right
class Deque:
    #initialization
    def __init__(self):
        self.items = []
    #check for emptiness
    def is_empty(self):
        return self.items == []
    #add in left
    def append_left(self, item):
        self.items.insert(0, item)
    #add in right
    def append_right(self, item):
        self.items.append(item)
    #delete in left
    def pop_left(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "Deque is empty"
    #delete in right
    def pop_right(self):
        if not self.is_empty():
            return self.items.pop()
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
