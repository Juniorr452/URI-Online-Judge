# -*- coding: utf-8 -*-

i = 0.0

while i <= 2.0:
	j = i + 1
	for k in range(0, 3):
		j += 1

		print("I="+str(round(i, 2))+" J="+str(round(j, 2)))
	i += 0.2
	
