# Экземпляры класса(объекта) - 
# Объект - это и есть экземпляр. Экземпляры объектов, созданные по шаблону класса. 
# Инкапсуляция - это один из принципов ООП. Это защита lанных. В чем проявляется? Может поставить защиту. 
# Публичный, защищенный и приватный.  Абстракция бывает Публичный, защищенный и приватный

class Laptops:
    def __init__(self, model, os, memory):
        self.model = model # Публичный атрибут
        self._os = os #Защищенный атрибут (_)
        self.__memory = memory #Приватный атрибут (__а)

    @ property   #Декоратор-@, Используется для приватного атрибута, чтобы сделать его публичным.
    def memory(self):
        return self.__memory

    def info(self): #Публичный
        print(f"model - {self.model}, {self._os}")
        # huawei._desktop()
        self._desktop()
        self.__password()

    def _desktop(self):  #Защищеный
        print("Рабочий стол")

    def __password(self): # Приватный 
        print("password = 1234") 

    @property
    def password(self):
        return self.__password

huawei = Laptops("Huawei", "Windows 11", 512)

print(huawei.model)
print(huawei._os)
print(huawei.memory)
print(huawei.memory)
huawei.info()
# huawei._desktop()
huawei.password()

# import time
# def users(value):
#     def start():
#         print("Hello world!")
#         time.sleep(2)
#         print("H!")
#         time.sleep(2)
#         print("e!")
#         time.sleep(2)
#         print("l!")
#         time.sleep(2)
#         print("l!")
#         time.sleep(2)
#         print("o!")
#         value()
#         print("Bye!")
#     return start

# @users
# def say():
#     print("Hi!")
# say()

# Множествненное наследование

class Father:
    def __init__(self, name, age, beard):
        self.name = name
        self.age = age
        self.beard = beard

    def work(self):
        print("Работать!")

class Mother:
    def __init__(self, name, age, manik):
        self.name = name
        self.age = age
        self.manik = manik

    def cook(self):
        print("Готовка!")

class Child(Father, Mother):
    def __init__(self, name, age, beard, manik, toys):
        Father.__init__(self, name, age, beard)
        Mother.__init__(self, name, age, manik)
        self.toys = toys

    

    def cook(self):
        print("Я не умею готовить!")

david =  Child("David", 15, "Черная борода", "Розовый маникюр", "Много игрушек")
david.work()
david.cook()