class Node:
    def __init__(self, chamado):
        self.chamado = chamado
        self.next = None


class ListaChamados:
    def __init__(self):
        self.head = None

    def inserir_fim(self, chamado):
        novo = Node(chamado)

        if self.head is None:
            self.head = novo
            return

        atual = self.head

        while atual.next is not None:
            atual = atual.next

        atual.next = novo

    def exibir(self):
        atual = self.head

        while atual is not None:
            print(atual.chamado, end=" -> ")
            atual = atual.next

        print("None")

    def buscar(self, chamado):
        atual = self.head
        posicao = 0

        while atual is not None:
            if atual.chamado == chamado:
                return posicao

            atual = atual.next
            posicao += 1

        return -1