# Lab10
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

# Example of class usage
student = Student(name="Ivan", age=30, grade="2")
print("Student Name:", student.name)
print("Student Age:", student.age)
print("Student Grade:", student.grade)
Клас Student: Цей клас має три атрибути: name, age і grade. Вони ініціалізуються у методі __init__, який викликається автоматично при створенні нового об'єкта цього класу.

Конструктор __init__: Приймає три параметри name, age і grade і призначає їх до відповідних атрибутів об'єкта (self.name, self.age, self.grade).

Створення екземпляра класу: student = Student(name="Ivan", age=30, grade="2") створює новий об'єкт типу Student з конкретними значеннями атрибутів.

Доступ до атрибутів: student.name, student.age і student.grade дозволяють отримати доступ до значень цих атрибутів для конкретного екземпляра класу.

Приклад 2: Клас Student з методом display_info

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

# Example of class usage
student = Student(name="Ivan", age=30, grade="2")
print(student.display_info())  # Output: Name: Ivan, Age: 30, Grade: 2
Метод display_info: Цей метод визначений у класі Student. Він повертає рядок, який містить інформацію про ім'я, вік і оцінку студента.

Використання методу: print(student.display_info()) викликає метод display_info для об'єкта student і виводить рядок з інформацією про студента на екран.

Приклад 3: Клас Animal і його підклас Dog

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        return f"{self.name}: {self.sound}"


class Dog(Animal):
    def __init__(self, name, sound, breed):
        super().__init__(name, sound)
        self.breed = breed

# Example of class usage
animal = Animal(name="Lala", sound="")
dog = Dog(name="Lala", sound="Auuuuuuu", breed="Spitz")
print(animal.make_sound())  # Output: Lala:
print(dog.make_sound())  # Output: Lala: Auuuuuuu
Клас Animal: Визначає базовий клас Animal з атрибутами name і sound і методом make_sound, який повертає рядок зі звуком тварини.

Підклас Dog: Наслідує клас Animal. Має додатковий атрибут breed. Конструктор підкласу Dog використовує super() для ініціалізації атрибутів з базового класу Animal.

Створення об'єктів: animal = Animal(name="Lala", sound="") і dog = Dog(name="Lala", sound="Auuuuuuu", breed="Spitz") створюють об'єкти класів Animal і Dog відповідно.

Виклик методів: print(animal.make_sound()) і print(dog.make_sound()) демонструють, як методи можна викликати для об'єктів базового класу і його підкласу, повертаючи різні результати.

Приклад 4: Класи Bird, Sparrow і Penguin

class Bird:
    def fly(self):
        return None

class Sparrow(Bird):
    def fly(self):
        return "Sparrow flies high"

class Penguin(Bird):
    def fly(self):
        return "Penguin cannot fly"

# Example of class usage
bird = Bird()
sparrow = Sparrow()
penguin = Penguin()
print(bird.fly())  # Output: None
print(sparrow.fly())  # Output: Sparrow flies high
print(penguin.fly())  # Output: Penguin cannot fly
Клас Bird: Визначає базовий клас Bird з методом fly, який за замовчуванням повертає None.

Підкласи Sparrow і Penguin: Наслідують клас Bird і перевизначають метод fly для різних типів птахів.

Поведінка методів: Об'єкти bird, sparrow і penguin викликають метод fly, який повертає різні значення відповідно до типу птаха.

Приклад 5: Клас Encapsulation з різними рівнями доступу

class Encapsulation:
    def __init__(self, public, _private, __protected):
        self.public = public
        self._private = _private
        self.__protected = __protected

# Example of class usage
obj = Encapsulation(1, 2, 3)
print(obj.public)  # Output: 1
print(obj._private)  # Output: 2
print(obj._Encapsulation__protected)  # Output: 3
print(obj._Encapsulation__protected)  # Output: 3
Клас Encapsulation: Має три атрибути з різними рівнями доступу: public, _private і __protected.

Доступ до атрибутів: Атрибут public доступний для зовнішнього використання без обмежень. Атрибут _private є "приватним", але в Python це не справжній приватний доступ. Атрибут __protected має "захищений" доступ, який зазвичай не використовується прямо.

Демонстрація доступу: Об'єкт obj створюється з конкретними значеннями для атрибутів. Виклики print(obj.public), print(obj._private), print(obj._Encapsulation__protected) показують рівні доступу до цих атрибутів.

Приклад 6: Клас Rectangle з методом calculate_perimeter

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height
