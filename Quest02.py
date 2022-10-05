#Declaração de Variáveis
salCarlos: float
salJoao: float
meses: int

#Entrada de Dados
salCarlos = int(input("Digite o salário de Carlos: "))
salJoao = int(input("Digite o salário de João: "))

#Processamento de Dadoss
salJoao = salCarlos / 3
meses = 0
while salJoao < salCarlos:
    salCarlos = salCarlos + (salCarlos * 2 / 100)
    salJoao = salJoao + (salJoao * 5 / 100)
    meses = meses + 1

#Saída de Dados
print(f"Serão necssários {meses} meses para João ultrapassar Carlos")