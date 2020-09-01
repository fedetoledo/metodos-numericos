import numpy as np

def ingresarDatos():
	n = int(input("Ingrese orden de la matriz: "))

	matriz = np.zeros([n,n], dtype = np.float) 
	b = np.zeros([n], dtype = np.float) 
	
	print("Ingrese elementos de la matriz: ")
	for i in range(0,n):
		for j in range(0,n):
			matriz[i,j] = input("Elemento a["+str(i+1)+"]["+str(j+1)+"]: ")
	for i in range(0,n): 
		b[i] = input("Elemento b["+str(i+1)+"]: ")
	print(matriz)
	return [n, matriz, b]

def generarDatos():
	n=3
	matriz = np.array([[2,6,-1],[1,5,-5],[1,-1,1]], dtype = np.float)
	b = np.array([11,-4,2])
	return [n, matriz, b]

def seleccionarIngresoDatos():
	choice = input("Correr ejemplo [p] o ingresar datos manualmente [m]: ")
	if choice.lower() == 'm':
		return ingresarDatos()
	elif choice.lower() == 'p':
		return generarDatos()
	else:
		print("Elija una opcion correcta, p o m")
		exit()

def descomposicionLR(n, matriz):
	ciclo = 0
	L = np.zeros([n,n])
	R = np.zeros([n,n])

	for k in range(0,n):
		ciclo+=1

		for j in range(k,n):
			L[j,k] = matriz[j,k]
			R[k,j] = matriz[k,j]/L[k,k]

		for i in range(k,n):
			for j in range(k,n):
				matriz[i,j] = matriz[i,j] - L[i,k]*R[k,j]
	return [L,R]

def getVectorCoeficientes(n, indVector, L, R):
	c = np.zeros([n])
	c[0] = indVector[0]/L[0,0]

	for i in range(1,n):
		sumatoria = sum([L[i,j]*c[j] for j in range(0,i)])
		c[i] = (indVector[i] - sumatoria)/L[i,i]
	return c

def busquedaVectorX(n, c, R):
	x = np.zeros([n])
	x[n-1] = c[n-1]

	for i in range(n-2,-1,-1):
		sumatoria = sum([R[i,j]*x[j] for j in range(i+1,n)])
		x[i] = c[i] - sumatoria
	return x

def busquedaInversa(n, L, R):
	vectores = np.zeros([n,n])
	identidad = np.identity(n)
	for i, vector in enumerate(identidad):
		c = getVectorCoeficientes(n, vector, L, R)
		vectores[i] = busquedaVectorX(n, c, R)
	inversa = np.transpose(vectores)
	return inversa

def calcularDeterminante(n, L):
	determinante = 1
	for i in range(0,n):
		determinante *= L[i,i]
	return determinante

def LR(n, matriz, b):
	L, R = descomposicionLR(n, matriz)
	c = getVectorCoeficientes(n, b, L, R)

	solucion = busquedaVectorX(n, c, R)
	return solucion

def help():
	print('Para correr el Metodo LR: metodoLR.LR(orden, matriz, b)')
