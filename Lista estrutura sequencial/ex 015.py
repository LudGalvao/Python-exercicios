sal_hora = float(input('Quantos você ganha por hora: '))
hora = int(input('Quantas hora você trabalha por dia: '))

salario_bruto = (sal_hora * hora) * 22
ir = (salario_bruto * 11) / 100
inss = (salario_bruto * 8) / 100
sind = (salario_bruto * 5) / 100
salario_liqui = salario_bruto - ir - inss - sind

print(f'Seu sálario bruto é R$ {salario_bruto:.2f}')
print(f'Você precisa pagar ao imposto de renda R$ {ir:.2f}')
print(f'Você precisa pagar ao Inss R$ {inss:.2f}')
print(f'Você precisa pagar ao sindicato R$ {sind:.2f}')
print(f'Seu sálario liquido é R$ {salario_liqui:.2f}')
