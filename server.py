# -*- coding: utf-8 -*-
import socket
import threading
import sys

TAMANHO_PEDACOS=100
BUFFER_LEN=(5+1+1+2+TAMANHO_PEDACOS)
TERMINADOR="1;>;0"

class Servidor():
	"""docstring for Servidor"""
	def __init__(self,port=55555):
		#super(Servidor, self).__init__()
		self.s = socket.socket()
		self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		host = socket.gethostname()
		self.s.bind(('', port))
		self.s.listen(5)
		while True:
			c, addr = self.s.accept()     # Establish connection with client.
			t=threading.Thread(target=self.lida_cliente,args=(c,addr))
			t.run()
	
	def lida_cliente(self,c,addr):
		pacote=""
		#print 'Got connection from', addr
		msg_decodificada=""
		while pacote !=TERMINADOR:
			pacote=c.recv(BUFFER_LEN)
			if pacote !=TERMINADOR:
				#print pacote
				pacote=pacote.split(";")
				#print pacote
				pacote=self.decodifica_msg(pacote)
				msg_decodificada+=pacote
				c.send(pacote)
		c.close()# Close the connection
		print msg_decodificada

	def decodifica_msg(self,pacote):
		#tamanho>=<msg>=<cifra
		msg_decodificada=""
		cifra=int(pacote[2])
		for c in pacote[1]:
			asc_decodificado=ord(c)-cifra
			if asc_decodificado<97:
				asc_decodificado+=26
			msg_decodificada+=str(unichr(asc_decodificado))
		return msg_decodificada
		


if __name__=='__main__':
	#print sys.argv[1]
	if len(sys.argv)!=2:
		print "A entrada deve ser: python server.py porta"
	else:
		S=Servidor(int(sys.argv[1]))


