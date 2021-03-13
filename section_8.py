# ---------------------------------------- Attributes and Class Keyword ----------------------------------------
# class Dog():
#     def __init__(self, mybreed, name, spots):
#         # attributes
#         # we take in the argument
#         # assign it using self.attribute_name
#         self.my_attribute = mybreed
#         self.name = name

#         # expect boolean true/false
#         self.spots = spots

# my_dog = Dog(mybreed='Huskie', name='Sammy', spots=False)
# print(my_dog.my_attribute, my_dog.name, my_dog.spots)
# print(type(my_dog))

# ---------------------------------------- Class Object Atributes and Methods ----------------------------------------
# class Dog():
#     # class object attribute
#     # same for any instance of a class
#     species = 'mammal'

#     def __init__(self, mybreed, name, spots):
#         # attributes
#         # we take in the argument
#         # assign it using self.attribute_name
#         self.my_attribute = mybreed
#         self.name = name

#         # expect boolean true/false
#         self.spots = spots
    
#     # operations/actions ---> methods
#     def bark(self, number):
#         print("Woof! My name is {} and the number is {}".format(self.name, number))

# my_dog = Dog(mybreed='Lab', name='Sam', spots=False)
# print(my_dog.my_attribute, my_dog.name, my_dog.spots, my_dog.species)
# print(type(my_dog))
# my_dog.bark(5)

# class Circle():
#     # class objec attribute
#     pi = 3.14

#     def __init__(self, radius=1):
#         self.radius = radius
#         self.area = radius*radius*Circle.pi
    
#     # method
#     def get_circumference(self):
#         return self.radius * self.pi * 2

# my_circle = Circle(30)
# print(my_circle.pi)
# print(my_circle.radius)
# print(my_circle.get_circumference())
# print(my_circle.area)

# ---------------------------------------- Inheritance and Polymorphism ----------------------------------------
# class Animal():
#     def __init__(self):
#         print("Animal created")
    
#     def who_am_i(self):
#         print("I am an animal")
    
#     def eat(self):
#         print("I am eating")

# class Dog(Animal):
#     def __init__(self):
#         Animal.__init__(self)
#         print("Dog Created")
    
#     # overwrites from animal
#     def who_am_i(self):
#         print("I am a dog!")
    
#     def eat(self):
#         print("I am dog eating")
    
#     def bark(self):
#         print("Woof!")

# mydog = Dog()
# mydog.who_am_i()
# mydog.eat()
# mydog.bark()

# class Dog():
#     def __init__(self, name):
#         self.name = name
    
#     def speak(self):
#         return self.name + " says woof!"

# class Cat():
#     def __init__(self, name):
#         self.name = name
    
#     def speak(self):
#         return self.name + " says meow!"

# niko = Dog("niko")
# felix = Cat("felix")

# print(niko.speak())
# print(felix.speak())

# for pet in [niko, felix]:
#     print(type(pet))
#     print(pet.speak())

# def pet_speak(pet):
#     print(pet.speak())

# pet_speak(niko)
# pet_speak(felix)

# class Animal():
#     def __init__(self, name):
#         self.name = name
    
#     def speak(self):
#         raise NotImplementedError("Subclass must implement this abstract method")

# class Dog(Animal):
#     def speak(self):
#         return self.name + " says woof!"

# class Cat(Animal):
#     def speak(self):
#         return self.name + " says meow!"

# fido = Dog("Fido")
# baby = Cat("Baby")
# print(fido.speak())
# print(baby.speak())

# ---------------------------------------- Special Methods ----------------------------------------
# class Book():
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages

#     def __str__(self):
#         return f"{self.title} by {self.author}"
    
#     def __len__(self):
#         return self.pages
    
#     def __del__(self):
#         print("A book object has been deleted")

# b = Book('Python rocks', 'Jose', 200)
# print(b)
# print(len(b))
# del(b)

# ---------------------------------------- Homework ----------------------------------------
# class Line:
#     def __init__(self, coor1, coor2):
#         self.coor1 = coor1
#         self.coor2 = coor2
    
#     def distance(self):
#         x1,y1 = self.coor1
#         x2,y2 = self.coor2
#         return ((x2-x1)**2 + (y2-y1)**2)**0.5
    
#     def slope(self):
#         x1,y1 = self.coor1
#         x2,y2 = self.coor2

#         return (y2-y1) / (x2-x1)

# c1 = (3,2)
# c2 = (8,10)
# myline = Line(c1,c2)
# print(myline.distance())
# print(myline.slope())

# class Cylinder:
#     def __init__(self, height=1, radius=1):
#         self.height = height
#         self.radius = radius

#     def volume(self):
#         return self.height * 3.14 * (self.radius)**2
    
#     def surface_area(self):
#         top = 3.14 * (self.radius**2)
#         return (2*top) + (2*3.14*self.radius*self.height)

# mycyl = Cylinder(2,3)
# print(mycyl.volume())
# print(mycyl.surface_area())

# ---------------------------------------- Challenge ----------------------------------------
class Account():
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, dep_amt):
        self.balance = self.balance + dep_amt
        print(f"Added {dep_amt} to balance")
    
    def withdrawal(self, wd_amt):
        if self.balance >= wd_amt:
            self.balance = self.balance - wd_amt
            print("Withdrawal accepted")
        else:
            print("Sorry, not enough funds!")
    
    def __str__(self):
        return f"Owner: {self.owner} \nBalance: {self.balance}"
    
a = Account("Kyle", 500)
print(a.owner)
print(a.balance)
a.deposit(100)
print(a.balance)
a.withdrawal(600)
print(a.balance)
a.withdrawal(100)