mat = [[0,0,0], [0,0,0],[0,0,0]]
s = 0
for lin in range(0,3):
    for col in range(0,3):
        mat[lin][col] = int (input('Informe um valor para a posição [%d][%d]: ' %(lin+1, col+1)))
for lin in range(0,3):
        for col in range(0,3):
            s += mat[lin][col]
print(s)