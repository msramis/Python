# SOFÍA RAMIS COMPANY - CRECIENTE, DECRECIENTE O DESORDENADOS

import time
print("Acontinuación pediremos 5 números y diremos en qué orden estan...")
num1 = int(input("Dime el 1º número: "))
num2 = int(input("Dime el 2º número: "))
num3 = int(input("Dime el 3º número: "))
num4 = int(input("Dime el 4º número: "))
num5 = int(input("Dime el 5º número: "))

print("Los números introducidos son", num1 , num2 , num3 , num4 , num5)
print("Ahora verficaremos si el orden es decreciente, creciente o desordenado")
#Ponemos un tiempo de espera de un segundo con time.sleep
time.sleep(1)
if num1 < num2 and num2 < num3 and num3 < num4 and num4 < num5:
    print("El orden es creciente")
elif num1 > num2 and num2 > num3 and num3 > num4 and num4 > num5:
    print("El orden es decreciente")
else:

    print("Los números estan desordenados")
