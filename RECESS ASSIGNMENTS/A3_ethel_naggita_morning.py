#Operators
#Arithmetic operators
print("Arithmetic operators")
#Addition
a=60+ 40
print(a)
#Subtraction
b=60 - 40
print(b)
#Multiplication
c = 6 * 4
print(c)
#Divison
d=60 / 4
print(d)
#Modulus
e = 50 % 3
print(e)
#divide (returns exponential without remainder)
f = 50//3
print(f)
#exponential
g=2**4
print(g)
#Comparision operators
print("Comparision operators")
a=50
b=10
#greater than
if a>b:
    print("a is greater than b")
    print(a>b)
#less than
if a<b:
    print("a is less than b")
    print(a<b)
#greater than or equal
if a>=b:
    print("a is greater than or equal to b")
    print(a>=b)
#less than or equal
if a<=b:
    print("a is less than or equal to b")
    print(a<=b)
#equal to
if a==b:
    print("a is equal to b")
    print(a==b)
#not equal to
if a!=b:
    print("a is not equal to b")
    print(a!=b)
#Logical operators
print("Logical operators")
#logical AND
x=True
y=False
print(x and y)
print(not x and not y)
#logical OR
print(x or y)
#logical NOT
print(not x)
print(not y)
#Assignment operators
print("Assignment operators")
#compound assignment operators
#assign
r=5
#add and assign
r+=5
print(r)
#subtract and assign
h=20
h-=20
print(h)
#exponential and assign
i=2
i**=4
print(i)
#multiply and assign
j=2
j*=4
print(j)
#divide and assign
k=10
k/=5
print(k)
#modulus and assign
l=50
l%=3
print(l)

#Membership assignment operators
print("Membership operators")
cars=["legacy", "wish", "vitz"]
if "legacy" in cars:
    print("Legacy is in cars")
print("vitz" in cars)
print("fortuner" in cars)
#Identity operators
print("Identity operators")
m="class"
n="class"
print(m is y)
print(m is not y)
print(m==n)
print(m!=n)
print(m<=n)
p=[1,2,3,4,5]
q=[1,2,3,4,5]
print(p is q)
print(p is not q)

#Bitwise operators (used to perform operations on individual bits in binary numbers)
print("Bitwise operators")
#Bitwise AND (returns 1 if both bits are 1 otherwise 0)
s=10  #....0000 1010 (32 bits)
t=4   #....0000 0100
print(s & t)
#biteise OR (returns 1 if one of the bits is 1 otherwise 0)
print(s|t)  #1110 =14
#bitwise XOR (returns 1 if one of the bits is 1 and the other 0 otherwise 0)
print(s^t)  #1110=14
#bitwise NOT (returns the interchanged version of bits)
print(~s) 
#bitwise right shift (shifts bits to the right and fills the void witha zero, if number is negative,void is filled with 1. equivalet to dividing number by 2)
print(s>>1) #.....0000 1010 then 0000 0101 = 5
v=-10
print(v>>1) #.....1111 0110 then 1111 1011 =-5
#bitwise left shift 
w=5
print(w<<1) #.....0000 0101 then 0000 1010 =10
print(w<<2)
x=-10
print(x<<1) #.....1111 0110 then 1110 1100=-20
print(x<<2) #.....1101 1000 =-40
#a simple calculator
print("A simple calculator")
def add(y,z):
    return y+z
def subtract(y,z):
    return y-z
def divide(y,z):
    return y/z
def multiply(y,z):
    return y*z
def main():
    print("Welcome to Ethel's simple Calc")
    try:
        num1=float(input("Enter first number:"))
        num2=float(input("Enter second number:"))
        operator=input("Enter one of the operators +, -, /, or *:" )
        if operator=="+":
            result=add(num1,num2)
        elif operator=="-":
            result=subtract(num1,num2)
        elif operator=="/":
            result=divide(num1,num2)
        elif operator=="*":
            result=multiply(num1,num2)
            return
        print("The result is: ", result)
    except:
        print("invalid Input")

main()

#Exercise
#a graphical simple calculator using tkinter

#importing everything from tkinter
from tkinter import *  
#globally declare the expression variable
expression=""
#function to update expression in entry box on pressing a grid/button
def press(num):
    #point out the global expression
    global expression
    #concatenation of string
    expression=expression+ str(num)
    #update the expression
    equation.set(expression)
#function to evaluate the final expression
def equalpress():
    #try except to catch errors like zer division
    try:
        global expression
        #eval function to evaluate the final expression and string function to convert it into a string
        total=str(eval(expression))
        equation.set(total)
        expression=" "
    except:
        equation.set("error")
        expression=" "
#function to clear the entry box
def clear():
    global expression
    expression=""
    equation.set("")

#driver code
if __name__ == "__main__":
    #create the GUI window
    gui=Tk()
    #setting the background color of window
    gui.configure(background="blue")
    #setting the title of the window
    gui.title("Naggita Ethel Simple Calculator")
    #setting window configuration
    gui.geometry("270x150")
    #creating an instance of the string variable class
    equation=StringVar()
    #creating the text entry box
    expression_field=Entry(gui, textvariable=equation)
    #grid method to place widgets in respective positions in form of a table
    expression_field.grid(columnspan=4,ipadx=70)
    #creating buttons and placing them in respective positions
    button1=Button(gui, text="1", fg="black",bg="yellow", command=lambda: press(1), height=1, width=7)
    button1.grid(row=2,column=0)
    button2=Button(gui, text="2", fg="black",bg="yellow", command=lambda: press(2), height=1, width=7)
    button2.grid(row=2,column=1)
    button3=Button(gui, text="3", fg="black",bg="yellow", command=lambda: press(3), height=1, width=7)
    button3.grid(row=2,column=2)
    button4=Button(gui, text="4", fg="black",bg="yellow", command=lambda: press(4), height=1, width=7)
    button4.grid(row=3,column=0)
    button5=Button(gui, text="5", fg="black",bg="yellow", command=lambda: press(5), height=1, width=7)
    button5.grid(row=3,column=1)
    button6=Button(gui, text="6", fg="black",bg="yellow", command=lambda: press(6), height=1, width=7)
    button6.grid(row=3,column=2)
    button7=Button(gui, text="7", fg="black",bg="yellow", command=lambda: press(7), height=1, width=7)
    button7.grid(row=4,column=0)
    button8=Button(gui, text="8", fg="black",bg="yellow", command=lambda: press(8), height=1, width=7)
    button8.grid(row=4,column=1)
    button9=Button(gui, text="9", fg="black",bg="yellow", command=lambda: press(9), height=1, width=7)
    button9.grid(row=4,column=2)
    button0=Button(gui, text="0", fg="black",bg="yellow", command=lambda: press(0), height=1, width=7)
    button0.grid(row=5,column=0)
    plus=Button(gui, text="+", fg="black",bg="lightgreen", command=lambda: press("+"), height=1, width=7)
    plus.grid(row=2,column=3)
    minus=Button(gui, text="-", fg="black",bg="lightgreen", command=lambda: press("-"), height=1, width=7)
    minus.grid(row=3,column=3)
    multiply=Button(gui, text="*", fg="black",bg="lightgreen", command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=4,column=3)
    divide=Button(gui, text="/", fg="black",bg="lightgreen", command=lambda: press("/"), height=1, width=7)
    divide.grid(row=5,column=3)
    equal=Button(gui, text="=", fg="black",bg="lightgreen", command=equalpress, height=1, width=7)
    equal.grid(row=5,column=2)
    clear=Button(gui, text="clear", fg="black",bg="lightgreen", command=clear, height=1, width=7)
    clear.grid(row=5,column=1)
    point=Button(gui, text=".", fg="black",bg="lightgreen", command=lambda: press("."), height=1, width=7)
    point.grid(row=6,column=0)
    #starting the GUI
gui.mainloop()







