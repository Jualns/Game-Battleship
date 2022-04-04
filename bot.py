from math import floor
from random import randint
#(i,j);(x,y);Tamanho do barco;Matriz de barcos do COM,Tipo do barco;Lista com coordenadas de todos os barcos;Tamanho da matriz do jogo;Matriz que administra os barcos do COM
def jogada(i,j,x,y,t,mat,carimbo,lista_pontos,n,matriz_barcos):
    '''
    Tipo: COM
    Técnico: Pega duas coordenadas (i,j) e (x,y) e preenche elas junto com todos os pontos que estiverem entre elas
    In game: Coloca UM barco entre duas coordenadas dadas(incluindo as próprias)
    '''
    i,j,x,y,lista_pontos = barcos(n,t,i,j,x,y,lista_pontos) #Verifica se os pontos são válidos(respeitam as regras do jogo)
    lista_aux = []
    if i == x: #(Barco na horizontal)
        for b in range(t): # Troca as coordenadas entre (i,j) e (x,y) pelo tipo do barco (A,N,D ou P)
            mat[i][j] = carimbo #Carimba o tipo do barco na Matriz de barcos do COM
            refil(i,j,carimbo,lista_aux) #Gera a lista que vai ser adicionada na Matriz administrativa mais tarde
            j += 1 #Cresce as colunas
        barquiz(matriz_barcos,lista_a) # Adiciona a lista criada no refil() na matriz administrativa
    elif j == y: #(Barco na vertical)
        for b in range(t): # Troca as coordenadas entre (i,j) e (x,y) pelo tipo do barco (A,N,D ou P)
            mat[i][j] = carimbo #Carimba o tipo do barco na Matriz de barcos do COM
            refil(i,j,carimbo,lista_aux) #Gera a lista que vai ser adicionada na Matriz administrativa mais tarde
            i += 1 #Cresce as linhas
        barquiz(matriz_barcos,lista_a) # Adiciona a lista criada no refil() na matriz administrativa
def barcos(n,t,i,j,x,y,lista_pontos): #função que verifica se o ponto marcado pelo jogador está na matriz
#tamanho a matriz, tamanho do barco, coordenadas (x,y,j,i), lista com coordenadas de todos os barcos
    ''' tipo : COM
    '''
    aux,i1,j1 = 0,i,j 
    if i == x: #(Barco na horizontal)
        lista_aux = []
        for elemento in range(t):
            if [i,j1] in lista_pontos: #confere se os pontos estão na lista
                aux = 1
                break
            lista_aux.extend([[i,j1]])
            j1 += 1
        if aux == 1:
            i,j,x,y = coordenada(n,t) #se estiverem,chama a funçao novamente para efetuar a jogada e conferir os pontos outra vez
            i,j,x,y,lista_pontos = barcos(n,t,i,j,x,y,lista_pontos)
        else:
            lista_pontos.extend(lista_aux)#caso aux == 0, adiciona os pontos verificados na lista
    elif j == y:#barco na vertical
        lista_aux = []
        for elemento in range(t):
            if [i1,j] in lista_pontos: #confere se os pontos estão na lista
                aux = 1
                break
            lista_aux.extend([[i1,j]])
            i1 += 1
        if aux == 1:
            i,j,x,y = coordenada(n,t)#se estiverem,chama a funçao novamente para efetuar a jogada e conferir os pontos outra vez
            i,j,x,y,lista_pontos = barcos(n,t,i,j,x,y,lista_pontos)
        else:
            lista_pontos.extend(lista_aux)
    return i,j,x,y,lista_pontos
def matriz(n): #cria uma matriz de ordem N
    matriz = []
    for i in range(n):
        matriz.append(n*["~"])
    return matriz
def matriz_esp(n):
    matriz = []
    for i in range(n+1):
        matriz.append((n+1)*["~"])
    for hi in range(n+1):
        matriz[0][hi] = hi
        matriz[hi][0] = hi
    return matriz
def imprime(mat,n):
    for l in range(n):
        print(n*"----")
        for c in range(n):
            print("|",mat[l][c],"",end = "")
        print("|")
    print(n*"----")
def coordenada_l(n,t):
    x = i = randint(0,n-1)
    j = randint(0,n-t)
    y = j + t-1
    return i,j,x,y
def coordenada_c(n,t):
    y = j = randint(0,n-1)
    i = randint(0,n-t)
    x = i + t-1
    return i,j,x,y
def coordenada(n,t): #chama aleatóriamente uma das opções de cordenadas(variando linhas ou colunas)
    verificador = randint(0,10)
    if verificador < 5:
        return coordenada_l(n,t)
    else:
        return coordenada_c(n,t)
def COM(n,mat,lista_pontos,matriz_barcos):
    num_barcos = floor((n*n)/64)
    tamanhos = [5,4,3,2]
    dic = {5 : "A" ,4 : "N",3 : "D", 2 : "P"}
    for t in tamanhos:
        for a in range(num_barcos):
            i,j,x,y = coordenada(n,t)
            jogada(i,j,x,y,t,mat,dic[t],lista_pontos,n,matriz_barcos)
#def play(n,quant_barcos):
#    for q in range(4*quant_barcos):
#        i,j = input()
def tiro(matiro,n,lista_pontos,lista_tiro,matriz_ADMP,PCOM_pontos): #COM
    x = randint(1,n)
    y = randint(1,n)
    while [x,y] in lista_tiro:
      x = randint(1,n)
      y = randint(1,n)
    if [x,y] in lista_pontos:
      matiro[x][y] = "X"
      PCOM_pontos += 1
      lista_tiro.append([x,y])
      contiros(x,y,matriz_ADMP)
    else:
      matiro[x][y] = "O"
      lista_tiro.append([x,y])
    #return x,y,matiro
    return PCOM_pontos
def refil(i,j,carimbo,lista_aux):
    global lista_a
    tiros_lev = 0
    lista_aux.append([i+1,j+1])
    lista_a = [carimbo,tiros_lev,len(lista_aux),lista_aux]
    #carimbo,tiros levados, tamanho barco, pontos barco
def barquiz(matriz_barcos,lista_a):
    matriz_barcos.append(lista_a)
def contiros(i,j,matriz_ADMP): #Do COM para Player, contabiliza os tiros levados
    linha = 0
    for f in matriz_ADMP:
        for u in matriz_ADMP[linha][3]:
            if [i,j] == u:
                matriz_ADMP[linha][1] += 1
        linha += 1
# Matriz com ondinhas da pessoa, matriz adiministrativa do COM
def derrubada(mati_paratiro,matriz_barcos): #pessoa atira no COM
    linha = 0
    for h in matriz_barcos:
        if matriz_barcos[linha][1] == matriz_barcos[linha][2]:
            for c in matriz_barcos[linha][3]:
                i,j = c
                mati_paratiro[i][j] = matriz_barcos[linha][0]
        linha += 1

#FUNÇÕES DO PLAYER
###########################################################
def P1(bb,bardic,lista_PP,mat_p,tamtriz,matriz_ADMP): #cria e verifica os pontos na matriz
    dic = {5 : "A" ,4 : "N",3 : "D", 2 : "P"}
    copia_bb = bb[:]
    for z in copia_bb:
        i,j = input("Primeira coordenada do seu {} :".format(z)).split(",")
        x,y = input("Segunda coordenada do seu {} :".format(z)).split(",")
        i,j,x,y = int(i),int(j),int(x),int(y)
        while (j == y and max((x-i),(i-x))+1 != bardic[z]) or (i == x and max((y-j),(j-y))+1 != bardic[z]) or (i not in range(1,tamtriz+1) or j not in range(1,tamtriz+1) or y not in range(1,tamtriz+1) or x not in range(1,tamtriz+1)) or (i != x and j != y):
            print("ERRO!\nDigite coordenadas válidas")
            i,j = input("Primeira coordenada do seu {} :".format(z)).split(",")
            x,y = input("Segunda coordenada do seu {} :".format(z)).split(",")
            i,j,x,y = int(i),int(j),int(x),int(y)
        lista_ijxy = []
        col,lin = min(y,j),min(x,i)
        if x == i:
            while col <= max(y,j):
                lista_ijxy.append([x,col])
                col += 1
        elif y == j:
            while lin <= max(x,i):
                lista_ijxy.append([lin,y])
                lin += 1
        for ponto in lista_ijxy:
            if ponto in lista_PP:
                print("ERRO!\nDigite coordenadas válidas")
                P1(copia_bb,bardic,lista_PP,mat_p,tamtriz)
                pivo = 1
                break
            else:
                pivo = 0
        if pivo == 0:
            for e in lista_ijxy:
                i,j = e
                mat_p[i][j] = "{}".format(dic[bardic[z]])
            matriz_ADMP.append([dic[bardic[z]],0,bardic[z],lista_ijxy])
            imprime(mat_p,tamtriz+1)
            lista_PP.extend(lista_ijxy)
            del bb[0]
def contirosP(i,j,matriz_barcos): #Do player para COM
    linha = 0
    for f in matriz_barcos:
        for u in matriz_barcos[linha][3]:
            if [i,j] == u:
                matriz_barcos[linha][1] += 1
        linha += 1
def tiroP(mati_paratiro,tamtriz,lista_PP,lista_tirop,matriz_ADMCOM,P_pontos):
    i,j = input("Atire: ").split(",")
    i,j = int(i),int(j)
    while (i < 1 or i > tamtriz) or (j < 1 or j > tamtriz) or ([i,j] in lista_tirop):
        print("Coordedas inválidas")
        i,j = input("Atire: ").split(",")
        i,j = int(i),int(j)
    lista_tirop.append([i,j])
    if [i,j] in lista_PP:
        print("Acertou")
        mati_paratiro[i][j] = "X"
        P_pontos += 1
        contirosP(i,j,matriz_ADMCOM)
    else:
        print("ERROOOWW")
        mati_paratiro[i][j] = "O"
    return P_pontos
# Matriz com ondinhas do player
def derrubadaP(mati_paratiro,matriz_barcos): #COM atira na pessoa 
    linha = 0
    for h in matriz_barcos:
        if matriz_barcos[linha][1] == matriz_barcos[linha][2]:
            for c in matriz_barcos[linha][3]:
                i,j = c
                mati_paratiro[i][j] = matriz_barcos[linha][0]
        linha += 1
###########################################################
from os import system
verificador = 1
while verificador == 1:
    menu = int(input(''' BATALHA NAVAL 
1) Jogar
2) Sobre o jogo
3) Sair
=> '''))
    if menu == 3:
        print("Tchau Marujo, até a próxima.")
        verificador = 0
    elif menu == 2:
        print(''' Esse será sobre o jogo
fmaslvmkdls~va
''')
        verificador = input("1) Voltar \n2) Sair")
    elif menu == 1:
        op = int(input('''1) P vs COM
2) P vs P
3) Voltar
=> '''))
        if op == 3:
            verificador = 0
        elif op == 1:
            P1_pontos = PCOM_pontos = 0 # Conta quantos pontos o jogador fez
            bardic = {"Porta-aviões" : 5,"Navios-tanque" : 4,"Destóier" : 3, "Pesca" : 2}
            tamtriz = int(input("Defina o tamanho do campo de batalha: "))
            if tamtriz > 20:
                print("Oi Jackson")
            while tamtriz < 8 :
                print("Tamanho inválido")
                tamtriz = int(input("Defina o tamanho do campo de batalha: "))
            p1 = input("Marujo, insira seu nome: ")
            quant_barcos = floor((tamtriz**2)/64)
            mat_p1 = matriz(tamtriz+1)
            matriz_ADMP1 = []
            aux_mat = matriz(tamtriz)
            aux_mat_ParaTiroCOM = matriz(tamtriz)
            aux_mat_ParaTiroP1 = matriz(tamtriz)
            coluna = linha = 0
            for s in range(tamtriz+1):
                mat_p1[0][coluna] = coluna
                coluna += 1
                mat_p1[linha][0] = linha
                linha += 1
            imprime(mat_p1,tamtriz+1)
            ba = quant_barcos*["Porta-aviões"]
            bn = quant_barcos*["Navios-tanque"]
            bd = quant_barcos*["Destóier"]
            bp = quant_barcos*["Pesca"]
            bb = []
            bb.extend(ba),bb.extend(bn),bb.extend(bd),bb.extend(bp)
            lista_PP1 = [] #lista pontos de p1, barcos dele
            lista_COM = [] #lista pontos do COM, barcos dele
            lista_tiroCOM = [] #lista dos tiros do COM
            lista_tiroP1 = [] #lista dos tiros do P1
            matriz_ADMCOM = []
            P1(bb,bardic,lista_PP1,mat_p1,tamtriz,matriz_ADMP1)
            Pontos_total = 0 # Conta quantas posições foram preenchidas (Máximo de pontos)
            for ki in range(quant_barcos*4):
                Pontos_total += matriz_ADMP1[ki][2]
            COM(tamtriz,aux_mat,lista_COM,matriz_ADMCOM)
            for fi in range(len(lista_COM)): #adiciona uma linha e uma coluna em todas as coordenadas (por causa do imprime)
                i,j = lista_COM[fi]
                lista_COM[fi] = [i+1,j+1]
            mat = matriz(tamtriz+1)
            mat_ParaTiroP1 = matriz(tamtriz+1)
            mat_ParaTiroCOM = matriz(tamtriz+1)
            linha = coluna = 0
            for xi in range(tamtriz):
              for yi in range(tamtriz):
                mat[xi+1][yi+1] = aux_mat[xi][yi]
                mat_ParaTiroP1[xi+1][yi+1] = aux_mat_ParaTiroP1[xi][yi]
                mat_ParaTiroCOM[xi+1][yi+1] = aux_mat_ParaTiroCOM[xi][yi]
            for si in range(tamtriz+1):
                mat[0][coluna] = coluna
                mat_ParaTiroP1[0][coluna] = coluna
                mat_ParaTiroCOM[0][coluna] = coluna
                coluna += 1
                mat[linha][0] = linha
                mat_ParaTiroP1[linha][0] = linha
                mat_ParaTiroCOM[linha][0] = linha
                linha += 1
            imprime(mat,tamtriz+1)
            verificador2 = 0
            while verificador2 == 0:
                system("clear")
                P1_pontos = tiroP(mat_ParaTiroP1,tamtriz,lista_COM,lista_tiroP1,matriz_ADMCOM,P1_pontos)
                derrubada(mat_ParaTiroP1,matriz_ADMCOM)
                imprime(mat_ParaTiroP1,tamtriz+1)
                PCOM_pontos = tiro(mat_ParaTiroCOM,tamtriz,lista_PP1,lista_tiroCOM,matriz_ADMP1,PCOM_pontos)
                derrubada(mat_ParaTiroCOM,matriz_ADMP1)
                imprime(mat_ParaTiroCOM,tamtriz+1)
                if P1_pontos == Pontos_total or PCOM_pontos == Pontos_total:
                    if P1_pontos == Pontos_total:
                        print("PARABÉNS marujo {}\nVocê conseguiu impedir a frota inimiga do ataque.\nAté a proxima".format(p1))
                    else:
                        print("VOCÊ PERDEU\nSua frota foi totalmente massacrada.")
                    verificador2 = 1
            fim_de_game = input("Deseja jogar novamente(S/N)? ")
            if fim_de_game == "S" or fim_de_game == "s":
                verificador = 1
            elif fim_de_game == "N" or fim_de_game == "n":
                print("Adeus Marujo\nFoi bom navegar com você.")
                verificador = 0
        elif op == 2:
            P1_pontos = P2_pontos = 0 # Conta quantos pontos cada jogador fez
            bardic = {"Porta-aviões" : 5,"Navios-tanque" : 4,"Destóier" : 3, "Pesca" : 2}
            tamtriz = int(input("Defina o tamanho do campo de batalha: "))
            if tamtriz > 20:
                print("Oi Jackson")
            while tamtriz < 8 :
                print("Tamanho inválido")
                tamtriz = int(input("Defina o tamanho do campo de batalha: "))
            p1 = input("Marujo 1, insira seu nome: ")
            p2 = input("Marujo 2, insira seu nome: ")
            quant_barcos = floor((tamtriz**2)/64)
            mat_p1 = matriz(tamtriz+1)
            mat_p2 = matriz(tamtriz+1)
            matriz_ADMP1 = []
            matriz_ADMP2 = []
            aux_mat_ParaTiroP2 = matriz(tamtriz)
            aux_mat_ParaTiroP1 = matriz(tamtriz)
            coluna = linha = 0
            for s in range(tamtriz+1):
                mat_p1[0][coluna] = coluna
                mat_p2[0][coluna] = coluna
                mat_p1[coluna][0] = coluna
                mat_p2[coluna][0] = coluna
                coluna += 1
            print("Matriz P1:")
            imprime(mat_p1,tamtriz+1)
            print("Matriz P2:")
            imprime(mat_p2,tamtriz+1)
            ba = quant_barcos*["Porta-aviões"]
            bn = quant_barcos*["Navios-tanque"]
            bd = quant_barcos*["Destóier"]
            bp = quant_barcos*["Pesca"]
            bb = []
            bb.extend(ba),bb.extend(bn),bb.extend(bd),bb.extend(bp)
            lista_PP1 = [] #lista pontos de p1, barcos dele
            lista_PP2 = [] #lista pontos do p2, barcos dele
            lista_tiroP2 = [] #lista dos tiros do P2
            lista_tiroP1 = [] #lista dos tiros do P1
            P1(bb,bardic,lista_PP1,mat_p1,tamtriz,matriz_ADMP1) #P1
            P1(bb,bardic,lista_PP2,mat_p2,tamtriz,matriz_ADMP2) #P2
            Pontos_total = 0 # Conta quantas posições foram preenchidas (Máximo de pontos)
            for ki in range(quant_barcos*4):
                Pontos_total += matriz_ADMP1[ki][2]
            mat_ParaTiroP1 = matriz(tamtriz+1)
            mat_ParaTiroP2 = matriz(tamtriz+1)
            linha = coluna = 0
            for xi in range(tamtriz):
              for yi in range(tamtriz): #pega a matriz auxilair (NxN) e copia na matriz original ((N+1)x(N+1)) para posteriormente poder colocar valores de linhas e colunas
                mat_ParaTiroP1[xi+1][yi+1] = aux_mat_ParaTiroP1[xi][yi]
                mat_ParaTiroP2[xi+1][yi+1] = aux_mat_ParaTiroP2[xi][yi]
            for si in range(tamtriz+1): #coloca os números das linhas e das colunas para ficar bonitinho
                mat_ParaTiroP1[0][coluna] = coluna
                mat_ParaTiroP2[0][coluna] = coluna
                mat_ParaTiroP1[coluna][0] = coluna
                mat_ParaTiroP2[coluna][0] = coluna
                coluna += 1
            verificador2 = 0
            while verificador2 == 0:
                system("clear") #limpa a tela para ficar bonitinho
                P1_pontos = tiroP(mat_ParaTiroP1,tamtriz,lista_PP2,lista_tiroP1,matriz_ADMP2,P1_pontos) #jogada do p1
                derrubada(mat_ParaTiroP1,matriz_ADMP2) #verifica se algum barco foi derrubado
                imprime(mat_ParaTiroP1,tamtriz+1)
                P2_pontos = tiroP(mat_ParaTiroP2,tamtriz,lista_PP1,lista_tiroP2,matriz_ADMP1,P2_pontos) #jogada do p2
                derrubada(mat_ParaTiroP2,matriz_ADMP1) #verifica se algum barco foi derrubado
                imprime(mat_ParaTiroP2,tamtriz+1)
                if P1_pontos == Pontos_total or P2_pontos == Pontos_total:
                    if P1_pontos == Pontos_total:
                        print("PARABÉNS marujo {}\nVocê conseguiu impedir a frota inimiga do ataque.\nAté a proxima".format(p1))
                        print("Marujo {} perdeu".format(p2))
                    else:
                        print("PARABÉNS marujo {}\nVocê conseguiu impedir a frota inimiga do ataque.\nAté a proxima".format(p2))
                        print("Marujo {} perdeu".format(p1))
                    verificador2 = 1
            fim_de_game = input("Deseja jogar novamente(S/N)? ")
            if fim_de_game == "S" or fim_de_game == "s":
                verificador = 1
            elif fim_de_game == "N" or fim_de_game == "n":
                print("Adeus Marujo\nFoi bom navegar com você.")
                verificador = 0