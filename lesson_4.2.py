# Магические методы
# dunder (double underscore) - это магический метод

from typing import Any


class ElectroCar:
    def __init__(self, power, battery):
        self.power = power
        self.battery = battery

    def info(self, value):
        print(f"Мощность - {self.power} Vat\nЗаряд батерии- {self.battery} Mhc - {value}")

    def add(self, a, b):
        print(a+b)

    def __repr__(self):  #__repr__ == print
        return f"Мощность - {self.power} Vat\nЗаряд батерии- {self.battery} Mhc - это метод repr"  # Работает без car.info? заменили
        
    def __str__(self):  #__str__ == print
        return f"Мощность - {self.power} Vat\nЗаряд батерии- {self.battery} Mhc - это медот str" # str- главнее. так же он влияет на свет принта, это магический метод

    def __call__(self):  # K call Мы обращаемся как к функции (car())
        print("Hello world!")
 
    def __call__(self, a, b):
        print(a+b) 

    "Магические действия для арифметических действий"
    def __add__(self, other):  #__add__ = +
        new_power = self.power + other.power 
        return ElectroCar(new_power, self.battery)
    

    def __sub__(self, other):  #__sub__ = -
        new_power = self.power - other.power 
        return ElectroCar(new_power, self.battery)
    
    def __mul__(self, other):  #__mul__ = *
        new_power = self.power + other.power 
        return ElectroCar(new_power, self.battery)
    
    def __truediv__(self, other):  #__mul__ = /  truediv - это деление с остатком
        new_power = self.power / other.power 
        return ElectroCar(new_power, self.battery)
    
    def __floordiv__(self, other):  #__mul__ = /  floorediv - это деление без остатком
        new_power = self.power // other.power 
        return ElectroCar(new_power, self.battery)
    
    "Магичисике действия для сравнения"

    def __gt__(self, other): #> - Больше, чем
        return self.battery > other.battery 

    def __lt__(self, other): #< - Меньше, чем
        return self.battery > other.battery 
    
    def __eq__(self, other): # == 
        return self.battery == other.battery 


    def __ne__(self, other): # != 
        return self.battery != other.battery

    def __ge__(self, other): # >= 
        return self.battery >= other.battery
    
    def __le__(self, other): # <= 
        return self.battery <= other.battery


car = ElectroCar(120, 2000)
car_2 = ElectroCar(120, 2000)
# car.info(12)
# car.add(1, 2)
print(car)
car(3, 5)
print(car + car_2)
print(car - car_2)
print(car * car_2)
print(car / car_2)
print(car // car_2)
    
    #  "Магичисике действия для сравнения"

print(car > car_2)
print(car < car_2)
print(car == car_2)
print(car != car_2)
print(car >= car_2)
print(car <= car_2)
