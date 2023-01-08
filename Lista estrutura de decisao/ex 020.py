num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

op = input("Qual operação você deseja realizar? (+, -, *, /) ")

if op == "+":
  resultado = num1 + num2
elif op == "-":
  resultado = num1 - num2
elif op == "*":
  resultado = num1 * num2
elif op == "/":
  resultado = num1 / num2
else:
  print("Operação inválida.")

if resultado % 2 == 0:
  par_ou_impar = "par"
else:
  par_ou_impar = "ímpar"

if resultado >= 0:
  positivo_ou_negativo = "positivo"
else:
  positivo_ou_negativo = "negativo"

if resultado % 1 == 0:
  inteiro_ou_decimal = "inteiro"
else:
  inteiro_ou_decimal = "decimal"


print(f"O resultado da operação é {resultado}. Este número é {par_ou_impar}, {positivo_ou_negativo} e {inteiro_ou_decimal}.")
