# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import socket				 					#importa modulo de socket
import sys										#importa modulo de argv
import threading								#importa modulo de threading

TAMANHO_PEDACOS=100								#tamanho maximo do pedaço da string que será enviada		
BUFFER_LEN=(5+1+1+2+TAMANHO_PEDACOS)			#tamanho maximo da mensagem que será enviada
TERMINADOR="1;>;0"								#terminador, que sinaliza fim de comunicação

class Servidor():
	"""Classe que modela o servidor do trabalho"""
	def __init__(self,port=5555):
		"""Construtor do trabalho, esse metodo rodará até o fechamento do servidor pelo usuário
		 por CTRL+C"""
		self.s = socket.socket()				#Abre Socket e trata erro de address already in use
		self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)				
		self.s.bind(('', port))					#faz o bind na porta devida
		self.s.listen(5)						#prepara conexões vindoras
		while True:
			c, addr = self.s.accept()     		#espera conexão com o cliente
			c.settimeout(15.0)
			t=threading.Thread(target=			#prepra thread no metodo lida_cliente
							self.lida_cliente,
							args=(c,addr))
			t.run()								#dispara thread t
	
	def lida_cliente(self,c,addr):
		"""Metodo que lida com demanda do cliente"""
		#print 'Got connection from', addr
		pacote=""								#inicializa variaveis
		msg_decodificada=""
		while pacote !=TERMINADOR:				#esse metodo rodará até receber o terminador
			pacote=c.recv(BUFFER_LEN)			#lê o cliente
			if pacote !=TERMINADOR:				#caso o pacote recebido não seja o terminador
				#print pacote
				pacote=pacote.split(";")		#separa o pacote para obter o tamanho do trecho enviado,
												#trecho e cifra em uma lista
				#print pacote
				pacote=self.decodifica_msg(pacote)#decifra trecho
				msg_decodificada+=pacote		#concatena mensgem decifrada
				c.send(pacote)					#envia trecho decifrado
		c.close()								#fecha a conexão
		print msg_decodificada

	def decodifica_msg(self,pacote):
		"""Decifra a mensagem em pacote"""
		msg_decodificada=""
		cifra=int(pacote[2])					#obtem a cifra da mensagem
		for c in pacote[1]:						#para cada letra do trecho
			asc_decodificado=ord(c)-cifra		#reduz da letra o numero de casas referentes a cifra
			if asc_decodificado<97:				#caso o codigo ascii seja inferior ao a, avança o codigo até o final,
												#fazendo com que a-1=z
				asc_decodificado+=26
			msg_decodificada+=str(unichr(		#torna o codigo ascii em caracter novamente
										asc_decodificado
										))
		return msg_decodificada					#retorna trecho decodificado
		


if __name__=='__main__':						
	#print sys.argv[1]
	if len(sys.argv)!=2:						#caso os argumentos passados não correspondam com esperado
												#levanta mensagem de erro				
		print "A entrada deve ser: python server.py porta"
	else:
		S=Servidor(int(sys.argv[1]))			#inicializa o servidor na porta passada no primeiroargumento


