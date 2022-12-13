m_2 = float(input('Informe o tamanho da Área que você deseja pintar: '))
litro = m_2 / 3
lata = int(litro / 18)

if litro % 18 != 0:
    lata += 1

print(f'Você vai precisar comprar {lata:.0f} latas de tintas')
print(f'Você vai pagar ao total de R${lata * 80:.2f}')