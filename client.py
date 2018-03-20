#!/usr/bin/python           # This is client.py file

import socket               # Import socket module
import sys


BUFFER_LEN=1024

host=sys.argv[1]
port=int(sys.argv[2])
comprimento_msg=sys.argv[3]
msg=sys.argv[4]
cifra=sys.argv[5]

s = socket.socket()         # Create a socket object
print host
host = socket.gethostbyname(host)# Get local machine name
port=int(port)
print (host, port)
s.connect((host, port))
#tamanho>=<msg>=<ciframsg
pacote="{};{};{}".format(len(msg),msg,cifra)
print pacote
s.send(pacote)
a=s.recv(BUFFER_LEN)
print a
print "termina programa"
s.close()                    # Close the socket when done