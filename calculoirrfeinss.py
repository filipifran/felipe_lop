# Simulação simples de descontos

salario = float(input("Digite o salário: "))

# INSS (exemplo simplificado)
inss = salario * 0.08

# IRRF (exemplo simplificado)
if salario <= 1903.98:
    irrf = 0
elif salario <= 2826.65:
    irrf = salario * 0.075
else:
    irrf = salario * 0.15

print(f"INSS: R$ {inss:.2f}")
print(f"IRRF: R$ {irrf:.2f}")
print(f"Salário líquido: R$ {salario - inss - irrf:.2f}")