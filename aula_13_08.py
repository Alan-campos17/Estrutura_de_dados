class Node:
    def __init__(self, data) :
        self.data = data 
        self.next = None

    def __repr__(self):
        return f"Node list({self.data!r})"

class linkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        novo = Node(data)
        if self.head is None:
            self.head = novo
            return
        atual = self.head
        while atual.next is not None:
            atual = atual.next
        atual.next = novo

    def __iter__(self):
        atual = self.head
        while atual is not None:
            yield atual.data
            atual= atual.next

lista = linkedList()
lista.append('ab')
lista.append('ac')
lista.append('ad')

for item in lista:
    print(item)

