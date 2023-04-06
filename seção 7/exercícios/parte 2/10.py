"""
Leia uma matriz de 3x3 elementos. Calcule a soma dos elementos que estao na diagonal principal
"""
from random import randint

matriz = []
diagonal_princ = []

while len(matriz) < 3:
    linha = []
    while len(linha) <3:
        num = randint(1, 50)
        if num not in linha:
            linha.append(num)
    matriz.append(linha)
print('-' * 16)
print(f'{"matriz":^17}')
print('-' * 16)
for x, linha in enumerate(matriz):
    for y, num in enumerate(linha):
        if x == y:
            diagonal_princ.append(num)
            print(f'\033[32m{num:>4}\033[m', end=' ')
        else:
            print(f'{num:>4}', end=' ')
    print()
print('-' * 16)
print()
print(f'\033[32m>\033[m Soma da diagonal principal '
      f'\033[32m{diagonal_princ}\033[m = \033[32m{sum(diagonal_princ)}\033[m')
