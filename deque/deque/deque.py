import fileinput
#Deque - data structure, where you can add and delete elements at left and right
class Deque:
    #initialization
    def __init__(self):
        self.size: int = 0
        self.capacity: int = 0
        self.first: int = 0
    #setting size
    def set_size(self, input_size: str):
        if input_size.is_digit():
            self.capacity=int(input_size) 
            self.array = [None] * int(input_size)
        else:
            print('error')
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
    for line in fileinput.input():
        line = line.replace('\n', '')

        if line == '':
            continue

        elif deque.capacity == 0:
            params: list = line.split(' ')
            if params[0] == 'set_size' and len(params) == 2:
                deque.set_size(params[1])
            else:
                print('error')

        # без сайза
        elif deque.capacity != 0:
            params = line.split(' ')
            if len(params) > 2:
                print('error')
            elif len(params) == 2:
                if params[0] == 'pushf':
                    deque.pushf(params[1])
                elif params[0] == 'pushb':
                    deque.pushb(params[1])
                else:
                    print('error')
            elif line == 'popf':
                print(deque.popf())
            elif line == 'popb':
                print(deque.popb())

            elif line == 'print':
                deque.print()
            else:
                print('error')
        else:
            print('error')
