# -*- coding: utf-8 -*-
import socket
import threading

class Servidor():
	"""docstring for Servidor"""
	def __init__(self):
		#super(Servidor, self).__init__()
		self.s = socket.socket()
		host = socket.gethostname()
		port = 55555                # Reserve a port for your service.
		self.s.bind((host, port))
		self.s.listen(5)
		while True:
			c, addr = self.s.accept()     # Establish connection with client.
			t=threading.Thread(target=self.lida_cliente,args=(c,addr))
			t.run()
	
	def lida_cliente(self,c,addr):
		print 'Got connection from', addr
		c.send('Thank you for connecting. vc e demais! ')
		c.close()# Close the connection
		



S=Servidor()

