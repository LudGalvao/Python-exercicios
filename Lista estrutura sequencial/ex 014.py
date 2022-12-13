peixe = float(input('Informe quantos kg de peixe você pegou: '))
multa = (peixe - 50) * 4.00
excesso = peixe - 50

if peixe < 50:
    print('Você pegou menos de 50kg e não tem multa a pagar')
else:
    print(f'Você passou do excesso de peixe e pegou {excesso}kg a mais')
    print(f'O valor da sua multa foi R$ {multa:.2f}')