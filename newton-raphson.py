import numpy as np

def function(x):
	y = 1/2+1/4*x**2-x*np.sin(x)-1/2*np.cos(2*x)
	return y

def derivada(x):
	y = x/2+np.sin(2*x)-x*np.cos(x)-np.sin(x)
	return y

pi=np.pi/2
tol = 10**-5
i=1
maxIter = 20
while i < maxIter:
	x = pi - function(pi)/derivada(pi)
	if np.abs(x-pi) < tol:
		print("solucion: ", x)
		break
	pi = x
