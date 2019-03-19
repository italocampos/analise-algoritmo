# Ranges: 1k, 10k, 20k, 50k, 70k
from random import randint
from time import time
from matplotlib import pyplot as frame

def bubble_sort(lista):
	elementos = len(lista)-1
	ordenado = False
	while not ordenado:
		ordenado = True
		for i in range(elementos):
			if lista[i] > lista[i+1]:
				lista[i], lista[i+1] = lista[i+1],lista[i]
				ordenado = False
				#print(lista)
	return lista

def get_vector(length, mode = 'r'):
	if mode == 'r':
		vector = []
		for _ in range(length):
			vector.append(randint(0,length))
		return vector
	elif mode == 'o':
		return list(range(length))
	elif mode == 'i':
		return list(range(length))[::-1]
	else:
		raise('Unknown list generation mode.')

#values = [1000, 2000, 10000, 15000, 20000, 30000, 40000, 50000, 75000, 100000, 125000, 150000]
values = [500, 1000, 1500, 2000, 2500, 3000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000]
times = []

# Calcular as médias para vetores com valores randômicos
for value in values:
	average = 0
	for i in range(3):
		initial = time()
		bubble_sort(get_vector(value, 'r'))
		average += time() - initial
		print('{a} - Iteration #{b} finished.'.format(a = value, b = i))
	average /= 3
	times.append(average)
	print('Tests for {a} vaules finished. Computed time: {b}'.format(a = value, b = average))

# Mostrar gráficos
frame.plot(values, times)
frame.xlabel('Tamanho da entrada')
frame.ylabel('Tempo médio')
frame.show()