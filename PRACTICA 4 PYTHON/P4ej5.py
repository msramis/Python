# SOFÍA RAMIS COMPANY - CAJERO AUTOMÁTICO


i = int(input("Ingrese importe: "))
if(i%500 == 0):
        b = i/500
        print("El cajero de devuelve %d de 500 euros" % b)
elif(i%200 == 0):
        b = i/200
        print("El cajero de devuelve %d de 200 euros" % b)
elif(i%100 == 0):
        b = i/100
        print("El cajero de devuelve %d de 100 euros" % b)
elif(i%50 == 0):
        b = i/50
        print("El cajero de devuelve %d de 50 euros" % b)
elif(i%20 == 0):
        b = i/20
        print("El cajero de devuelve %d de 20 euros" % b)
elif(i%10 == 0):
        b = i/10
        print("El cajero de devuelve %d de 10 euros"% b)
elif(i%5 == 0):
        b = i/5
        print("El cajero de devuelve %d de 5 euros" % b)
        
