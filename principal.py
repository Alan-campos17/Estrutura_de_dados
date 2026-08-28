from chamados import ListaChamados

def main():
    lista = ListaChamados()

    # Leitura dos chamados via input()
    while True:
        entrada = input().strip()
        if entrada.lower() == 'fim':
            break
        if entrada:  # Garante que não vai inserir linhas vazias
            lista.inserir_fim(entrada)

    # Exibe a lista completa de chamados
    lista.exibir()

    # Solicita o chamado para buscar
    termo_busca = input().strip()
    
    # Executa a busca e formata a saída
    posicao = lista.buscar(termo_busca)
    if posicao != -1:
        print(f"Chamado '{termo_busca}' encontrado na posicao {posicao}.")
    else:
        print(f"Chamado '{termo_busca}' nao encontrado.")

if __name__ == "__main__":
    main()
