from mcl import lcg
from collections import Counter
import math
math.e

modulo = 2**31
a = 1103515245
c = 12345

# Aceitação/rejeição
def Poisson(n=0, P=1, lamb=10): 
	while True:
		R = lcg(modulo, a, c)
		P = P*R
		# print(P, "<", math.e**(-lamb))
		if P < math.e**(-lamb):
			return n
		n = n+1
	return -1

def generateInPlot(n_sample, sample_size):
	for sample_i in range(n_sample):
		result = []
		for i in range(1, sample_size):
			result.append(Poisson())

		# counter occurrences
		resultCount = Counter(sorted(result))
		# print(resultCount)
		x = []
		y = []
		for i in resultCount:
			x.append(i)
			y.append(resultCount[i])
			# print(i, "->", resultCount[i])

		# plot chart
		import matplotlib.pyplot as plt
		plt.plot(x, y, marker='o')
		plt.title('sample')
		plt.xlabel('Values x')
		plt.ylabel('Occurrences')
		plt.show()

generateInPlot(10, 1000)
generateInPlot(10, 10000)
generateInPlot(10, 100000)