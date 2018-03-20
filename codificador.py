# -*- coding: utf-8 -*-
import sys

if len(sys.argv)!= 3:
	print "A entrada deve ser: python codificador.py string cifra"
	exit()

msg_original=sys.argv[1].decode(sys.getfilesystemencoding()).encode('ascii','ignore')
cifra=int(sys.argv[2])%26
msg_original=msg_original.replace(" ","").replace(".","").replace(",","").replace('\n',"").lower()
print msg_original
msg_codificada=""
print "=============================="
for c in msg_original:
	asc_codificado=ord(c)+cifra
	if asc_codificado>122:
		asc_codificado-=26
	msg_codificada+=str(unichr(asc_codificado))
print msg_codificada
file=open("codificado",'w')
file.write(msg_codificada)
file.close()
file=open("decodificado",'w')
file.write(msg_original)
file.close()