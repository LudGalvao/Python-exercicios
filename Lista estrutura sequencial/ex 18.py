down = float(input('informe o tamanho do arquivo em mb: '))
vel = int(input('Informe a velocidade em mbps da sua internet: '))
calc = down / (vel / 8)
tempo = calc / 60

print(f'Para fazer o download de um aquivo {int(down)}mbs com velocidade de {vel}mbps, você vai levar {tempo:.1f}min')