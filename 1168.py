n = int(input())

m = {
	"1": 2,
	"2": 5,
	"3": 5,
	"4": 4,
	"5": 5,
	"6": 6,
	"7": 3,
	"8": 7,
	"9": 6,
	"0": 6
}

for i in range(0, n):
	v = input()
	s = 0
	for c in v:
		s += m[c]

	print("{} leds".format(s))