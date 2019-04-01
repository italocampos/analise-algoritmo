from time import time
from matplotlib import pyplot as chart

def lista_primo(n):
	primos = []
	for numero in range(2,n+1):
		divisor = 2
		while (divisor < numero and numero % divisor != 0):
			divisor += 1
		if divisor == numero:
			primos.append(numero)
	return primos

# Valores de x
values = range(2000)
# Valores de y
times = []

# Laço de execução do algoritmo para cada valor de x
for value in values:
	# Execução do algoritmo
	average = 0
	execution = range(5)
	for _ in execution:
		initial = time()
		lista_primo(value)
		average += time() - initial
	average /= len(execution)
	times.append(average)
	print('Iteration {a}/{b} finished. Computed time: {time}'.format(a = value, b = len(values), time = average))

# Mostrar gráficos
chart.title('Algoritmo lista_primo')
chart.plot(values, times, color = 'blue')
chart.xlabel('Tamanho da entrada')
chart.ylabel('Tempo médio')
chart.xlim(0, len(values))

# Estabelecendo valores que aparecerão no eixo x
x_labels = []
x_markup = []
i = 0
label = True
while i <= len(values):
	x_markup.append(i)
	if label:
		x_labels.append(str(i))
		label = False
	else:
		x_labels.append('')
		label = True
	i += int(len(values)*0.05)

chart.xticks(x_markup, x_labels)
#chart.xticks(list(range(1,int(len(values)//2*0.2*len(values)))))#,[str(i) for i in range(1,len(values)+1)])
#chart.ylim(0, len(values))
chart.grid(b = True)
chart.savefig('lista_primo.png')
chart.show()

# Escrevendo dados em arquivo
file = open('data.csv', 'w')
file.write('Tamanho da entrada\tTempo\n')
for i in range(len(values)):
	file.write('{n}\t{tempo}\n'.format(n = i, tempo = times[i]))