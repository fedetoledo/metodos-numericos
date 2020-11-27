import numpy as np

def funcion(x):
	#y = np.exp(-x)-x
	y = x**3-2*x**2-5 #3.a
	#y = x**3+3*x**2-1 #3.b
	return y

def secante(a,b,tol,n):
	i=2
	q0 = funcion(a)
	q1 = funcion(b)

	while(i < n):

		x = b - q1*(b-a)/(q1-q0)
		
		print(' i    a       b       x        error')
		print(' --  -----   -----   -----    ----')
		print('%2d'%i,' ','%1.3f'%a,' ','%1.5f'%b,' ','%1.5f'%x,' ','%1.3f'%funcion(x))
		print()

		if np.abs(funcion(x)) < tol:
			return x

		i = i + 1
		a=b
		q0=q1
		b=x
		q1=funcion(x)


print(secante(1,4,10**-4,20)) #2.6906484961992585
#print(secante(-3,-2,10**-4,20)) #solucion = -2.879385194736809
