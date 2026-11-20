# class Student:
#     name = "Sneha"
#     age=22
# stud1=Student()
# stud2=Student()
# print(stud1.name)
# print(stud1.age)
# print(stud2.name)

# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def display_details(self):
#         print(self.name)
#         print(self.age)
# stud1=Student("Sruthi",27)
# stud1.display_details()


# class Area:
#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth=breadth
#     def display(self):
#         area=self.length*self.breadth
#         return area
# a=Area(4,5)
# print(a.display())

# class Area:
#     l=5
#     b=3
#     def display(l,b):
#         area=l*b
#         return area
# a1=Area()
# print(a1.l)
# print(a1.b)

# class Human:
#     count=0
#     @classmethod
#     def class_method(cls):
#         cls.count+=1
# Human.class_method()
# Human.class_method()
# print(Human.count)

# class Student:
#     @staticmethod
#     def display(name,age):
#         print(f"{name} {age}")
# Student.display("sruthi",27)

# class Student:
#     name =  "malavika"
#     age = 27
#     marks = 90
#     def marks_update(self,newmark):
#         self.marks=newmark
#         return self.marks
#     def display(self):
#         print(f" {self.name} : {self.age} : {self.marks} ")
# stud=Student()
# stud.marks_update(88)
# stud.display()

# class Bank:
#     balance=0
#     amount=0
#     def __init__(self,amount):
#         self.balance+=amount
    
#     def deposit(self,amount):
#         self.balance+=amount
#         print(f"Deposited {amount}")
#     def withdraw(self,amount):
#         if amount>self.balance:
#             print("Insufficient balance")
#         else:
#             self.balance-=amount
#             print(f"Now the balance is {self.balance}")
#     def check_balance(self):
#         print(self.balance)
# b=Bank(10000)
# b.deposit(500)
# b.check_balance()
# b.withdraw(200)
# b.check_balance()

# class Rectangle:
#     def __init__(self,l,b):
#         self.l=l
#         self.b=b
#     def calc_area(self):
#         area=self.l*self.b
#         return area
#     def calc_perimeter(self):
#         p=2*(self.l + self.b)
#         return p
# r=Rectangle(4,5)
# print(r.calc_area())
# print(r.calc_perimeter())


# class Car:
#     def __init__(self,brand,model,mileage):
#         self.brand=brand
#         self.model=model
#         self.mileage=mileage
    
#     def update_mileage(self,newmileage):
#         self.mileage=newmileage
#         print(f"Updated mileage {self.mileage}")
#     def display(self):
#         print(f"{self.brand} : {self.model} : {self.mileage}")

# c=Car("Tata","Nexon",12500)
# c.display()
# c.update_mileage(13200)
# c.display()

# class Employee:
#     def __init__(self,base_salary):
#         self.base_salary=base_salary
#         self.bonus=0
#         self.deduction=0
    
#     def add_bonus(self,amount):
#         self.base_salary+=amount
#         print(f"Bonus of {amount}")
#     def add_deduction(self,amount):
#             self.base_salary-=amount
#             print(f"Deduction of {amount}")
#     def net_salary(self):
#         return (self.base_salary+self.bonus)-self.deduction
# e=Employee(10000)
# e.add_bonus(500)
# print(e.net_salary())
# e.add_deduction(400)
# print(e.net_salary())

class Temperature:
    @staticmethod
    def calc_f(celsius):
        return celsius * 9 / 5 + 32
    @staticmethod
    def calc_c(farenheit):
        return (farenheit - 32)  * 5 / 9
t1=30
print(Temperature.calc_f(t1))
t2=98.6
print(Temperature.calc_c(t2))






        
    