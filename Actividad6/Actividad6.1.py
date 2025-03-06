print("Hola Jose Carlos Arangua, ingresa el numero entero")

try:
    n = int(input())
    print("El numero ingresado es: " , n)

    for j in range (n):
        if((n % 2) == 0):
            print("El numero es: ", j)
        else:
            print("El cuadrado del numero es: ", j * j)
except:
    print("La entrada no es un entero")