#abstraccion y clase abstraccion
from abc import ABC, abstractmethod

class absNumeros(ABC):
    @abstractmethod
    def print_numeros(self):
        pass

class Racionales(absNumeros):
    
    def __init__(self,n):
        self.n = n
    
    def print_numeros(self):
        print("El numero racionales: ", self.n)
        print("El numero racional en forma de fraccion es: ", self.n.as_integer_ratio())

    def print_hello(self):
        return "Hello Jose"
    