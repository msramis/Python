# SOFÍA RAMIS COMPANY - TERCER EJERCICIO PYTHON

#Programa para saber si un número es par o inpar
#Pedimos un número
n = int(input("Di un numero"))

#Si la división da de residuo 0 entonces el número indicado es par
if (n % 2) == 0:
    print("es par")
#En caso del resto no sea cero entonces el número indicado es inpar
else:
    print("no es par")
