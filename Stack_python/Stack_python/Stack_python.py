# Stack - data type that can do two commands Pop() and Push() 
# Push(item) - creating last element 
# Pop() - deleting last element 
class Stack:
    # Initialization
    def __init__(self):
        self.items=[]
    # CHeck for null
    def isEmpty(self):
        return len(self.items) == 0
    # Creating last object
    def push(self, item):
        self.items.append(item)
    # Delete last object
    def pop(self):
        if not self.isEmpty():
            self.items.pop()
        else:
            print('ЕГГОГ')
    # Size of stack
    def size(self):
        return len(self.items)
# Main
st = Stack()
st.push(1)
st.push(2)
st.push(3)
print('What do you want to do? 1:pop 2:push')
what = int(input())
if what == 1:
    st.pop()
if what == 2:
    a=int(input())
    st.push(a)
print(st.items)
print(f'Size: {st.size()}')
