while True:
	d, n = input().split()

	if d == '0' and n == '0':
		break

	v = [x if x != d else '' for x in n]

	j = ''.join(v)
	if j == '':
		j = '0'

	print(int(j))