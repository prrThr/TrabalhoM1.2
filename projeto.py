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
def marcaPosicao(m, comp, l, c):
    m[l][c] = comp[l][c]
    return m

#// ----------------------------------------------------------------//
#                              MAIN 
#// ----------------------------------------------------------------//
def main():
    tamanho = dificuldade()
    matriz = gerarCampo(tamanho)
    campoVazio = default(tamanho)
    campoAtual = campoVazio
    campoComputado = computaBombas(matriz)
    fimDeJogo = False
    mostrarMatriz(tamanho,matriz)
    print(' ')
    mostrarMatriz(tamanho, campoAtual)  
    while not fimDeJogo:
        linha = int(input("Digite a linha que deseja marcar: ")) -1
        coluna = int(input("Digite a coluna que deseja marcar: ")) -1
        campoAtual = marcaPosicao(campoAtual, campoComputado, linha, coluna)
        if campoAtual[linha][coluna] == -1:
            fimDeJogo = True
            print('Clicou na bomba! Voce perdeu!')
        mostrarMatriz(tamanho, campoAtual)



    
        
        


#// ----------------------------------------------------------------//
#                      PROGRAMA PRINCIPAL
#// ----------------------------------------------------------------//
main()
