# -*- coding: utf-8 -*-

maior = -1
index_maior = -1

for i in range(1, 101):
	n = int(input())
	if n > maior:
		maior = n
		index_maior = i

print(maior)
print(index_maior)
