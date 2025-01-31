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
class Dog(self, Animal):
    super().__init__(dog_name)  #  конструктор родительского класса
    self.dog_name =dog_name

    def speak(self):
        print(f"{self.animal_name} Woof")

#У класса Cat метод speak() должен возвращать "Meow"
class Cat(Animal):
    def __init__(self, cat_name):
        self.dog_name = cat_name

    def speak(self):
        print(f"{self.animal_name} Meow")

# Экзкмпляры и использование методов классов
dog = Dog ("Mukhtar")
print (dog, dog.speak(dog))
cat = Cat ("Murzik")
print (cat, cat.speak(cat))