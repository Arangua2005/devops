class Numeros:
    def __init__(self,n):
        self.n = n
    def print_numbers(self):
        for j in range(self.n):
            if((self.n%2)==0):
                print("El numero es: ", j)
            else:
                print("El cuadrado del numero es: ", j**2)

class Racionales(Numeros):
    def __init__(self,n):
        super().__init__(n)

    def print_numeros(self):
        # as_intenger_ratin()
        print("El numero racionales: ", self.n)
        print("El numero racional en forma de fraccion es: ", self.n.as_integer_ratio())
