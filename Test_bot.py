import telepot
import time
from telepot.loop import MessageLoop
def printa(idP1,tamtriz,matriz_para_printar): #bot manda msg com a matriz desejada #antigo imprime()
  matriz = matriz_para_printar
  mat_in_text = ""
  mensagem = tamtriz
  for x in range(len(matriz)):
  	mat_in_text += len(matriz)*"--------"+"\n"
  	for y in range(len(matriz[0])):
  		mat_in_text += "|"+"   "+matriz[x][y]+"   "
  	mat_in_text += "|\n"
  mat_in_text += "--------"*len(matriz)
  bot.sendMessage(idP1,mat_in_text)
def rangi(): #pega o intervalo [k,h], ou seja, range(k,h+1)
	global rang #deixo essa lista como global para poder definir o range antes de chamar outra função
	k,h = rang #rang vai ser sempre algo do tipo [k,h]
	return range(k,h+1)
def recebe(msg):
	global idP1,lista_nome
	idP1 = msg["chat"]["id"]
	lista_nome = [msg["chat"]["first_name"]]
	mensagem = transformador(msg["text"])
	if mensagem != None:
		guardador(mensagem) #dentro do guardador que o código principal vai receber permissão pra continuar ou não
	else:
		bot.sendMessage(idP1,"Por favor insíra um valor válido!")
def guardador(texto): #nosso programa vai rodar dentro dessa função
	global lista_mensagem,continuar #continuar vai ser a variável que vai "pausar" o programa pra pessoa inserir o dado
	lista_mensagem.append(texto) #adiciono na lista a última mensagem que enviei pro bot
	if len(lista_mensagem) > 1: #quero uma lista com um único elemento
		for k in range(len(lista_mensagem)-1): #-1 pq quero deixar somente o último termo da lista
			del lista_mensagem[k]
	continuar = 1 #deixo o programa continuar rodando
def transformador(mensa): #transforma a mensagem enviada pro bot em um valor ou em uma coordenada
	global idP1
	if mensa == "/start":
		return mensa
	if len(mensa) >= 3: #se for coordenada
		mensa = mensa.split(",")
		i,j = mensa
		return [int(i),int(j)]
	elif len(mensa) == 1: #se for valor
		try:
			mensa = int(mensa)
			return mensa
		except:
			return mensa
	return None #se a pessoa digitar errado ex: "1," (não vai entrar em nenhum caso, vai pedir pra pessoa digitar de novo)
################
#Coisas para lembrar:
# continuar = variável que vai segurar("pausar") o programa principal pra pessoa poder enviar a mensagem pro bot
# lista_mensagem = lista com um único elemento, a última mensagem que a pessoa mandou
# rang = lista com dois valores(k,h) que representam um range(k,h+1)
################
bot = telepot.Bot("792531396:AAGDOE-R5R4oTgatC3Q2YT0OZV0XmleRrQ0")
tamtriz,matriz_para_printar = 0,[]
idP1 = 0 #pega o id da pessoa para poder manda mensagem para ela depois
MessageLoop(bot, recebe).run_as_thread() #pega as informações que enviamos pro bot (podemos trabalhar dentro da função recebe)
print("Escutando ...")
lista_mensagem = []
lista_nome = []
rang = [1,3]
while idP1 == 0:
	pass
print(idP1)
bot.sendMessage(idP1,"Primeira coordenada do seu A: ")
continuar = 0
while continuar == 0:
	pass
continuar = 0
i,j = lista_mensagem[0]
bot.sendMessage(idP1,"Segunda coordenada do seu A: ")
while continuar == 0:
	pass
continuar = 0
x,y = lista_mensagem[0]
print("i: ",i)
print("j: ",j)
print("x: ",x)
print("y: ",y)
print(lista_nome)