# 3 - Operações Matemáticas Simples
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2
sub = num1 - num2
mult = num1 * num2
div = num1 / num2 if num2 != 0 else "Divisão por zero inválida"

print("Soma:", soma)
print("Subtração:", sub)
print("Multiplicação:", mult)
print("Divisão:", div)
