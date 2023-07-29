#inheritance
class Animal:
    def __init__(self,name):
        self.name=name
    def eat(self):
        print("Animal is eating")
class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)
    def eat(self):
        print(self.name,"is eating.")
    def bark(self):
        print(self.name,"is barking.")
class Cat(Animal):
    def __init__(self,name):
        super().__init__(name)
    def eat(self):
        print(self.name,"is eating.")
    def meow(self):
        print(self.name,"is meowing.")
animal=Animal("Generic animal")
dog=Dog("Spair")
cat= Cat("Cupcake")
animal.eat()
dog.eat()
dog.bark()
cat.eat()
cat.meow()        


class Vehicle:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
    def display_info(self):
        print("Brand:",self.brand)
        print("Color:",self.color)
    def move(self):
        print("Vehicle is moving")
class Car(Vehicle):
    def __init__(self,brand,color,num_wheels):
        super().__init__(brand,color)
        self.num_wheels= num_wheels
    def display_info(self):
        super().display_info()
        print("Number of wheels:",self.num_wheels)
    def honk(self):
        print("Car is honking")
my_car = Car ("Toyota","silver",4)
my_car.color="blue"
my_car.display_info()
my_car.move()
my_car.honk()


#Exercise1: Demonstrate using inheritance to calculate the area and perimeter of a circle and rectangle respectively
class Shape:
    def __init__(self,name):
        self.name=name
class Circle(Shape):
    def __init__(self, name,radius):
        super().__init__(name)
        self.radius=radius
    def calculate_area(self):
        return 3.14*self.radius**2
class Rectangle(Shape):
    def __init__(self, name,length,width):
        super().__init__(name)
        self.length=length
        self.width=width
    def calculate_perimeter(self):
        return 2*(self.length + self.width)
circle1=Circle("circle",4)
rectangle1=Rectangle("rectagle",2,3)
print(circle1.name)
print("Area of circle:",circle1.calculate_area())
print(rectangle1.name)
print("Perimeter of rectangle:",rectangle1.calculate_perimeter())

#multiple inheritance
class Animal:
    def __init__(self, name):
        self.name= name
    def eat(self):
        print(f"{self.name} is eating")
    
class Flyable:
    def fly(self):
        print(f"{self.name} is flying")
class Bird(Animal, Flyable):
    def __init__(self,name,species):
        super().__init__(name)
        self.species=species
    def display_info(self):
        #super().display_info()
        print(f"Species: {self.species}")
        print(f"Name: {self.name}")
my_bird=Bird("pigeon", "bird")
my_bird.display_info()
my_bird.eat()
my_bird.fly()
#Polymorphism(Allows reusability of code by different objects)
#method overriding (occurs when a child class provides its own implementation of a method of a super class)
class Animal:
    def make_sound(self):
        print("Animal is making sound")
class Dog(Animal):
    def make_sound(self):
        print("Dog is barking")
class Cat(Animal):
    def make_sound(self):
        print("Cat is meowing")
animal=Animal()
dog=Dog()
cat=Cat()
animal.make_sound()
dog.make_sound()
cat.make_sound()


#method overloading (occurs when a class has different methods with the same name but different parameters)

class Shape:
    def calc_area(self):
        pass
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length=length
        self.width=width
    def calc_area(self):
        return self.length* self.width
class Circle(Shape):
    def __init__(self, radius):
        self.radius=radius
    def calc_area(self): 
        return 3.14*self.radius**2
    def calc_circum(self):
        return 2*3.14*self.radius
rect= Rectangle(5,5)
circ=Circle(5)
print("Area of rectangle:",rect.calc_area())
print("Area of circle:",circ.calc_area())
print("CIrcumference of circle:",circ.calc_circum())

#Abstraction (shows important methods)
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass
class Car(Vehicle):
    def start(self):
        print("Starting the car")
    def stop(self):
        print("Stopping the car")
class Truck(Vehicle):
    def start(self):
        print("Starting the truck")
    def stop(self):
        print("Stopping the truck")
car=Car()
truck=Truck()
car.start()
car.stop()
truck.start()
truck.stop()

#Exercise2 Demonstrate abstraction using calculating area of a circle and rectangle
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def calc_area(self):
        pass
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length=length
        self.width=width
    def calc_area(self):
        return self.length* self.width
class Circle(Shape):
    def __init__(self, radius):
        self.radius=radius
    def calc_area(self): 
        return 3.14*self.radius**2
rectangle= Rectangle(5,5)
circle=Circle(5)
print("Area of rectangle:",rectangle.calc_area())
print("Area of circle:",circle.calc_area())

#Assignment 1: Create a receipt printing program with GUI
from tkinter import *
from tkinter import ttk
#print method prints the receipt when print button is clicked
def print():
    tott = float(totText.get())
    top = Toplevel()
    #window size
    top.geometry("300x300")
    #window color set to white
    top.config(bg="white")
    #window heading for receipt
    l = Label(top, text='---------RECIEPT----------')
    l.pack()
    l.config(bg="white")
    #columns for the receipt
    heading = Label(top, text='\tItem\tPRICE\tQTY\tTOTAL')
    heading.pack()
    heading.config(bg="white")

    for child in listBox.get_children():
        item = (listBox.item(child, 'values')[0])
        price = float(listBox.item(child, 'values')[1])
        qty = float(listBox.item(child, 'values')[2])
        tot = float(listBox.item(child, 'values')[3])
        item1 = Label(top, text=f'{item}\t{price}\t{qty}\t{tot}')
        item1.config(bg="white")
        item1.pack()

    tot = Label(top, text=f'Total\t{tott}')
    tot.config(bg="white")
    tot.pack()

#show function is called when an item,its price and quantity are added to the treeview by pressing the add button
def show():
    tot = 0
    if (var1.get()):
        #e1 is widget for adding price and e6 is widget for adding quantity
        price = int(e1.get())
        qty = int(e6.get())
        #calculating the total
        tot = int(price * qty)
        tempList = [['Burgers', e1.get(), e6.get(), tot]]
        tempList.sort(key=lambda e: e[1], reverse=True)
        for i, (item, price, qty, tot) in enumerate(tempList, start=1):
            listBox.insert("", "end", values=(item, price, qty, tot))

    if (var2.get()):
        price = int(e2.get())
        qty = int(e7.get())
        tot = int(price * qty)
        tempList = [['Chicken wings', e2.get(), e7.get(), tot]]
        tempList.sort(key=lambda e: e[1], reverse=True)
        for i, (item, price, qty, tot) in enumerate(tempList, start=1):
            listBox.insert("", "end", values=(item, price, qty, tot))

    if (var3.get()):
        price = int(e3.get())
        qty = int(e8.get())
        tot = int(price * qty)
        tempList = [['Soda', e3.get(), e8.get(), tot]]
        tempList.sort(key=lambda e: e[1], reverse=True)
        for i, (item, price, qty, tot) in enumerate(tempList, start=1):
            listBox.insert("", "end", values=(item, price, qty, tot))

    if (var4.get()):
        price = int(e4.get())
        qty = int(e9.get())
        tot = int(price * qty)
        tempList = [['Apples', e4.get(), e9.get(), tot]]
        tempList.sort(key=lambda e: e[1], reverse=True)

        for i, (item, price, qty, tot) in enumerate(tempList, start=1):
            listBox.insert("", "end", values=(item, price, qty, tot))

    if (var5.get()):
        price = int(e5.get())
        qty = int(e10.get())
        tot = int(price * qty)
        tempList = [['Pie', e5.get(), e10.get(), tot]]
        tempList.sort(key=lambda e: e[1], reverse=True)
        for i, (item, price, qty, tot) in enumerate(tempList, start=1):
            listBox.insert("", "end", values=(item, price, qty, tot))
#calculating the final total
    sum1 = 0.0
    for child in listBox.get_children():
        sum1 += float(listBox.item(child, 'values')[3]) #3 because total is in index 3 as the treeview is treated as an array
    totText.set(sum1)

#design
root = Tk()
#title
root.title("Receipt Printing Program")
root.geometry("1000x600")
global e1
global e2
global e3
global e4
global totText
global balText

totText = StringVar()
balText = IntVar()
#heading
Label(root, text="Receipt Printing Program", font="arial 22 bold" ,bg="white").place(x=5, y=10)

#checkboxes for items
var1 = IntVar()
Checkbutton(root, text="Burgers", variable=var1).place(x=10, y=50)

var2 = IntVar()
Checkbutton(root, text="Chicken wings", variable=var2).place(x=10, y=80)

var3 = IntVar()
Checkbutton(root, text="Soda", variable=var3).place(x=10, y=110)

var4 = IntVar()
Checkbutton(root, text="Apples", variable=var4).place(x=10, y=140)

var5 = IntVar()
Checkbutton(root, text=" Pie  ", variable=var5).place(x=10, y=170)
Label(root, text="Total").place(x=600, y=10)

#text boxes for entry of quantity and price
e1 = Entry(root)
e1.place(x=140, y=50)

e2 = Entry(root)
e2.place(x=140, y=80)

e3 = Entry(root)
e3.place(x=140, y=110)

e4 = Entry(root)
e4.place(x=140, y=140)

e5 = Entry(root)
e5.place(x=140, y=170)

e6 = Entry(root)
e6.place(x=300, y=50)

e7 = Entry(root)
e7.place(x=300, y=80)

e8 = Entry(root)
e8.place(x=300, y=110)

e9 = Entry(root)
e9.place(x=300, y=140)

e10 = Entry(root)
e10.place(x=300, y=170)

#Total label for displaying the total before printing the receipt
tot = Label(root, text="", font="arial 22 bold", textvariable=totText)
tot.place(x=650, y=10)
#add button for adding items and their quantities and prices onto the treeview
Button(root, text="Add", command=show, height=3, width=13).place(x=10, y=220)
#printing button for printing the receipt
Button(root, text="Print", command=print, height=3, width=13).place(x=850, y=120)
#treeview for displaying the names,quantities and prices of added items
cols = ('item', 'price', 'qty', 'total')
listBox = ttk.Treeview(root, columns=cols, show='headings')

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=10, y=300)

#calling main function to show the program results
root.mainloop()


