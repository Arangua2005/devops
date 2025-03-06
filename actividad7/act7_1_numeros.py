class Numeros:
    def __init__(self, n): 
        self.n = n 

    def print_Numeros(self): 
        for number in range(self.n):
            if (number % 2) == 0:
                print("El número es:", number)
            else:
                print("El cuadrado del número es:", number ** 2)

class Racionales(Numeros):
    def __init__(self,n):
        super().__init__(n)

    def print_numeros(self):
        # as_intenger_ratio()
        print("El numero racional es: ", self.n)
        print("El numero racional en forma de fraccion es :", self.n.as_integrer_ratio())

    def print_hello(self):
        return "Hello Jose"