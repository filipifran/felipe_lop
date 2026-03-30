# Calculadora simples

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Potência")
print("6 - Raiz quadrada (do primeiro número)")
print("7 - Número par")
print("8 - Número ímpar")

op = int(input("Escolha a operação: "))

if op == 1:
    print(num1 + num2)
elif op == 2:
    print(num1 - num2)
elif op == 3:
    print(num1 * num2)
elif op == 4:
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Erro: divisão por zero")
elif op == 5:
    print(num1 ** num2)
elif op == 6:
    print(num1 ** 0.5)
elif op == 7:
    print("Par" if num1 % 2 == 0 else "Não é par")
elif op == 8:
    print("Ímpar" if num1 % 2 != 0 else "Não é ímpar")
else:
    print("Opção inválida")