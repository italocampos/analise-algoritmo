import time
from random import randint
import matplotlib.pyplot as plt

def insertion_sort( lista ):
  for i in range( 1, len( lista ) ):
    chave = lista[i]
    k = i
    while k > 0 and chave < lista[k - 1]:
        lista[k] = lista[k - 1]
        k -= 1
    lista[k] = chave

def iteration(lista):
  inicio = time.time()
  insertion_sort(lista)
  fim = time.time()
  return(fim - inicio)

def media(lista, turns):
  r = 0;
  for i in turns:
    r += iteration(lista)
  return r/turns

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

vector = [1000, 10000, 20000, 50000, 70000]
medias = []

for i in range( 1, 5):
  lista = list(range(0, vector[i]))
  print(media(lista, 3))
  medias.append(media(lista, 3))

plt.plot(vector, medias)
plt.show()

vector = [1000, 5000, 10000, 15000, 20000, 30000, 40000, 50000, 75000, 100000, 125000, 150000]

def selection (A):
	for i in range(len(A)):       
	    # Find the minimum element in remaining  
	    # unsorted array 
	    min_idx = i 
	    for j in range(i+1, len(A)): 
	        if A[min_idx] > A[j]: 
	            min_idx = j 
	              
	    # Swap the found minimum element with  
	    # the first element         
	    A[i], A[min_idx] = A[min_idx], A[i]
