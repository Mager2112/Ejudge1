import fileinput
class Deque:
    #initialization
    def __init__(self):
        self.size: int = 0
        self.capacity: int = 0
        self.first: int = 0
    #setting size
    def set_size(self, input_size: str) -> None:
        if input_size.isdigit():
            self.capacity=int(input_size) 
            self.array = [None] * int(input_size)
        else:
            print('error')
    #push back        
    def pushb(self, value: str) -> None:
        if self.size == self.capacity:
            print('overflow')
        else:
            self.array[(self.first + self.size) % self.capacity] = value
            self.size += 1
    #push front       
    def pushf(self, value: str) -> None:
        if self.size == self.capacity:
            print('overflow')
        else:
            self.size += 1
            self.first -= 1
            self.array[(self.first) % self.capacity] = value
    #pop back        
    def popb(self) -> str:
        if self.size == 0:
            return ('underflow')
        else:
            result: str
            result, self.array[(self.first + self.size - 1) % self.capacity] = \
                self.array[(self.first + self.size - 1) % self.capacity], None

            self.size -= 1
            return result
    #pop front        
    def popf(self) -> str:
        if self.size == 0:
            return ('underflow')
        else:
            result: str
            result, self.array[self.first % self.capacity] = self.array[self.first % self.capacity], None
            self.first += 1
            self.size -= 1
            return result
            
    def print(self) -> None:
        if self.size == 0:
            print('empty')
            return
        for i in range(self.size):
            if i != self.size - 1:
                print(self.array[(self.first + i) % self.capacity], end=' ')
            else:
                print(self.array[(self.first + i) % self.capacity])

if __name__ == '__main__':
    deq = Deque()
    for line in fileinput.input():
        line = line.replace('\n', '')
        if line == '':
            continue
        elif deq.capacity == 0:
            params: list = line.split(' ')
            if params[0] == 'set_size' and len(params) == 2:
                deq.set_size(params[1])
            else:
                print('error')
        elif deq.capacity != 0:
            params = line.split(' ')
            if len(params) > 2:
                print('error')
            elif len(params) == 2:
                if params[0] == 'pushf':
                    deq.pushf(params[1])
                elif params[0] == 'pushb':
                    deq.pushb(params[1])
                else:
                    print('error')
            elif line == 'popf':
                print(deq.popf())
            elif line == 'popb':
                print(deq.popb())
            elif line == 'print':
                deq.print()
            else:
                print('error')
        else:
            print('error')
