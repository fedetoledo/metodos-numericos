import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from random import randint
from math import floor
import metodoLR as lr

def ingresarDatos(n, min, max, auto):
	x,y = [], []
	for i in range(1,n+1):
		x.append(i)
		valor = randint(min,max) if auto else float(input('n {}: '.format(i)))
		y.append(valor)
	return [x, y]

def seleccionarIngresoDatos(n):
	choice = input("Ingresar datos [I] o generar [G]: ").lower()
	if choice not in ['i','g']:
		print("Opcion invalida, elija una opcion correcta")
		exit()
	elif choice == 'i':
		x, y = ingresarDatos(n, -15, 15, False)
	else:
		x, y = ingresarDatos(n, -15, 15, True)
	return [x, y]

def generarGrafico(n, px,py, solution):
	x = np.linspace(0,n,100)
	f = np.poly1d(solution)
	y = f(x)
	plt.plot(x, y, '-r')
	plt.plot(px, py, 'o')
	plt.title('Regresion simple')
	plt.xlabel('x', color='#1C2833')
	plt.ylabel('y', color='#1C2833')
	plt.grid()
	plt.show()

def generarMatriz(datos, orden):
	matriz = np.empty([len(datos),orden])
	for i in range(len(datos)):
		if orden != 1: #Is X, else Y
			for j in range(orden):
				matriz[i][j] = datos[i]**(orden-j-1) if j < orden-1 else 1
		else: 
			matriz[i] = datos[i]
	return matriz

def regresion():
	print("Regresion simple")

	n = int(input('Cantidad de muestras: '))
	orden = int(input('Orden de la regresion: '))

	x, y = seleccionarIngresoDatos(n)
	print('Vector x \n', x)
	print('Vector y \n', y)
	matrizX = generarMatriz(x, orden+1)
	matrizY = generarMatriz(y, 1)

	transpuestaX = np.transpose(matrizX)

	izquierda = transpuestaX.dot(matrizX)
	derecha = transpuestaX.dot(matrizY)

	print('Matriz x: \n', izquierda)
	print('Matriz y: \n', derecha)

	vector_solucion = lr.LR(orden+1, izquierda, derecha)
	print('Vector solucion del sistema \n', vector_solucion)

	generarGrafico(n, x, y, vector_solucion)

if __name__ == '__main__':
	regresion()