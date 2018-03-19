# -*- coding: utf-8 -*-

a=[1,2,3,4,'5']


for i in a:
	print i

i=2
j=3
if i>j:
	print "i>j{} {}".format(i,2.0)
elif j>i:
	print "j>i{} {}".format(j,2.0)

else:
	print "igual"
msg="1;oi;2"
msg=msg.split(";")
print msg[1]

dicto={'data':"18/03/18","hora":"11:06 am","mesa":["ventilador","PC"],"qtd":1}
print dicto['mesa']