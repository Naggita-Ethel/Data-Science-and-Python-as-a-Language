#Functions (group blocks of code)
#syntax: def fuction_name():
def afternoon():
    print("This is an afternoon class")
#calling the function
afternoon()
#arguments and parameters
def afternoon(fname,lname):
    print(fname,lname,"has attended class")
#calling the function
afternoon("Ethel","Naggita")
#default parameters
def add(a,b=3):
    print(a+ b)
add(2,6)
add(4)
#multiple unknown parameters
def multiple(*args):
    for arg in args:
        print(arg)
multiple("Enid", 15,)
#return functions
def subtract(x,y):
    return x - y
print(subtract(5,3))

#Modules
#a simple calc
def plus(s,t):
    return s + t
def product(s,t):
    return s * t

#importing square and factorial from math module
from math import sqrt,factorial #or import * or alias import math as mt
print(sqrt(16))
print(factorial(4))

#input and output
#input(prompt)
"""name=input("Enter your name: ")
print("Your name is:", name)"""

"""num= int(input("Enter a number:"))
square= num*num
print("The square is:", square)"""

#multiple inputs



"""q,r,z =map(int,input("Enter values: ").split())
print("The values are: ", end=" ")
print(q,r,z)"""


"""f=(1,2,3)
print("First tuple:", f)
g=list(f)
g.append(int(input("Enter new value: ")))
f=tuple(g)
print("New tuple:",f)"""

mylist=list(map(int,input("Enter list values:").split()))
myset=set(map(int,input("Enter set values:").split()))
print(mylist)
print(myset)

