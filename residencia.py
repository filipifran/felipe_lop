# Programa para calcular conta de água - residência social

consumo = float(input("Digite o consumo de água (m3): "))

# Verifica as faixas de consumo
if consumo <= 10:
    valor = 7.59
elif consumo <= 20:
    valor = consumo * 1.31
elif consumo <= 30:
    valor = consumo * 4.64
elif consumo <= 50:
    valor = consumo * 6.62
else:
    valor = consumo * 7.31

print(f"Valor da conta: R$ {valor:.2f}")