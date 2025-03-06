def printsquare():
    for j in range(n):
        if ((n % 2) == 0):
            print("El numero ingresado es: ", j)
        else:
            print("El cuadrado del numero es: ", j ** 2)
print ("Ingresa un numero entero")
try:
    n = int(input())
    print ("El numero que ingresaste es: ", n) 
    printsquare()          
except:
    print("La entrada no es un entero")
