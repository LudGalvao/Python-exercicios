jogador1 = {
    "nomeUsuario":"",
    "partidasGanhas":0,
}
jogador2 = {
    "nomeUsuario":"",
    "partidasGanhas":0,
}
matrizJogo = [
    [11,12,13],
    [21,22,23],
    [31,32,33]
]
def defineNomeJogador():
    nomeUsuario1 = str(input("Insira o nome do Jogador 1 [x]: "))
    jogador1["nomeUsuario"] = nomeUsuario1
    nomeUsuario2 = str(input("Insira o nome do Jogador 2 [o]: "))
    jogador2["nomeUsuario"] = nomeUsuario2
    jogo()
def jogo():
    num = 11
    while True:
        for i in range(0,9):
            for q in range(0,len(matrizJogo)):
                print(matrizJogo[q])
            if(i%2 == 0):
                print(f"Vez do(a) {jogador1['nomeUsuario']} [x]")
                escolhaJogadorUm = int(input("Insira a posição de sua escolha: "))
                insereEscolha(escolhaJogadorUm,1)
                if(verificaResultado("x") == 3):
                    for k in range(0,len(matrizJogo)):
                        print(matrizJogo[k])
                    print(f"{jogador1['nomeUsuario']} ganhou o jogo!")
                    jogador1["partidasGanhas"] = jogador1["partidasGanhas"] + 1
                    break
            else:
                print(f"Vez do {jogador2['nomeUsuario']} [o]")
                escolhaJogadorDois = int(input("Insira o posição de sua escolha: "))
                insereEscolha(escolhaJogadorDois,2)
                if(verificaResultado("o") == 3):
                    for k in range(0,len(matrizJogo)):
                        print(matrizJogo[k])
                    print(f"O {jogador2['nomeUsuario']} ganhou o jogo!")
                    jogador2["partidasGanhas"] = jogador2["partidasGanhas"] + 1
                    break
            if(i == 8):
                print("Fim de Jogo! \nEmpate!")
        continua = str(input("Digite 's' para continuar no programa \nou 'n' para sair do programa: "))
        if(continua == "n"):
            print(f"O programa será desligado... \nO jogo terminou com o jogador {jogador1['nomeUsuario']} com {jogador1['partidasGanhas']} pontos, \ne jogador {jogador2['nomeUsuario']} terminou com {jogador2['partidasGanhas']} pontos.")
            break
        for a in range(len(matrizJogo)):
            for b in range(len(matrizJogo)):
                matrizJogo[a][b] = num
                num = num + 1
            num = 21 + (a*10)
def insereEscolha(caminhoEscolha,jogador):
    if(jogador == 1):
        tratamentoEscolha = str(caminhoEscolha)
        for i in range(0,len(tratamentoEscolha)):
            if(matrizJogo[int(tratamentoEscolha[0])-1][int(tratamentoEscolha[1])-1] != "x" and matrizJogo[int(tratamentoEscolha[0])-1][int(tratamentoEscolha[1])-1] != "o"):
                matrizJogo[int(tratamentoEscolha[0])-1][int(tratamentoEscolha[1])-1] = "x"
                break
            else:
                print("Escolha inválida, jogador 1 perdeu a vez!")
                break
    if(jogador == 2):
        tratamentoEscolha = str(caminhoEscolha)
        for i in range(0,len(tratamentoEscolha)):
            if(matrizJogo[int(tratamentoEscolha[0])-1][int(tratamentoEscolha[1])-1] != "x" and matrizJogo[int(tratamentoEscolha[0])-1][int(tratamentoEscolha[1])-1] != "o"):
                matrizJogo[int(tratamentoEscolha[0])-1][int(tratamentoEscolha[1])-1] = "o"
                break
            else:
                print("Escolha inválida, jogador 2 perdeu a vez!")
                break
def verificaResultado(symbolPlayer):
    pontoDiagonal = 0
    pontoDiagonalSecundaria = 0
    pontoLinhas0 = 0
    pontoLinhas1 = 0
    pontoLinhas2 = 0
    pontosColuna0 = 0
    pontosColuna1 = 0
    pontosColuna2 = 0
    for x in range(0,3):
        for y in range(0,3):
            # diagonais
            if(x==y and matrizJogo[x][y] == symbolPlayer):
                pontoDiagonal += 1
            if((x == 0 and y == 2) or (x == 1 and y == 1) or (x == 2 and y == 0)):
                if(matrizJogo[x][y] == symbolPlayer):
                    pontoDiagonalSecundaria += 1
            # linhas
            if(x == 0):
                if(matrizJogo[x][y] == symbolPlayer):
                    pontoLinhas0 += 1
                    if(y == 2 and pontoLinhas0 != 3):
                        pontoLinhas0 = 0
            if(x == 1):
                if(matrizJogo[x][y] == symbolPlayer):
                    pontoLinhas1 += 1
                    if(y == 2 and pontoLinhas1 != 3):
                        pontoLinhas1 = 0
            if(x == 2):
                if(matrizJogo[x][y] == symbolPlayer):
                    pontoLinhas2 += 1
                    if(y == 2 and pontoLinhas2 != 3):
                        pontoLinhas2 = 0
            #colunas
            if(y == 0):
                if(matrizJogo[x][y] == symbolPlayer):
                    pontosColuna0 += 1
                    if(x == 2 and pontosColuna0 != 3):
                        pontosColuna0 = 0
            if(y == 1):
                if(matrizJogo[x][y] == symbolPlayer):
                    pontosColuna1 += 1
                    if(x == 2 and pontosColuna1 != 3):
                        pontosColuna1 = 0
            if(y == 2):
                if(matrizJogo[x][y] == symbolPlayer):
                    pontosColuna2 += 1
                    if(x == 2 and pontosColuna2 != 3):
                        pontosColuna2 = 0
            if(pontoDiagonal == 3):
                return 3
            if(pontoDiagonalSecundaria == 3):
                return 3
            if(pontoLinhas0 == 3):
                return 3
            if(pontoLinhas1 == 3):
                return 3
            if(pontoLinhas2 == 3):
                return 3
            if(pontosColuna0 == 3):
                return 3
            if(pontosColuna1 == 3):
                return 3
            if(pontosColuna2 == 3):
                return 3

defineNomeJogador()