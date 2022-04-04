from math import floor
from random import randint
from os import system,name
from time import sleep
def limpa_tela(): #lipa a tela para ficar bonitinho
    system("cls" if name == "nt" else "clear")

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
        matriz_barcos.append(lista_a) # Adiciona a lista criada no refil() na matriz administrativa
    elif j == y: #(Barco na vertical)
        for b in range(t): # Troca as coordenadas entre (i,j) e (x,y) pelo tipo do barco (A,N,D ou P)
            mat[i][j] = carimbo #Carimba o tipo do barco na Matriz de barcos do COM
            refil(i,j,carimbo,lista_aux) #Gera a lista que vai ser adicionada na Matriz administrativa mais tarde
            i += 1 #Cresce as linhas
        matriz_barcos.append(lista_a) # Adiciona a lista criada no refil() na matriz administrativa
#tamanho a matriz, tamanho do barco, coordenadas (x,y,j,i), lista com coordenadas de todos os barcos
def barcos(n,t,i,j,x,y,lista_pontos):
    ''' 
    Tipo : COM
    Técnico: Verifica se os pontos dados e os pontos que estiverem entre eles, para ver se tem algum barco ali já
    In game: Implícita
    '''
    aux,i1,j1 = 0,i,j # Para modificar i ou j sem alterar o valor original
    if i == x: #(Barco na horizontal)
        lista_aux = [] # adicinamos temporariamente os pontos até validação da regra(dois corpos não ocupam o mesmo espaço)
        for elemento in range(t): # varia o J com o tamanho do barco
            if [i,j1] in lista_pontos: #confere se os pontos estão na lista que tem os pontos dos barcos
                aux = 1 #if mais a frente
                break
            lista_aux.extend([[i,j1]]) #adiciona o ponto
            j1 += 1
        if aux == 1: # só cai aqui dentro se algum ponto já estiver preenchido (na lista de pontos dos barcos)
            #gera novas coordenadas para validação
            i,j,x,y = coordenada(n,t)
    #se algum ponto estiver,chama a funçao novamente com os novos pontos para efetuar a jogada e conferir os pontos outra vez
            i,j,x,y,lista_pontos = barcos(n,t,i,j,x,y,lista_pontos)
        else:
    #caso todos os pontos não estejam na lista de pontos dos barcos, adiciona os pontos verificados na lista de pontos dos barcos
            lista_pontos.extend(lista_aux)
    elif j == y:# (Barco na vertical)
        lista_aux = [] # adicinamos temporariamente os pontos até validação da regra(dois corpos não ocupam o mesmo espaço)
        for elemento in range(t): # varia o I com o tamanho do barco
            if [i1,j] in lista_pontos: #confere se os pontos estão na lista que tem os pontos dos barcos
                aux = 1 #if mais a frente
                break
            lista_aux.extend([[i1,j]])#adiciona o ponto
            i1 += 1
        if aux == 1: # só cai aqui dentro se algum ponto já estiver preenchido (na lista de pontos dos barcos)
            #gera novas coordenadas para validação
            i,j,x,y = coordenada(n,t)
    #se algum ponto estiver,chama a funçao novamente com os novos pontos para efetuar a jogada e conferir os pontos outra vez
            i,j,x,y,lista_pontos = barcos(n,t,i,j,x,y,lista_pontos)
        else:
    #caso todos os pontos não estejam na lista de pontos dos barcos, adiciona os pontos verificados na lista de pontos dos barcos
            lista_pontos.extend(lista_aux)
    return i,j,x,y,lista_pontos
def matriz(n): #tamanho da matriz
    '''
    Tipo : Geral
    Técnico: cria uma matriz de ordem N
    In game: implícito
    '''
    matriz = []
    for i in range(n):
        matriz.append(n*["~"])
    return matriz
def imprime(mat,n): #printa mat de tamanho n
    '''
    Tipo : Geral
    Técnico: Imprime bonitinho uma matriz de ordem N
    In game: Mostra a matriz na tela
    '''
    for l in range(n):
        print(n*"----")
        for c in range(n):
            print("|{:^3}".format(mat[l][c]),end = "") #print bonitinho (:^3 força os prints a terem 3 espaços)
        print("|")
    print(n*"----")
def imprime_lado(mat1,mat2,n): #printa mat1 na esquerda, mat2 na direita, as duas de tamanho n
    '''
    Tipo : Geral
    Técnico: Imprime bonitinho duas matrizes de ordem N
    In game: Mostra as duas matrizes na tela, uma do lado da outra
    '''
    text = ""
    for l in range(n):
        text += (n*"----")+"     "+(n*"----")+"\n"
        for c1 in range(n):
            text += "|{:^3}".format(mat1[l][c1])
        text += "|    "
        for c2 in range(n):
            text += "|{:^3}".format(mat2[l][c2])
        text += "|    \n"
    text += (n*"----")+"     "+(n*"----")+"\n"
    print(text)
def coordenada_l(n,t): #tamanho da matriz, tamanho do barco
    '''
    Tipo : COM
    Técnico: Gera duas coordenadas com distância T na mesma linha
    In game: Gera um barco de tamanho T na horizontal
    '''
    x = i = randint(0,n-1) # (n-1) pq a matriz começa no 0 e vai até (n-1)
    j = randint(0,n-t) # (n-t) para pegar um ponto na submatriz e posteriormente somar t-1 para cair dentro da matriz
    # t-1 pois pegando o valor max(j)= n-t, e aplicando essa linha do cód, teremos y = (n-t) + t-1 = n-1 (borda da matriz)
    y = j + t-1 
    return i,j,x,y
def coordenada_c(n,t): #tamanho da matriz, tamanho do barco
    '''
    Tipo : COM
    Técnico: Gera duas coordenadas com distância T na mesma coluna
    In game: Gera um barco de tamanho T na vertical
    '''
    y = j = randint(0,n-1) # (n-1) pq a matriz começa no 0 e vai até (n-1)
    i = randint(0,n-t) # (n-t) para pegar um ponto na submatriz e posteriormente somar t-1 para cair dentro da matriz
    # t-1 pois pegando o valor max(i)= n-t, e aplicando essa linha do cód, teremos x = (n-t) + t-1 = n-1 (borda da matriz)
    x = i + t-1 
    return i,j,x,y
def coordenada(n,t): #tamanho da matriz, tamanho do barco
    '''
    Tipo : COM
    Técnico: chama aleatóriamente uma das opções de cordenadas(variando linhas ou colunas)
    In game: Implícito
    '''
    verificador = randint(0,10)
    if verificador < 5:
        return coordenada_l(n,t)
    else:
        return coordenada_c(n,t)
#tamanho da matriz, matriz, lista com os pontos dos barcos, matriz que tem os barcos
def COM(n,mat,lista_pontos,matriz_barcos):
    '''
    Tipo : COM
    Técnico: Gera a matriz com TODOS os barcos posicionados corretamente
    In game: Implícito
    '''
    num_barcos = floor((n*n)/64) #quantidade de barcos(nossa função)
    tamanhos = [5,4,3,2] #tamanhos dos tipos dos barcos em ordem
    dic = {5 : "A" ,4 : "N",3 : "D", 2 : "P"} #troca o tamanho do barco pela sua letra
    # os 2 for's pegam todos os tipos de barcos juntos (primeiro todos os A's depois os N' ...)
    for t in tamanhos:
        for a in range(num_barcos):
            i,j,x,y = coordenada(n,t) #gera as coordenadas do barco 
            jogada(i,j,x,y,t,mat,dic[t],lista_pontos,n,matriz_barcos) #efetua a verficação dos pontos e gera a matriz dos barcos
#matriz printada(que leva os tiros),tamanho da matriz,lista com os pontos dos barcos,matriz administrativa do Pl, pontos do COM
def tiro(matiro,n,lista_pontos,lista_tiro,matriz_ADMP,PCOM_pontos): #COM
    '''
    Tipo : COM
    Técnico: Gera um ponto (x,y) dentro da matriz para atirar e faz a verificação conforme as regras
    In game: Gera um tiro válido e faz a verificação (não atira no mesmo lugar e sempre dentro do campo de batalha)
    '''
    x = randint(1,n) # começa em 1 pra não pegar a linha/coluna dos números
    y = randint(1,n) # começa em 1 pra não pegar a linha/coluna dos números
    while [x,y] in lista_tiro: #verifica se o COM já atirou naquele lugar
      x = randint(1,n)
      y = randint(1,n)
    if [x,y] in lista_pontos: #Se acertou um barco
      matiro[x][y] = "X" #troca ~ por X
      PCOM_pontos += 1 #Pontos do COM
      lista_tiro.append([x,y]) # Adiciona o tiro no histórico
      contiros(x,y,matriz_ADMP) # Valida esse tiro dentro da matriz administrativa do Player
    else: #Se errou o barco
      matiro[x][y] = "O" #troca ~ por O
      lista_tiro.append([x,y]) # Adiciona o tiro no histórico
    return PCOM_pontos
# ponto (i,j), tipo do barco, lista zeravel dentro do código
def refil(i,j,carimbo,lista_aux): 
    '''
    Tipo : COM
    Técnico: Gera a lista (lista_a) que vai ser adicionada na Matriz administrativa mais tarde
    In game: Implícita
    '''
    global lista_a # outra lista auxiliar(que é criada várias vezes, só é finalizada depois da verificação jogada() ser completa)
    tiros_lev = 0 #tiros que o barco levou (0 pq está sendo criada a matriz)
    lista_aux.append([i+1,j+1]) # +1 pq na hora do jogo as coordenadas vão de 1 até o tamanho da matriz
    #carimbo,tiros levados, tamanho barco, pontos barco
    lista_a = [carimbo,tiros_lev,len(lista_aux),lista_aux]
# (i,j), matriz adiministrativa da pessoa
def contiros(i,j,matriz_ADMP):
    '''
    Tipo : Geral
    Técnico: Verifica se algum ponto de algum barco levou o tiro (i,j), contabiliza os tiros levados
    In game: Implícita
    '''
    linha = 0 #define qual barco vai ser escolhido
    for f in matriz_ADMP: #pega as linhas da matriz administrativa do player
        for u in matriz_ADMP[linha][3]: #pega a lista que contem todos os pontos do barco específico(definido pela variável linha)
            if [i,j] == u: # verifica se o tiro (i,j) acertou alguma posição desse barco
                matriz_ADMP[linha][1] += 1 # se sim marca um tiro levado
        linha += 1 # varia o barco 
# Matriz com ondinhas da pessoa, matriz adiministrativa
def derrubada(mati_paratiro,matriz_barcos):
    '''
    Tipo : Geral
    Técnico: Verifica se o barco foi derrubado
    In game: Se o barco foi derrubado, troca todos os X do barco na matriz por sua respectiva letra
    '''
    linha = 0 #define qual barco vai ser escolhido
    for h in matriz_barcos: #pega as linhas da matriz administrativa do COM
        if matriz_barcos[linha][1] == matriz_barcos[linha][2]: #se os tiros levados forem iguais ao tamanho do barco
            for c in matriz_barcos[linha][3]: # pega todos os pontos do barco
                i,j = c
                mati_paratiro[i][j] = matriz_barcos[linha][0] #troca o X na posição i,j pela letra do barco
        linha += 1 #varia o barco

#FUNÇÕES DO PLAYER
###########################################################
def verificada(coor):
    '''
    Tipo : Player
    Técnico: Verifica se a coordenada foi escrita corretamente "i,j" ou "i j" e se i e j são números
    In game: Retorna true se a coordenada foi válida e False caso contrário
    '''
    try: 
        i,j = coor.split(",") #tenta separar por vírgula
    except:
        try:
            i,j = coor.split() #tenta separar por espaço
        except:
            return False
    return (i.isdigit() and j.isdigit()) #após separar por virgula OU por espaço, verifica se são números
'''
tipos dos barcos nas quantidades certas(bb), tipo do barco :tamanho dele(baric),lista de pontos dos barcos do Pl(lista_PP), 
matriz com os barcos do jogador(mat_p),tamanho da matriz(tamtriz),matriz administrativa do player(matriz_ADMP),auxiliar da função
'''
def P1(bb,bardic,lista_PP,mat_p,tamtriz,matriz_ADMP,posicao = 0):
    '''
    Tipo : Player
    Técnico: Pede para pessoa inserir as coordenadas de todos os barcos e os verifica
    In game: Coloca os barcos do Player
    '''
    dic = {5 : "A" ,4 : "N",3 : "D", 2 : "P"} # tamanho : tipo
    while posicao != len(bb): # repete até o todos os barcos serem colocados
        print("\n")
        #primeira coordenada do barco
        coor = input("Primeira coordenada do seu {} (some {} em alguma coordenada):".format(bb[posicao],bardic[bb[posicao]]-1))
        while verificada(coor) == False: #verifica se a coordenada foi digitado corretamente
            print("ERRO!\nDigite coordenadas válidas")
            coor = input("Primeira coordenada do seu {} (some {} em alguma coordenada):".format(bb[posicao],bardic[bb[posicao]]-1))
        try: #transforma a primeira coordenada em dois valores isolados
            i,j = coor.split(",")
        except:
            i,j = coor.split()
        #última coordenada do barco
        coor = input("Última coordenada do seu {} :".format(bb[posicao]))
        while verificada(coor) == False: #verifica se a coordenada foi digitado corretamente
            print("ERRO!\nDigite coordenadas válidas")
            coor = input("Última coordenada do seu {} :".format(bb[posicao]))
        try:#transforma a última coordenada em dois valores isolados
            x,y = coor.split(",")
        except:
            x,y = coor.split()
        i,j,x,y = int(i),int(j),int(x),int(y)
        #linguiça de verificações sobre as coordenadas i,j,x,y
        while (j == y and max((x-i),(i-x))+1 != bardic[bb[posicao]]) or (i == x and max((y-j),(j-y))+1 != bardic[bb[posicao]]) or (i not in range(1,tamtriz+1) or j not in range(1,tamtriz+1) or y not in range(1,tamtriz+1) or x not in range(1,tamtriz+1)) or (i != x and j != y):
            '''
        Comentário especial para explicar o que cada coisa significa
        => (j == y):
            barco está na horizontal
        AND
        => max((x-i),(i-x))+1 != bardic[bb[posicao]]):
            -max((x-i),(i-x))+1: 
                pega o módulo da distância entre o ponto I ao ponto X, +1 para poder pegar o ponto final
                    ex: (1,1) e (1,5) tem distância 4, mas se considerarmos todos os espaços entre esses dois pontos
                incluindo eles, temos 5 espaços, ou seja um barco com tamanho 5.
            -bardic[bb[posicao]] : #pega o tamanho do barco dentro da função principal (P1)
                posicao = um número  #range(0,len(bb)) varia de 0 até o tamanho da lista bb
                bb = lista com nomes dos barcos em ordem decrescente de tamanho ex:["Porta-Aviões","Navios-Tanque",...]
                bardic = dicionário que tranforma o nome do barco no seu tamanho
        OR
        =>(i == x):
            barco está na vertical
        AND
        => max((y-j),(j-y))+1 != bardic[bb[posicao]]):
            -max((y-j),(j-y))+1: 
                pega o módulo da distância entre o ponto Y ao ponto J, +1 para poder pegar o ponto final
                    ex: (1,1) e (5,1) tem distância 4, mas se considerarmos todos os espaços entre esses dois pontos
                incluindo eles, temos 5 espaços, ou seja um barco com tamanho 5.
            -bardic[bb[posicao]] : #pega o tamanho do barco dentro da função principal (P1)
                posicao = um número  #range(0,len(bb)) varia de 0 até o tamanho da lista bb
                bb = lista com nomes dos barcos em ordem decrescente de tamanho ex:["Porta-Aviões","Navios-Tanque",...]
                bardic = dicionário que tranforma o nome do barco no seu tamanho
        OR
        => i,j,x ou y
            verifica se todos esses números estão no range(1,tamtriz+1), ou seja dentro do campo de batalha
        OR
        => i != x AND j != y
            verifica se os pontos estão na mesma linha ou mesma coluna
            ex: (1,1) e (3,4).
        Se TODAS as afirmações acima forem validadas podemos garatir 100% que é possível colocar um barco
        nas coordenadas dadas, falta verificar se já não existe um barco entre os dois pontos dados'''
        #CASO ESSA MERDA DE MEGA TEXTO NÂO DER CERTO
        #O programa vai continuar pedindo dois pontos até que tudo de certo(desconsiderando barco em cima de barco) 
            print("ERRO!\nDigite coordenadas válidas")
            coor = input("Primeira coordenada do seu {} (some {} em alguma coordenada):".format(bb[posicao],bardic[bb[posicao]]-1))
       	    while verificada(coor) == False:
                print("ERRO!\nDigite coordenadas válidas")
                coor = input("Primeira coordenada do seu {} (some {} em alguma coordenada):".format(bb[posicao],bardic[bb[posicao]]-1))
            try:
                i,j = coor.split(",")
            except:
                i,j = coor.split()
            coor = input("Última coordenada do seu {} :".format(bb[posicao]))
            while verificada(coor) == False:
                print("ERRO!\nDigite coordenadas válidas")
                coor = input("Última coordenada do seu {} :".format(bb[posicao]))
            try:
                x,y = coor.split(",")
            except:
                x,y = coor.split()
            i,j,x,y = int(i),int(j),int(x),int(y)
        lista_ijxy = [] #lista auxiliar para verificar se as coordenadas oferecidas podem ser efetuadas
        col,lin = min(y,j),min(x,i) #pega o menor valor das coordenadas na linha e na coluna
        if x == i: #se o barco estiver na horizontal
            while col <= max(y,j): #cresce a variável col até chegar no max(y,j)
                lista_ijxy.append([x,col]) #adiciona esses pontos na lista auxiliar
                col += 1
        elif y == j: #se o barco estiver na vertical
            while lin <= max(x,i): #cresce a variável lin até chegar no max(x,i)
                lista_ijxy.append([lin,y]) #adiciona esses pontos na lista auxiliar
                lin += 1
        #pega TODOS os pontos do suposto barco e verifica se ja não existe um barco naqueles pontos
        for ponto in lista_ijxy:
            if ponto in lista_PP:
                print("ERRO!\nDigite coordenadas válidas") #caso já exista um barco ali, chama a função novamente
                posicao = P1(bb,bardic,lista_PP,mat_p,tamtriz,matriz_ADMP,posicao)
                pivo = 1#impede que as coordenadas que deram errado do suposto barco, entrem na matriz adiminsitrativa
                break
            else:
                pivo = 0
        if pivo == 0: #se tudo deu certo, e for possível colocar o barco nas posições dejadas
            for e in lista_ijxy:
                i,j = e
                mat_p[i][j] = "{}".format(dic[bardic[bb[posicao]]]) #troca essas posições pela letra do barco
            #cria a linha na matriz administrativa referente ao barco recém colodo
            #Tipo do barco,tiros levados,tamanho do barco,lista com os seus pontos
            matriz_ADMP.append([dic[bardic[bb[posicao]]],0,bardic[bb[posicao]],lista_ijxy])
            imprime(mat_p,tamtriz+1) #mostra a matriz com o barco colocado
            lista_PP.extend(lista_ijxy) #adiciona os pontos do barco na lista com todos os pontos dos barcos(kkkk)
            posicao += 1 #troca o barco para validação
    return posicao
def tiroP(mati_paratiro,tamtriz,lista_PP,lista_tirop,matriz_ADMCOM,P_pontos):
    '''
    Tipo : Player
    Técnico: Pede pra pessoa atirar em uma coordenada e verifica se esse tiro é válido
    In game: Função que cuida dos tiros do player
    '''
    coor = input("Atire: ")
    while verificada(coor) == False: #verifica se a coordenada foi digitado corretamente
        print("ERRO!\nDigite coordenadas válidas")
        coor = input("Atire: ")
    try:
        i,j = coor.split(",")
    except:
        i,j = coor.split()
    i,j = int(i),int(j)
    # verifica se (i,j) está dentro do campo de batalha e se a pessoa já atirou nesse mesmo local
    while (i not in range(1,tamtriz+1)) or (j not in range(1,tamtriz+1)) or ([i,j] in lista_tirop): #+1 para chegar até a última linha e coluna
        print("Coordedas inválidas")
        coor = input("Atire: ")
        while verificada(coor) == False: #verifica se a coordenada foi digitado corretamente
            print("ERRO!\nDigite coordenadas válidas")
            coor = input("Atire: ")
        try:
            i,j = coor.split(",")
        except:
            i,j = coor.split()
        i,j = int(i),int(j)
    lista_tirop.append([i,j]) #com o tiro validado, adiciona na lista com os tiros do player
    if [i,j] in lista_PP: #verifica se o tiro acertou algum barco
        print("Fogo")
        mati_paratiro[i][j] = "X" #troca "~" por "X"
        P_pontos += 1 #conta quantos pontos o player fez
        contiros(i,j,matriz_ADMCOM) #descobre qual barco levou o tiro, e marca esse tiro na matriz administrativa
    else:
        print("Água")
        mati_paratiro[i][j] = "O" #troca "~" por "O"
    return P_pontos

#ACABARAM AS FUNÇÕES
###########################################################
if __name__ == '__main__':
	verificador = 0
	while True: #continua rodando o jogo até a pessoa escolher sair
	    menu = int(input("BATALHA NAVAL\n1) Jogar\n2) Sobre o jogo\n3) Sair\n=>"))
	    print("\n")
	    if menu == 3:
	        print("Tchau Marujo, até a próxima.")
	        break
	    elif menu == 2:
	        print('''Bem vindo Marujo!\nAntes de navegar, seguem algumas regras que regem o jogo:''')
	        print("Para jogar BATALHA NAVAL,você terá a opção de desafiar o computador.\nFeita a escolha, o jogador terá à disposição uma frota que deverá ser disposta em um campo de batalha de tamanho definido POR VOCÊ (tamanho mínimo 8x8)")
	        print("sua frota será composta de:\nX PORTA-AVIÕES(tamanho 5)\nX NAVIOS-TANQUE(tamanho 4)\nX DESTRÓIERS(tamanho 3)\nX PESCA(tamanho 2).")
	        print("obs: a quantidade de barcos varia de acordo com o tamanho do campo.\n\nSeus barcos devem ser posicionados com a primeira coordenada na LINHA e a segunda na COLUNA (formato L,C)")
	        print("\nSeu objetivo é afundar toda a frota inimiga tentando advinhar, a partir de jogadas alternadas, onde as embarcações foram posicionadas.\nAo acertar uma parte de embarcação, o local atingido será marcado por X até que o barco seja afundado e substituido pelas iniciais da embarcação.\nCaso o tiro caia na água, o local será marcado por O.") 
	        print("Portanto apresse-se para salvar sua frota! Boa Sorte, Marujo!\n")
	        verificador = int(input("1) Voltar \n2) Sair\n=> "))
	        print("\n")
	        while verificador not in (1,2):
	            verificador = int(input("1) Voltar \n2) Sair\n=> "))
	            print("\n")
	        if verificador == 2:
	            print("Tchau Marujo, até a próxima.")
	            break
	    elif menu == 1:
	        op = int(input("1) P vs COM\n2) Voltar\n=>"))
	        print("\n")
	        if op == 1:
	            P1_pontos = PCOM_pontos = 0 # Conta quantos pontos o jogador fez
	            #dicionário útil mais pra frente dentro das funções
	            bardic = {"Porta-aviões" : 5,"Navios-tanque" : 4,"Destóier" : 3, "Pesca" : 2}
	            #pega o tamanho da matriz
	            tamtriz = int(input("Defina o tamanho do campo de batalha (Apenas UM número): "))
	            if tamtriz > 20: #hehe
	                print("Oi Jackson")
	            while tamtriz < 8 : #tamanho mínimo é 8
	                print("Tamanho inválido")
	                tamtriz = int(input("Defina o tamanho do campo de batalha: "))
	            p1 = input("Marujo, insira seu nome: ") #Nome do marujo
	            print("\n")
	            quant_barcos = floor((tamtriz**2)/64) #pega a quantidade de cada tipo de barco
	            mat_p1 = matriz(tamtriz+1) #cria a matriz de jogo (+1 por causa da linha e coluna adicional com os núm)
	            matriz_ADMP1 = [] # matriz administrativa do P1
	            aux_mat = matriz(tamtriz) #COM vai colocar os barcos aqui, depois colocar essa matriz na mat(tamtriz+1)
	            aux_mat_ParaTiroCOM = matriz(tamtriz) #matriz para o P1 atirar 
	            aux_mat_ParaTiroP1 = matriz(tamtriz) #matriz para o COM atirar
	            coluna = linha = 0
	            for s in range(tamtriz+1): #adiciono uma linha e uma coluna a mais para printar bonitinho
	                mat_p1[0][coluna] = coluna
	                coluna += 1
	                mat_p1[linha][0] = linha
	                linha += 1
	            imprime(mat_p1,tamtriz+1) #mostro a matriz do player para poder adicionar os barcos
	            ba = quant_barcos*["Porta-aviões"]
	            bn = quant_barcos*["Navios-tanque"]
	            bd = quant_barcos*["Destóier"]
	            bp = quant_barcos*["Pesca"]
	            bb = []
	            #crio a lista com todos os barcos em ordem decrescente
	            bb.extend(ba),bb.extend(bn),bb.extend(bd),bb.extend(bp)
	            lista_PP1 = [] #lista pontos de p1, barcos dele
	            lista_COM = [] #lista pontos do COM, barcos dele
	            lista_tiroCOM = [] #lista dos tiros do COM
	            lista_tiroP1 = [] #lista dos tiros do P1
	            matriz_ADMCOM = [] #matriz administrativa do COM
	            posicao = 0 #util denrto de P1
	            posicao = P1(bb,bardic,lista_PP1,mat_p1,tamtriz,matriz_ADMP1) #player coloca seus barcos
	            Pontos_total = 0
	            for ki in range(quant_barcos*4):# Conta quantas posições foram preenchidas (Máximo de pontos)
	                Pontos_total += matriz_ADMP1[ki][2]
	            COM(tamtriz,aux_mat,lista_COM,matriz_ADMCOM) #computador coloca seus barcos
	            #adiciona uma linha e uma coluna em todas as coordenadas dos barcos (por causa do imprime)
	            for fi in range(len(lista_COM)):
	                i,j = lista_COM[fi]
	                lista_COM[fi] = [i+1,j+1]
	            mat = matriz(tamtriz+1) #matriz com os barcos do COM
	            mat_ParaTiroP1 = matriz(tamtriz+1) #matriz para P1 atirar
	            mat_ParaTiroCOM = matriz(tamtriz+1) #matriz para COM atirar
	            linha = coluna = 0
	            #coloco as matrizes de tamanho (tamtriz) em matrizes de tamanho (tamtriz+1),imprime()
	            for xi in range(tamtriz):
	              for yi in range(tamtriz):
	                mat[xi+1][yi+1] = aux_mat[xi][yi]
	                mat_ParaTiroP1[xi+1][yi+1] = aux_mat_ParaTiroP1[xi][yi]
	                mat_ParaTiroCOM[xi+1][yi+1] = aux_mat_ParaTiroCOM[xi][yi]
	            for si in range(tamtriz+1): #adiciono uma linha e uma coluna para printar bonitinho
	                mat[0][coluna] = coluna
	                mat_ParaTiroP1[0][coluna] = coluna
	                mat_ParaTiroCOM[0][coluna] = coluna
	                coluna += 1
	                mat[linha][0] = linha
	                mat_ParaTiroP1[linha][0] = linha
	                mat_ParaTiroCOM[linha][0] = linha
	                linha += 1
	            verificador2 = 0
	            limpa_tela()
	            while verificador2 == 0: #Mata mata acontece aqui dentro
	                imprime_lado(mat_ParaTiroP1,mat_ParaTiroCOM,tamtriz+1)#imprime os dois campos de batalha
	                #P1 atira
	                P1_pontos = tiroP(mat_ParaTiroP1,tamtriz,lista_COM,lista_tiroP1,matriz_ADMCOM,P1_pontos)
	                derrubada(mat_ParaTiroP1,matriz_ADMCOM) #verifica se algum barco do COM foi derrubado
	                #COM atira
	                PCOM_pontos = tiro(mat_ParaTiroCOM,tamtriz,lista_PP1,lista_tiroCOM,matriz_ADMP1,PCOM_pontos)
	                derrubada(mat_ParaTiroCOM,matriz_ADMP1) #verifica se algum barco do P1 foi derrubado
	                #imprime_lado(mat_ParaTiroP1,mat_ParaTiroCOM,tamtriz+1)
	                #verifica se alguém ganhou
	                sleep(0.3)
	                limpa_tela()
	                if P1_pontos == Pontos_total or PCOM_pontos == Pontos_total:
	                    if P1_pontos == Pontos_total:
	                        print("PARABÉNS marujo {}\nVocê conseguiu impedir a frota inimiga do ataque.\nAté a proxima".format(p1))
	                    else:
	                        print("VOCÊ PERDEU\nSua frota foi totalmente massacrada.")
	                    verificador2 = 1
	            fim_de_game = input("Deseja jogar novamente(S/N)? ") #termina/recomeça o jogo
	            if fim_de_game == "S" or fim_de_game == "s":
	                verificador = 1
	            elif fim_de_game == "N" or fim_de_game == "n":
	                print("Adeus Marujo\nFoi bom navegar com você.")
	                break #quebra o while grandão
sleep(1)
limpa_tela()