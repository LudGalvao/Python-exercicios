mat = [[0,0,0], [0,0,0],[0,0,0]]
l1 =0
l2 = 0
l3 = 0
for lin in range(0,3):
    for col in range(0,3):
        mat[lin][col] = int (input('Informe um valor para a posição [%d][%d]: ' %(lin+1, col+1)))
for lin in range(0,3):
    for col in range(0, 3):
        print(f'[{mat[lin][col]:^5}]',end=" ")
    print()
for col in range(0,3):
    l1 += mat[0][col]
print("A soma da linha 1 é %.f "%(l1))
for col in range(0,3):
    l2 += mat[1][col]
print("A soma da linha 2 é %.f" % (l2))
for col in range(0,3):
    l3 += mat[2][col]
print("A soma da linha 3 é %.f " % (l3))
print("A matriz soma é: ")
print("[%.f] "%(l1))
print("[%.f]" % (l2))
print("[%.f] " % (l3))