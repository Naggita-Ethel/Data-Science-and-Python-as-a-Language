#OOP Concepts
#A class (A blue print used to create objects)
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def start_engine(self):
        print("Engine started")
    def stop_engine(self):
        print("Engine stopped")
#creating object of Car class
my_car= Car("Toyota", "Corolla", 2000)
print(my_car.make)
print(my_car.model)
print(my_car.year)
my_car.start_engine()
my_car.stop_engine()

#Bank account
class BankAccount:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds to withdraw")
    def dispaly_balance(self):
        print("Account number: ", self.account_no)
        print("Balance", self.balance)
my_acc=BankAccount("1234", 1000)
my_acc.dispaly_balance()
my_acc.deposit(500)
my_acc.withdraw(300)
my_acc.dispaly_balance()

#Perimeter of a rectangle
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def calc_area(self):
        return self.length*self.width
    def calc_perimeter(self):
        return 2*(self.length+self.width)
my_rect=Rectangle(15,5)
print(my_rect.length)
print(my_rect.width)
print("Area of rectangle:", my_rect.calc_area())
print("Perimeter of rectangle:", my_rect.calc_perimeter())        


#Student
class Student:
    def __init__(self, name, year, course):
        self.name = name
        self.year= year
        self.course = course
    def display_details(self):
        print("Name: ", self.name)
        print("Year: " , self.year)
        print("Course: " , self.course)
my_std=Student("Ethel", 2, "BSSE")
my_std.display_details()

#Calculating circumference and area of a  circle
class Circle:
    def __init__(self,radius):
        self.radius = radius
    def calc_area(self):
        return 3.14* self.radius* self.radius
    def calc_circumference(self):
        return 2* 3.14* self.radius
my_circle = Circle(4)
print("Radius of circle: ", my_circle.radius)
print("Area of rectangle: ", my_circle.calc_area())
print("Circumference of circle: ", my_circle.calc_circumference())

#Exercise 1
#Calculate employee's bonus that is 15% of the salary
class Bonus:
    def __init__(self,employee_no, salary):
        self.employee_no = employee_no
        self.salary = salary
    def calc_bonus(self):
        return 0.15*self.salary
emp1 = Bonus(1,150000)
emp2 = Bonus(2,230000)
print("Employee", emp1.employee_no ,"has bonus" , emp1.calc_bonus())
print("Employee", emp2.employee_no, "has bonus", emp2.calc_bonus())

#Encapsulation
class BankAccount:
    def __init__(self, acc_no, balance):
        self._acc_no = acc_no
        self._balance = balance
    def deposit(self,amount):
        self._balance += amount
    def withdraw(self,amount):
        if self._balance>=amount:
            self._balance -= amount
        else:
            print("Insufficient funds")
    def get_balance(self):
        return self._balance
myacc=BankAccount("1234", 1000)
print(myacc._acc_no)
myacc.deposit(500)
print(myacc.get_balance())
#Exercise 2
#convert temperature from celcius(37) to fahrenheit (encapsulation)
class TempConverter:
    def __init__(self, celcius):
        self._celcius = celcius
    def convert(self):
        return (self._celcius*1.8) +32
temp1 = TempConverter(37)
print(temp1.convert())

#Assignment
#Show encapsulation with employee information to give an increament to salary
class Employee:
    def __init__(self, name, oldsalary):
        self._name=name
        self._oldsalary=oldsalary
    def increase(self):
        return (self._oldsalary + 150000)
employee1=Employee("Evelyne", 850000)
employee2=Employee("Eron",600000)
print(employee1._name,"'s salary has been increased from", employee1._oldsalary, "to", employee1.increase())
print(employee2._name,"'s salary has been increased from", employee2._oldsalary, "to", employee2.increase())
        
        