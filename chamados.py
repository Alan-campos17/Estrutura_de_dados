class Node:
    def __init__(self, chamado):
        self.chamado = chamado
        self.next = None


class ListaChamados:
    def __init__(self):
        self.head = None

    def inserir_fim(self, chamado):
        novo_no = Node(chamado)
        
        # Caso a lista esteja vazia, o novo nó se torna o head
        if self.head is None:
            self.head = novo_no
            return
        
        # Caso contrário, percorre até o último nó
        atual = self.head
        while atual.next is not None:
            atual = atual.next
        
        # Liga o último nó ao novo nó
        atual.next = novo_no

    def exibir(self):
        atual = self.head
        elementos = []
        
        # Percorre a lista coletando os nomes dos chamados
        while atual is not None:
            elementos.append(str(atual.chamado))
            atual = atual.next
            
        # Adiciona o 'None' no final para representar o fim da lista
        elementos.append("None")
        print(" -> ".join(elementos))

    def buscar(self, chamado):
        atual = self.head
        posicao = 0
        
        # Percorre a lista comparando o chamado procurado
        while atual is not None:
            if atual.chamado == chamado:
                return posicao
            atual = atual.next
            posicao += 1
            
        return -1
