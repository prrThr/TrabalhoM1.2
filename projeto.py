import numpy as np
import random

m = []

for i in range(5):
    linha = []
    for j in range(5):
        num = random.randint(0, 9)
        linha.append(num)
    m.append(linha)

for i in range(5):
    for j in range(5):
        print(f'[{m[i][j]}]', end=' ')
    print()
