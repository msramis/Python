# SOFÍA RAMIS COMPANY - VALIDAR FECHAS

#Pedimos día, mes y año
dia = int(input("Introduzca un dia: "))
mes = int(input("Introduzca un mes: "))
año = int(input("Introduzca un año: "))

#si dia es mayor de 31 está mal
if (dia > 31):
    print("El día no es correcto")
    
#si mes es mayor es mayor de 12 está mal
elif (mes > 12):
    print("El mes no es correcto")
    
#si el año es menor de 0 está mal
elif (año < 0):
    print("El año no es correcto")


