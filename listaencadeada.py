class linkedList:
    def __init__(self):
        self.head = None

    def inserir_inicio(self, data):
        novo = Node(data)
        novo.next = self.head
        self.head = novo

    def inserir_fim(self, data):
        novo = Node(data)
        if self.head is not None:
            self.head = novo
            return

        atual = self.head
        while atual.next is not None:
            atual = atual.next
        atual.next = novo