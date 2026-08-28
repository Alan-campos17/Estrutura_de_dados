from chamados import ListaChamados


lista = ListaChamados()

while True:
    chamado = input()

    if chamado == "fim":
        break

    lista.inserir_fim(chamado)

lista.exibir()

chamado_buscar = input()

posicao = lista.buscar(chamado_buscar)

if posicao != -1:
    print(f"Chamado '{chamado_buscar}' encontrado na posicao {posicao}.")
else:
    print(f"Chamado '{chamado_buscar}' nao encontrado.")