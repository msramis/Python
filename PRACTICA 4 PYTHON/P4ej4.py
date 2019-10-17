# SOFÍA RAMIS COMPANY - DIVISOR O NO DIVISOR

print("Acontinuación preguntaremos 4 números")
num1 = int(input("Dime el 1º número"))
num2 = int(input("Dime el 2º número"))
num3 = int(input("Dime el 3º número"))
num4 = int(input("Dime el 4º número"))

# si los tres números son divisibles por el cuarto número entonces
# num4 es divisibles de los demás
if (num1 % num4) == 0 and (num2 % num4) == 0 and (num3 % num4) == 0:
    print("El número cuatro es divisor de los demás números")
#si no son divisisbles por num4 entonces no es divisible
else:
    print("No es divisible")
