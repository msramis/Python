# SOFÍA RAMIS COMPANY - MAYOR Y MENOR

print("Acontinuación pediremos 5 números...")
num1 = int(input("Dime el 1º número: "))
num2 = int(input("Dime el 2º número: "))
num3 = int(input("Dime el 3º número: "))
num4 = int(input("Dime el 4º número: "))
num5 = int(input("Dime el 5º número: "))

print("Los números introducidos son", num1 , num2 , num3 , num4 , num5)

if num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5:
    print("El numero 1 es el mayor de los 5 números")

elif num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5:
    print("El numero 2 es el mayor de los 5 números")

elif num3 > num1 and num3 > num2 and num3 > num4 and num3 > num5:
    print("El numero 3 es el mayor de los 5 números")

elif num4 > num1 and num4 > num2 and num4 > num3 and num4 > num5:
    print("El numero 4 es el mayor de los 5 números")

elif num5 > num1 and num5 > num2 and num5 > num3 and num5 > num4:
    print("El numero 5 es el mayor de los 5 números")

if num1 < num2 and num1 < num3 and num1 < num4 and num1 < num5:
    print("El numero 1 es el menor de los 5 números")

elif num2 < num1 and num2 < num3 and num2 < num4 and num2 < num5:
    print("El numero 2 es el menor de los 5 números")

elif num3 < num1 and num3 < num2 and num3 < num4 and num3 < num5:
    print("El numero 3 es el menor de los 5 números")

elif num4 < num1 and num4 < num2 and num4 < num3 and num4 < num5:
    print("El numero 4 es el menor de los 5 números")

elif num5 < num1 and num5 < num2 and num5 < num3 and num5 < num4:
    print("El numero 5 es el menor de los 5 números")
    
elif num1 == num2 and num2 == num3 and num3 == num4 and num4 == num5:
    print("Todos los números son iguales, no repitas números")
else:
    print("Números repetidos")
    
