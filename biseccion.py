import numpy as np

def Funcion(x):
    #y = np.exp(-x)-x
    #y = x**3-7*x**2+14*x-6 #1.a
    y = x**3-2*x**2-5
    y = x**3+3*x**2-1
    return y

def biseccion(a,b,tol,n):

    i=1
    while i < n:
        
        x = (a+b)/2
        print('x:',x)
        if np.abs(Funcion(x)) < tol:
            print("Solucion encontrada")
            return x
        elif Funcion(a)*Funcion(x) > 0: #La raiz esta en [x,b]
            a = x
        else:
            b = x
        print('f(x):',Funcion(x))

        i+=1


#print(biseccion(0,1.2,0.001,10))
print(biseccion(-3,-2,10**-5,100))
