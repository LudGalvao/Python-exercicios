mat = [[0,0,0,0], [0,0,0,0],[0,0,0,0],[0,0,0,0]]
l1 =0
l2 = 0
l3 = 0
l4=0
d=0
for lin in range(0,4):
    for col in range(0,4):
        mat[lin][col] = int (input('Informe um valor para a posição [%d][%d]: ' %(lin+1, col+1)))
for lin in range(0,4):
    for col in range(0, 4):
        print(f'[{mat[lin][col]:^5}]',end=" ")
    print()
l1 += mat[0][0]
l2 += mat[1][1]
l3 += mat[2][2]
l4 += mat[3][3]
d = l1+l2+l3+l4
print("A soma da diagonal é: %.f"%(d))