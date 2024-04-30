# Принципы ООП
# Основный принципы ооп. Существует 4 вида. Наследование, Абстракция, Полиморфизм, Инкапсуляция
# Принцип НАСЛЕДОВАНИЯ
# class Parents: #Родитедьский класс
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def info(self):
#         print(f" Имя - {self.name}, Возрасть - {self.age}")

#     def swim(self):
#         print("Я не умею плавать!")


# mom = Parents("Нагима", "30")
# # print(mom.name, mom.age)
# mom.info()
# mom.swim()

# class Children(Parents):  #Дочерний класс
#          #Мы берем экземпляр у родителей/ Значения наследуются с родительского, к детям. Класс, от которого наследуются называется родительским классом. Класс куда наследуется, это дочерний класс.
#     def __init__(self, name, age, property):
#         super(). __init__(name, age)
#         self.property = property

#     def swim(self):
#         print("Я умею плавать!")



# child = Children("Alihan", "15", "0")
# child.info()
# child.swim()

# # Принцип АБСТРАКЦИИ - это принцип, который собирает в один класс обобщенные вещи.
# # Любой абстрактный класс может быть родительским классом, но не каждый родительский класс может быть абстрактным классом.


# class Paople: #Абстрактный класс - Родительский класс
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# # Полиморфизм - при чтении кода, читаются предыдущие коды. Условия должны находится в разных классах 

# def swim(): #функция  # не полиморфизм
#     print("Я не умею плавать!")

# def swim(): #функция # не полиморфизм
#     print("Я умею плавать!")

# swim()

# num = 5    # не полиморфизм
# num = 7 
# print(num)

class Animals:
    def __init__(self, name, eyse):
        self.name = name
        self.eyse = eyse

    def make_sound(self):
        pass
class Dogs(Animals):
    def make_sound(self):
        print("Gaf-Gaf")

class Gats(Animals):
    def make_sound(self):
        print("Meow")

class Fish(Animals):
    def make_sound(self):
        print("Bul-Bul")

dog = Dogs("Шарик", "Карие")
cat = Gats("Мурка", "Зеленые")
fish = Fish ("Немо", "Оранжевый")

dog.make_sound()
cat.make_sound()
fish.make_sound()

# Полиморфизм - метод который выполняет разные действие