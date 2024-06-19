#Escribe un programa que solicite al usuario dos números y determine cuál es mayor o
#si son iguales.
n1= int (input("ingrese el primer numero: "))
n2= int (input ("ingrese el segundo numero: "))
if n1 > n2:
    print('es mayor',n1)
    if n2 < n1:
        print(' es menor',n2)
else:
    print ('son iguales')