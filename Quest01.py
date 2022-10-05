from datetime import datetime

#Declaração de Variáveis
salIni: float
anoIni: int
anoAt: int
aumento: float
novoSal: float

#Entrada de Dados
salIni = 1000
anoIni = 2005
anoAt = datetime.today().year
aumento = 1.5 * 1000
novoSal = 3 * 1000

#Processamento de Dados
while anoIni < anoAt:
    anoIni += 1
    salIni = 1 + aumento
    aumento = 2

#Saída de Dados
print(f"O salário em {anoAt} é de R$ {novoSal :.2f}")
    




