from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz quadrada de {} é {:.2f}'.format(num, floor(raiz)))
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))
