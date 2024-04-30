# "ООП - Объектно-ориентированное программирование"
# "DRY - Don't Repeat Yousels - Не повторяйся "
# Основные консепции - свойства и методы
# class - класс, писать с заглавной буквы, неписанное правило
# Змеиный регистр - разделяют слова с помощью нижнего подчеркивания _, пишется с маленькой буквы  (super_car)
# Верблюжий регистор - отделяются слова заглавной буквой (SuperCar)
# Атрибут класса-свойства(что у него есть), находится вне конструкции def
# Атрибут - это свойства объектов (что есть), находится внутри конструкции def. Динамические данные.
# Метод - те действия, которые они могут совершать.  Метод должен, как-то взаимодействовать с классом. функции внутри классов


class Car: #чертеж или же шаблон
    wheels = 4 # Атрибут/поле/свойства класса
    def __init__(self, model, color):  # self - сам объект.  init - конструктор, собирает.
        self.model = model # Атрибут/поле/свойства объекта
        self.color = color #Всем объектам
        self.is_start = False  #Каждому объекту

    def info(self):
        print(f"Model - {self.model}, color - {self.color}")

    def start(self):
        self.is_start = True
        print(f"Машина {self.model} завелась")

    def drive(self):
        if self.is_start == True:
            print(f"Машина {self.model} поехала")
        else:
            print(f"Машина {self.model} не заведена")

    def stop(self):
        self.is_start = False
        print(f"Машина {self.model} заглушена")

super_car = Car("Mersedes - cls", "black")
super_car_2 = Car("BMW - m5", "white")
# print(super_car.wheels)
# print(super_car.model)
# print(super_car_2.wheels)
# print(super_car_2.model)
super_car.info()
print(super_car.is_start)
super_car.drive()
print(super_car.is_start)
super_car.start()
print(super_car.is_start)
super_car.drive()
super_car.stop()
print(super_car.is_start)
super_car.drive()
super_car_2.info()


# maried = "3 года"
# is_maried = ""    #Bool создаеься с помощью is
