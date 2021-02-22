# https://en.wikipedia.org/wiki/Linear_congruential_generator

def lcg(modulo, a, c, semente=None):
	if semente != None:
		lcg.anterior = semente
	num_aleatorio = (lcg.anterior * a + c) % modulo
	lcg.anterior = num_aleatorio
	return num_aleatorio/modulo
lcg.anterior = 2222


# for i in range(1,1000):
# 	result = lcg(2**31, 1103515245, 12345)
# 	print(result)