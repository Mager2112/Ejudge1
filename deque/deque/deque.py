#Deque - data structure, where you can add and delete elements at left and right
class Deque:
    #initialization
    def __init__(self):
        self.items = []
    #check for emptiness
    def is_empty(self):
        return self.items == []
    #add in left
    def pushf(self, item):
        self.items.insert(0, item)
    #add in right
    def pushb(self, item):
        self.items.append(item)
    #delete in left
    def popf(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "Deque is empty"
    #delete in right
    def popb(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Deque is empty"
    def size(self):
        return len(self.items)
if __name__ == '__main__':
    deque = Deque()
    deque.pushf(1)
    deque.pushb(2)
    deque.pushf(3)
    print(deque.items) # 3 1 2
