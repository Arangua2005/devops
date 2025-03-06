print("Hola Jose Carlos Arangua, ingresa el numero entero")

try:
    n = int(input())
    print("El numero ingresado es ", n)

    for number in range(n):
        print(number)
except:
    print("La entrada no es un entero")

