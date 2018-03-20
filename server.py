# -*- coding: utf-8 -*-
import socket
import threading
import sys

BUFFER_LEN=1024
class Servidor():
	"""docstring for Servidor"""
	def __init__(self,port=5555):
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
		print 'Got connection from', addr
		pacote=c.recv(BUFFER_LEN)
		print pacote
		pacote=pacote.split(";")
		print pacote
		pacote=self.decodifica_msg(pacote)
		print pacote
		c.send(pacote)
		c.close()# Close the connection

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
	print sys.argv[1]
	S=Servidor(int(sys.argv[1]))


