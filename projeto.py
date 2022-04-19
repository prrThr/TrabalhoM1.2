import random

# ===== Escolhe uma das 3 dificuldades (apenas matrizes quadradas) ===== #
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

# ===== Gera campo aleatório a partir da dificuldade escolhida. ===== #
def gerarCampo(t):
    matriz = []
    for l in range(t):
        linha = []
        for c in range(t):
            num = random.randint(-1, 0)
            linha.append(num)
        matriz.append(linha)
    return matriz

# ===== Mostra a matriz (usando apenas para construir o programa) ===== #
def mostrarMatriz(t,m):
    for i in range(t):
        for j in range(t):
            print(f'{m[i][j]:^3}', ' ', end='')
        print('')       

# ===== Matriz padrão apenas com '-'
def default(t):
    padrao = []
    for l in range(t):
        linha = []
        for c in range(t):
            linha.append('-')
        padrao.append(linha) 
    return padrao

#def QntdBombas():
    



def main():
    tamanho = dificuldade()
    matriz = gerarCampo(tamanho)
    padrao = default(tamanho)
    mostrarMatriz(tamanho, matriz)
    print ('')
    mostrarMatriz(tamanho,padrao)
        
        



#===================PROGRAMA PRINCIPAL===================#

main()
