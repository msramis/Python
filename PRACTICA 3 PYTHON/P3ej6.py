# SOFÍA RAMIS COMPANY - CALCULAR IVA
IVA = 21
precioproducto = float(input("Dime el precio del producto: "))

producto = input("Nombre del producto: ")

resultadoIVA = (precioproducto*IVA) / 100

resultadofinal= resultadoIVA+precioproducto

print("El precio final del producto es: ", resultadofinal )
