# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import socket				 					#importa modulo de socket
import sys										#importa modulo de argv

def codificador(msg_original,cifra):
	msg_original=msg_original.replace(" ","").replace(".","").replace(",","").replace('\n',"").lower()
	msg_codificada=""
	for c in msg_original:
		asc_codificado=ord(c)+cifra
		if asc_codificado>122:
			asc_codificado-=26
		msg_codificada+=str(unichr(asc_codificado))
	return msg_codificada


TAMANHO_PEDACOS=100								#tamanho maximo do pedaço da string que será enviada		
BUFFER_LEN=(5+1+1+2+TAMANHO_PEDACOS)			#tamanho maximo da mensagem que será enviada
TERMINADOR="1;>;0"								#terminador, que sinaliza fim de comunicação

if len(sys.argv)!= 5:							#caso os argumentos passados não correspondam com esperado
												#levanta mensagem de erro
	print "A entrada deve ser: python client.py ip porta string cifra"
	exit()

host=sys.argv[1]								#obtem o ip do servidor do primeiro argumento
port=int(sys.argv[2])							#obtem a porta do segundo arguemento
#comprimento_msg=sys.argv[3]					#obtem o tamanho da mensagem do terceiro argumento
												#obtem string do quarto argumento
												#codifica mensagem em ascii, ignorando caracteres fora dela
msg=sys.argv[3].decode(sys.getfilesystemencoding()).encode('ascii','ignore')
cifra=int(sys.argv[4])%26						#obtem a cifra do 5 argumento, o resto da divisão
												#serve para garantir que a cifra esteja dentro do alfabeto

msg=codificador(msg,cifra)

s = socket.socket()         					#cria socket para comunicação com o servidor
s.settimeout(15.0)
#print host
host = socket.gethostbyname(host)				#obtem nome de maquina doip do servidor				
#print (host, port)
s.connect((host, port))							#conecta ao servidor pelo host na porta port
#tamanho;msg;cifra
												#quebra a mensagem em n pedaços de tamanho TAMANHO_PEDACOS
msg_quebrada=[ msg[i:i+TAMANHO_PEDACOS] for i in range(0, len(msg), TAMANHO_PEDACOS) ]
#print msg_quebrada
msg_decodificada=""								#inicializa mensagem decodificada
for m in msg_quebrada:							#percorre a lista com a mensagem quebrada em n pedaços
	#print m
	pacote="{:05d};{};{:02d}".format(len(m)		#formata o pacote utilizando o padrão tamanho;msg;cifra
									,m,cifra)	#tamanho ocupa 5 caracteres e cifra 2														
	#print pacote
	s.send(pacote)								#envia pacote formatado
	msg_decodificada+=s.recv(BUFFER_LEN)		#concatena a mensagem decriptada
print msg_decodificada
s.send(TERMINADOR)								#envia TERMINADOR
	
#print "termina programa"
s.close()                    					#fecha conexão