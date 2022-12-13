sexo = input('Informe seu sexo(h ou m): ')
altura = float(input('Informe a sua altura: '))
homem_calc = (72.7 * altura) - 58
mulher_calc = (62.1 * altura) - 44.7

if sexo == 'M' or sexo == 'm' :
    print(f'Seu peso ideal é {mulher_calc:.2f}kg')
elif sexo == 'H' or sexo == 'h':
    print(f'Seu peso ideal é {homem_calc:.2f}kg')
else:
    print('Invalido')