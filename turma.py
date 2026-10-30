class TabelaHash:

    def __init__(self):
        self.tamanho = 5
        self.tabela = []

        for i in range(self.tamanho):
            self.tabela.append([])

    def funcao_hash(self, matricula):
        return matricula % self.tamanho

    def inserir(self, matricula, nome):
        posicao = self.funcao_hash(matricula)

        self.tabela[posicao].append([matricula, nome])

    def buscar(self, matricula):
        posicao = self.funcao_hash(matricula)

        for aluno in self.tabela[posicao]:
            if aluno[0] == matricula:
                return aluno[1]

        return None
    def exibir(self):
        for i in range(self.tamanho):
            print(f"Posição {i}: {self.tabela[i]}")

tabela = TabelaHash()

tabela.inserir(103, "Ana")
tabela.inserir(208, "Bruno")
tabela.inserir(15, "Carla")
tabela.inserir(33, "Diego")
tabela.inserir(40, "Eva")

tabela.exibir()
            
