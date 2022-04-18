import random

def campoAleatorio(tamanho):
    for l in range(tamanho):
        linha = []
        for c in range(tamanho):
            num = random.randint(-1, 0)
            linha.append(num)
        matriz.append(linha)

def mostrarMatriz(tamanho):
    for i in range(tamanho):
        for j in range(tamanho):
            print(f'{matriz[i][j]:^3}', ' ', end='')
        print('')       

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
        else:   
            existe = True

    if escolhaDificuldade == 1:
        return 4
    elif escolhaDificuldade == 2:
        return 5
    else:
        return 15



def main():
    tamanho = dificuldade()
    campoAleatorio(tamanho)
    mostrarMatriz(tamanho)

#===================PROGRAMA PRINCIPAL===================#
tamanho = []
coluna = []
matriz = []
main()
