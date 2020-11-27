# encoding: utf-8
#MÉTODOS NUMERICOS - UNIDAD 3 TAREA 6 - ALVAREZ ARGAÑARAZ EMMANUEL

import numpy as np #Libreria para trabajar más comodamente con matrices en Python
import math #Operaciones basicas

#Operaciones auxiliares
def sumatoria(i): #Sumatoria para el calculo de los Ci
    for j in range(i):
        if j==i:
            continue
        auxs[j] = A[i,j]*xa[j] / A[i,i]

    return sum(auxs)

def norma(): #Calculo de la norma de xs-xa
    for i in range(n):
        auxn[i] = (xs[i]-xa[i])**2

    return math.sqrt(sum(auxn))

n = int(input("Introduzca el orden de la matriz A: ")) #Introduzco la dimensión de la matriz A
tol = float(input("Introduzca la tolerancia del método: ")) #Introduzco la tolerancia para el corte del método
N = int(input("Introduzca el máximo de iteraciones: ")) #Introduzco el número máximo de iteraciones
A = np.zeros([n,n]) #Matriz a introducir, se inicializa con n filas y n columnas llenas de 0
xa = np.zeros([n]) #Vector solución anterior (al principio es el inicial), se inicializa con n elementos con un valor de 0
b = np.zeros([n]) #Vector de términos independientes, se inicializa con n elementos con un valor de 0
xs = np.zeros([n]) #Vector solución siguiente, se inicializa con n elementos con un valor de 0
auxs = np.zeros([n]) #Vector auxiliar para el calculo de la sumatoria, se inicializa con n elementos con un valor de 0
auxn = np.zeros([n]) #Vector auxiliar para el calculo de la norma, se inicializa con n elementos con un valor de 0


#Introduzco los elementos de la matriz A
print("Introduzca los valores de A")
for i in range(n): #Comienza el ciclo
    for j in range(n):
        A[i,j] = input("Elemento a["+str(i+1)+","+str(j+1)+"]: ") #Utilizo esto porque para Python el primer elemento de
        #una matriz es el 0, entonces con ese arreglo el usuario ver que el primer elemento es el 1
        A[i,j] = float(A[i,j]) #Esto es porque el valor a ingresar podria ser un float


#Intruduzco los valores del vector de términos independientes
print("Introduzca los términos independientes")
for i in range(n):
    b[i] = input("Elemento b["+str(i+1)+"]: ") #Explicado más arriba
    b[i] = float(b[i])

#Introduzco los elementos del vector solución inicial
print("Introduzca los valores del vector solución inicial xa")
for i in range(n):
    xa[i] = input("Elemento xa["+str(i+1)+"]: ") #Explicado más arriba
    xa[i] = float(xa[i])

k = 0
while (k < N):
    i = 0
    while (i < n):
        xs[i] = b[i]/A[i,i] - sumatoria(n-1)#Método de Jacobi
        i = i + 1
    if norma() < tol: #Condicion de corte
        print('El vector solucion es:\n', xs)
        print('Cantidad de iteraciones: ', k)
        break
    else:
        i = 0
        for i in range(n):
            xa[i] = xs[i]
        k = k + 1



