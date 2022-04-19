import random

#// ----------------------------------------------------------------//
#      Escolhe uma das 3 dificuldades (apenas matrizes quadradas) 
#// ----------------------------------------------------------------//
def dificuldade():
    print('=====================================')
    print('ESCOLHA A DIFICULDADE: ')
    print('1 - Facil')
    print('2 - Medio')
    print('3 - Dificil')
    existe = False 
    while existe == False:
        escolhaDificuldade = int(input())
        if escolhaDificuldade != 1 and escolhaDificuldade != 2 and escolhaDificuldade != 3:
            existe = False
            print('Digite um valor dentro do intervalo 1-3')
        else:   
            existe = True

    if escolhaDificuldade == 1:
        return 4
    elif escolhaDificuldade == 2:
        return 5
    else:
        return 15

#// ----------------------------------------------------------------//
#       Contagem de bombas restantes para o fim do jogo         
#// ----------------------------------------------------------------//
def bombasRestantes(t, m):
    cont = 0
    for l in range(t):
        for c in range(t):
            if m[l][c] == -1:
                cont = cont + 1
    return cont

#// ----------------------------------------------------------------//
#       Gera campo aleatório a partir da dificuldade escolhida.         
#// ----------------------------------------------------------------//
def gerarCampo(t):
    inicial = []
    for l in range(t):
        linha = []
        for c in range(t):
            num = random.randint(-1, 0)
            linha.append(num)
        inicial.append(linha)
    return inicial

#// ----------------------------------------------------------------//
#      Mostra a matriz (usando apenas para construir o programa) 
#// ----------------------------------------------------------------//
def mostrarMatriz(t,m):
    for i in range(t):
        for j in range(t):
            print(' '*4,f'{m[i][j]:^3}', ' ', end='')
        print('')       

#// ----------------------------------------------------------------//
#                 Matriz padrão apenas com '-'
#// ----------------------------------------------------------------//
def default(t):
    campoVazio = []
    for l in range(t):
        linha = []
        for c in range(t):
            linha.append('#')
        campoVazio.append(linha) 
    return campoVazio
#// ----------------------------------------------------------------//
#  Computa a quantidade de bombas no jogo atual (NÃO ENTENDI O QUE ACONTECEU AQUI)
#// ----------------------------------------------------------------//
def computaBombas(m):
    matrizM = []
    for linha in range(len(m)):
        matrizM.append([])
        for coluna in range(len(m[linha])):
            if m[linha][coluna] == -1:
                matrizM[linha].append(-1)
                continue
            matrizM[linha].append(contaQtdMenosUm(m, linha, coluna))
    return matrizM  

def contaQtdMenosUm(m, i, j):
    cont = 0
    for linha in range(len(m)):
        for coluna in range(len(m[linha])):
            if linha == i and coluna == j:
                continue
            if m[linha][coluna] == -1:
                if linha == (i - 1) and (coluna == (j-1) or coluna == j or coluna == (j+1)):
                    cont = cont + 1
                elif linha == i and (coluna == j - 1 or coluna == j + 1):
                    cont = cont + 1
                elif linha == i + 1 and (coluna == j - 1 or coluna == j or coluna == j + 1):
                    cont = cont + 1
    return cont

#// ----------------------------------------------------------------//
#                           JOGO ATUAL 
#// ----------------------------------------------------------------//
def marcaPosicao(m, comp, l, c, t):
    m[l][c] = comp[l][c]
        
    if l > 0 and c > 0 and l < t and c < t: # Mostra as posições sem bomba caso linha/coluna > 0 e linha/coluna < tamanho
        if m[l][c] == 0 and comp[l-1][c] == 0 and comp[l-1][c-1] == 0 and comp[l-1][c+1] == 0 and comp[l][c-1] == 0 and comp[l][c+1] == 0 and comp[l+1][c] == 0 and comp[l+1][c-1] == 0 and comp[l+1][c+1] == 0:
           m[l-1][c] = comp[l-1][c]
           m[l-1][c-1] = comp[l-1][c-1]
           m[l-1][c+1] = comp[l-1][c+1]
           m[l][c-1] = comp[l][c-1]
           m[l][c+1] = comp[l][c+1]
           m[l+1][c] = comp[l+1][c]
           m[l+1][c-1] = comp[l+1][c-1]
           m[l+1][c+1] = comp[l+1][c+1]

    elif l == 0 and c > 0 and c < t:
        if m[l][c] == 0 and comp[l][c-1] == 0 and comp[l][c+1] == 0 and comp[l+1][c] == 0 and comp[l+1][c-1] == 0 and comp[l+1][c+1] == 0:
           m[l][c-1] = comp[l][c-1]
           m[l][c+1] = comp[l][c+1]
           m[l+1][c] = comp[l+1][c]
           m[l+1][c-1] = comp[l+1][c-1]
           m[l+1][c+1] = comp[l+1][c+1]

    elif l == t and c > 0 and c < t:
        if m[l][c] == 0 and comp[l-1][c] == 0 and comp[l-1][c-1] == 0 and comp[l-1][c+1] == 0 and comp[l][c-1] == 0 and comp[l][c+1] == 0:
           m[l-1][c] = comp[l-1][c]
           m[l-1][c-1] = comp[l-1][c-1]
           m[l-1][c+1] = comp[l-1][c+1]
           m[l][c-1] = comp[l][c-1]
           m[l][c+1] = comp[l][c+1]

    elif l == 0 and c == 0:
        if m[l][c] == 0 and comp[l][c+1] == 0 and comp[l+1][c] == 0 and comp[l+1][c+1] == 0:
           m[l][c+1] = comp[l][c+1]
           m[l+1][c] = comp[l+1][c]
           m[l+1][c+1] = comp[l+1][c+1]

    elif l == 0 and c == t:
        if m[l][c] == 0 and comp[l][c-1] == 0 and comp[l+1][c] == 0 and comp[l+1][c-1] == 0:
           m[l][c-1] = comp[l][c-1]
           m[l+1][c] = comp[l+1][c]
           m[l+1][c-1] = comp[l+1][c-1]

    elif l == t and c == t:
        if m[l][c] == 0 and comp[l-1][c] == 0 and comp[l-1][c-1] == 0 and comp[l][c-1] == 0:
           m[l-1][c] = comp[l-1][c]
           m[l-1][c-1] = comp[l-1][c-1]
           m[l][c-1] = comp[l][c-1]

    elif l == t and c == 0:
        if m[l][c] == 0 and comp[l-1][c] == 0 and comp[l-1][c+1] == 0 and comp[l][c+1] == 0:
           m[l-1][c] = comp[l-1][c]
           m[l-1][c+1] = comp[l-1][c+1]
           m[l][c+1] = comp[l][c+1]

    
    elif l > 0 and l < t and c == 0:
        if m[l][c] == 0 and comp[l-1][c] == 0 and comp[l-1][c+1] == 0 and comp[l][c+1] == 0 and comp[l+1][c] == 0 and comp[l+1][c+1] == 0:
           m[l-1][c] = comp[l-1][c]
           m[l-1][c+1] = comp[l-1][c+1]
           m[l][c+1] = comp[l][c+1]
           m[l+1][c] = comp[l+1][c]
           m[l+1][c+1] = comp[l+1][c+1]

    elif l > 0 and l < t and c == t:
        if m[l][c] == 0 and comp[l-1][c] == 0 and comp[l-1][c-1] == 0 and comp[l][c-1] == 0 and comp[l+1][c] == 0 and comp[l+1][c-1] == 0:
           m[l-1][c] = comp[l-1][c]
           m[l-1][c-1] = comp[l-1][c-1]
           m[l][c-1] = comp[l][c-1]
           m[l+1][c] = comp[l+1][c]
           m[l+1][c-1] = comp[l+1][c-1]

    return m
    
#// ----------------------------------------------------------------//
#                              MAIN 
#// ----------------------------------------------------------------//
def main():
    tamanho = dificuldade()                # Tamanho do campo
    matriz = gerarCampo(tamanho)           # Primeiro campo gerado, utilizado para elaboração das outras matrizes
    contBombas = bombasRestantes(tamanho, matriz)  # Computa o total de bombas no campo gerado
    campoVazio = default(tamanho)          # Campo vazio inicial preenchido "#" que será alterado futuramente
    campoAtual = campoVazio                # Campo que será modificado pelo usuário
    campoComputado = computaBombas(matriz) # Campo com as posições e números computados
    fimDeJogo = False
    posicoesParaDescobrir = tamanho * tamanho - contBombas
    mostrarMatriz(tamanho,matriz) # DELETAR DEPOIS
    print(' ')
    mostrarMatriz(tamanho, campoComputado)  
    while not fimDeJogo:
        linha = int(input("Digite a linha que deseja marcar: ")) -1
        coluna = int(input("Digite a coluna que deseja marcar: ")) -1
        campoAtual = marcaPosicao(campoAtual, campoComputado, linha, coluna, tamanho)
        if campoAtual[linha][coluna] == -1:
            fimDeJogo = True
            print('Clicou na bomba! Voce perdeu!')
        else:
            posicoesParaDescobrir = posicoesParaDescobrir - 1
            if posicoesParaDescobrir == 0:
                fimDeJogo = True
                print('Descobriu totas as bombas! Voce venceu!')
        mostrarMatriz(tamanho, campoAtual)
                

#// ----------------------------------------------------------------//
#                      PROGRAMA PRINCIPAL
#// ----------------------------------------------------------------//
main()
