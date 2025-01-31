# Инкапсуляция
#Создайте класс Person, который будет представлять человека
#У класса должен быть приватный атрибут _age (возраст).
class Person:
    def __inint__(self, name):
        self.name = name
        """ создает возраст, по умолчанию =0 """
        self._age=0

# Создайте методы для установки (set_age(age)) и получения (get_age()) возраста
    def get_age(self):
        """ возвращает текущий возраст человека """
        return self._age
    print(1)
    def set_age(self, age):
        """ устанавливает возраст при условии"""
        if age < 0:
            print("возраст не может быть отрицательным")
        else:
            self._age = age
# Пример использования
p = Person()
p.set_age(25)
print(p.get_age())  # Вывод: 25
p.set_age(-5)  # Вывод: Ошибка: возраст не может быть отрицательным.
print(p.get_age()) # Вывод: 25 (возраст не изменился)

# Наследование
# Создайте класс Animal и два наследника: Dog и Cat

# У класса Animal должен быть атрибут name и метод speak(), который возвращает строку "I am an animal"
class Animal:
    def __init__(self,animal_name):
       self.animal_name = animal_name

    def speak(self):
        print(f"{self.animal_name} I am an animal")

#У класса Dog метод speak() должен возвращать "Woof".
class Dog(Animal):
    def __init__(self, animal_name):
        super().__init__(animal_name)  #  конструктор родительского класса

    def speak(self):
        print(f"{self.animal_name} Woof")

#У класса Cat метод speak() должен возвращать "Meow"
class Cat(Animal):
    def __init__(self, animal_name):
        super().__init__(animal_name)

    def speak(self):
        print(f"{self.animal_name} Meow")

# Экземпляры и использование методов классов
dog = Dog ("Buddy")
dog.speak()
cat = Cat ("Kitty")
cat.speak()

# Полиморфизм
# Создайте несколько классов, которые будут представлять разные виды транспорта,
# и функцию move(vehicle), которая вызывает общий метод move() у переданного объекта

# Создайте базовый класс Vehicle с методом move(), который возвращает строку "Vehicle is moving"

class Vehicle:
    def __init__(self, vehicle_name):
        self.vehicle_name = vehicle_name

    def move(self):
        return print ("Vehicle is moving")

#Создайте два дочерних класса Car и Bicycle, которые переопределяют метод move().
#- У Car метод возвращает "Car is driving".
# У Bicycle метод возвращает "Bicycle is pedaling"

class Car(Vehicle):
    def __init__(self, vehicle_name):
        super().__init__(vehicle_name)

    def move(self):
        return print ("Car is driving")

class Bicycle(Vehicle):
    def __init__(self, vehicle_name):
        super().__init__(vehicle_name)

    def move(self):
        return print ("Bycycle is pedaling")

# Напишите функцию move(vehicle), которая принимает объект и вызывает у него метод move()
# пример использования car = Car() bike = Bicycle()

car = Car("Toyota")
car.move()
bike = Bicycle("Bike")
bike.move()

# Абстракция
#Создайте абстрактный класс Shape с методом area() и
# конкретные классы-наследники для вычисления площади разных фигур.
#Абстрактный класс Shape должен иметь метод area(), который
# не реализован (используйте модуль abc).

#Реализуйте два наследника Rectangle, принимающий ширину и высоту. Circle, принимающий радиус.

# Метод area() унаследованных классов должен вычислять площадь.


# Пример использования:
#       rect = Rectangle(10, 5)
#       circle = Circle(7)

