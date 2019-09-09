# -*- coding: utf-8 -*-

i = 1
j = 7

while i <= 9:
	j = 7 + i
	for k in range(0, 3):
		j -= 1
		print("I="+str(i)+" J="+str(j))
	i += 2
	
