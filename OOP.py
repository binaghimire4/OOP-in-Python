#Inheritance and Polymorphism
class school:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        
    def display(self):
        print(f"school name: {self.name}, location: {self.location}")
        
s = school("sajah", "ktm")
s.display()

class teacher(school):
    def __init__(self, name, location, subject):
        super().__init__(name, location)
        self.subject = subject
        
    def display(self):
        
        print(f"school's name {self.name}, {self.location} and subject: {self.subject}")
        
t = teacher("sajah", "ktm", "math")
t.display()

#Abstract Base Classes
from abc import ABC, abstractmethod
class student(ABC):
    @abstractmethod
    def __init__(self):
        pass
class employee(student):
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def display(self):
        print(f"employee name: {self.name}, id: {self.id}")
e = employee("sajah", 101)
e.display()

from abc import ABC, abstractmethod
class payment(ABC):
    def __init__(self, amount):
        self.amount = amount
        
    @abstractmethod
    def show(self):
        pass
    
class cash(payment):
    def __init__(self, amount, currency):
        super().__init__(amount)
        self.currency = currency
            
    def show(self):
        print(f"Payment amount: {self.amount} {self.currency}")

class card(payment):
    def __init__(self, amount,currency, card_type):
        super().__init__(amount)
        self.currency = currency
        self.card_type = card_type
    def show(self):
        print(f"Payment amount: {self.amount} {self.currency} using {self.card_type} card")
   
C= card("20000", "Nepali","visa")
C.show()

#Encapsulation in Python
class BankAccount:
    def __init__(self, __amount):
        self.__amount = __amount
    
    def get(self):
        return self.__amount
    
    def set(self, amount):
        if self.__amount > 0:
            self.__amount += amount
        else:
            print("Invalid amount")
    
class deposite(BankAccount):
    def __init__(self, __amount, deposite_amount):
        super().__init__(__amount)
        self.deposite_amount = deposite_amount
    def total_amount(self):
        self.set(self.deposite_amount)
        print(f"Total amount before deposite{self.deposite_amount}")
        print(f"Total amount after deposite: {self.deposite_amount}")
account = deposite(10000, 5000)
account.total_amount()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    def get(self):
        return self.__age
    
    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("Invalid age")
S = Person("kalu", 0)
S.set_age(12)
print(f"name:{S.name}, age:{S.get()}")

#Mangling Method for Private Attributes

class Vehicle:
    def __init__(self, model):
        self.__model = model
    
p = Vehicle("Toyota")
print(p._Vehicle__model)


class Book:
    def __init__(self, title, author):
        self.title = title
        self.__author = author

b = Book("Python Programming", "John Doe")
print(b.title)
print(b._Book__author)

#inner class 

class outer:
    def __init__(self):
        self.name = "outer class"
    def display(self):
        print("this is outer class")
    class inner:
        def __init__(self):
            self.name = "inner class"
        def display(self):
            print("this is inner class")
o = outer()
o.display()
i = o.inner()
i.display()


class A:
    def rk(self):
        print("In class A")

class B:
    def rk(self):
        print("In class B")

# classes ordering
class C(A, B):
    def __init__(self):
        print("Constructor C")

r = C()

# # it prints the lookup order 
# #rint(C.__mro__)
# print(C.mro())

# Python program showing
# how MRO works

class A:
    def rk(self):
        print("In class A")

class B(A):
    def rk(self):
        print("In class B")

r = A()
r.rk()


#Method overloading

class addition:
    def add(self, a, b):
        return a + b
A = addition()
print(A.add(2, 3))
print(A.add("Hello", " World"))
print(A.add([1, 2], [3, 4]))

#Method overriding
class Parent:
    def show(self):
        print("Parent class method")
class Child(Parent):
    def show(self):
        print("Child class method")
p = Parent()
p.show()