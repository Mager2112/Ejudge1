# Стек (очередь) - структура данных, в которой можно либо добавлять в начало, либо удалять из начала, как в стопке тарелок
# Push(item) добавляет элемент в начало
# Pop() убирает элемент из начала
class Stack:
    # Инициализация объекта при создании
    def __init__(self):
        self.items=[]
    # Проверка на пустоту
    def isEmpty(self):
        return len(self.items) == 0
    # Запись в начало
    def push(self, item):
        self.items.append(item)
    # Удаление начала
    def pop(self):
        if not self.isEmpty():
            self.items.pop()
        else:
            print('ЕГГОГ')
    # Размер стека
    def size(self):
        return len(self.items)
# Main
st = Stack()
st.push(1)
st.push(2)
st.push(3)
print('Что хотите сделать? 1:pop 2:push')
what = int(input())
if what == 1:
    st.pop()
if what == 2:
    a=int(input())
    st.push(a)
print(st.items)
print(f'Размер: {st.size()}')




    