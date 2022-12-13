sal_hora = float(input('Quantos você ganha por hora: '))
hora = int(input('Quantas hora você trabalha por dia: '))
dia = int(input('Informe quantos dias você trabalha no mês: '))
salario = (sal_hora * hora) * dia

print(f'O seu sálario total é {salario:.2f}')