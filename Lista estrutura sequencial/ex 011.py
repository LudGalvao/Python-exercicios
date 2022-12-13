num_1 = int(input('Digite um número inteiro: '))
num_2 = int(input('Digite outro número inteiro: '))
num_3 = float(input('Digite um número real: '))

calc_1 = num_1 * 2 * (num_2 / 2)
calc_2 = (num_1 * 3) + num_3
calc_3 = num_3 ** 3

print(f'O produto do dobro do primeiro com metade do segundo: {int(calc_1)}')
print(f'A soma do triplo do primeiro com o terceiro: {calc_2}')
print(f'O terceiro elevado ao cubo: {calc_3}')