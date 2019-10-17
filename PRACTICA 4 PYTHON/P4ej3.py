# SOFÍA RAMIS COMPANY - CALCULAR AREA TRIANGULO O CUADRADO

pregunta = input("¿Quieres calcular el área de un triángulo o de un cuadrado? ")

if (pregunta == "cuadrado"):
    print("Has elegido cuadrado: ")
    lado_cuadrado = float(input("Dime el tamaño del lado: "))
    area_cuadrado = lado_cuadrado * lado_cuadrado
    print("El área del cuadrado es ", area_cuadrado)

elif (pregunta == "triángulo" or pregunta == "triangulo"):
    print("Has elegido triángulo")
    base_triangulo = float(input("Dime la base del triangulo: "))
    altura_triangulo = float(input("Dime la altura: "))
    area_triangulo = (base_triangulo*altura_triangulo)/2
    print("El área del triangulo es ", area_triangulo)

else:
    print("Error de sintaxis")
                           
    

            
