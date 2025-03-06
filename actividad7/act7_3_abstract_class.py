from abc import ABC, abstractmethod

class AbsNumeros(ABC):
    @abstractmethod
    def print_numeros(self):
        pass

class Racionales(AbsNumeros):
    def __init__(self, n):
        self.n = n

    def print_numeros(self):
        print("El número racional es:", self.n)
        print("El número racional en forma de fracción es:", self.n.as_integer_ratio())