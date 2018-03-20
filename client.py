# -*- coding: utf-8 -*-

import socket               # Import socket module
import sys


TAMANHO_PEDACOS=100
BUFFER_LEN=(5+1+1+2+TAMANHO_PEDACOS)
TERMINADOR="1;>;0"

if len(sys.argv)!= 6:
	print "A entrada deve ser: python client.py ip porta tamanho string cifra"
	exit()

host=sys.argv[1]
port=int(sys.argv[2])
comprimento_msg=sys.argv[3]
msg=sys.argv[4].decode(sys.getfilesystemencoding()).encode('ascii','ignore')
cifra=int(sys.argv[5])%26

s = socket.socket()         # Create a socket object
#print host
host = socket.gethostbyname(host)# Get local machine name
port=int(port)
#print (host, port)
s.connect((host, port))
#tamanho;msg;cifra
pedacos=len(msg)
msg_quebrada=[ msg[i:i+TAMANHO_PEDACOS] for i in range(0, pedacos, TAMANHO_PEDACOS) ]
#print msg_quebrada
msg_decodificada=""
for m in msg_quebrada:
	#print m
	pacote="{:05d};{};{:02d}".format(len(m),m,cifra)
	#print pacote
	s.send(pacote)
	msg_decodificada+=s.recv(BUFFER_LEN)
print msg_decodificada
s.send(TERMINADOR)

#print "termina programa"
s.close()                    # Close the socket when done