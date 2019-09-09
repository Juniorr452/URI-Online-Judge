# -*- coding: utf-8 -*-

n = int(input())

cobaias = {
	'C': 0,
	'R': 0,
	'S': 0
}

for i in range(0, n):
	qtd, tipo = input().split()
	cobaias[tipo] = cobaias[tipo] + int(qtd)

total = sum(cobaias.values())

print("Total: {} cobaias".format(total))
print("Total de coelhos: {}".format(cobaias['C']))
print("Total de ratos: {}".format(cobaias['R']))
print("Total de sapos: {}".format(cobaias['S']))

print("Percentual de coelhos: {} %".format("%.2f" % (cobaias['C'] / total * 100)))
print("Percentual de ratos: {} %".format("%.2f" % (cobaias['R'] / total * 100)))
print("Percentual de sapos: {} %".format("%.2f" % (cobaias['S'] / total * 100)))