def lista_primo(n):
	primos = []
	for numero in range(2,n+1):
		divisor = 2
		while (divisor < numero and numero % divisor != 0):
			divisor += 1
		if divisor == numero:
			primos.append(numero)
	return primos