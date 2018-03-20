# -*- coding: utf-8 -*-
import sys

if len(sys.argv)!= 3:
	print "A entrada deve ser: python codificador.py string cifra"
	exit()

msg_original=sys.argv[1].decode(sys.getfilesystemencoding()).encode('ascii','ignore')
cifra=int(sys.argv[2])%26

print msg_original
msg_codificada=""
for c in msg_original:
	asc_codificado=ord(c)+cifra
	if asc_codificado>122:
		asc_codificado-=26
	msg_codificada+=str(unichr(asc_codificado))
print msg_codificada