import math
#Declaração de Variáveis
num: int
quad: int
raiz: int
cubo: int
linha: int

#Entrada e Processamento de Dados
num = int(input('Digite um Número: '))
quad = num * num 
cubo = num * num * num 
linha = 1
raiz = math.sqrt(num)

while linha < 20:
    linha = linha + 1
    print(f" Número: {num} | Quadrado: {quad} | Cubo: {cubo} | Raíz: {raiz:.2f} ")




