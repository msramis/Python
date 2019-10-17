# SOFÍA RAMIS COMPANY - NUMERO MÁXIMO DE 3 CIFRAS

#Pedimos un numero de tres cifras
n = input("Dime un número de tres cifras máximo: ")

#validamos que el número introducido no sea mayor que 3 cifras
if (len(n) > 3):
        print ("El número solo puede tener tres cifras")

#si el numero es menor de tres cifras estará correcto
else:
    print("Has introducido el número correctamente")
