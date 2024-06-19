#task 1
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

#task 2
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

#task 3
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


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


# Example of class usage
rectangle = Rectangle(width=5, height=4)
print(rectangle.calculate_perimeter())  # Output: 18


class AverageCalculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate_average(self):
        if not self.numbers:
            return 0
        return sum(self.numbers) / len(self.numbers)


# Example of class usage
numbers = [5, 10, 15, 20]
avg_calculator = AverageCalculator(numbers)
print(avg_calculator.calculate_average())  # Output: 12.5
