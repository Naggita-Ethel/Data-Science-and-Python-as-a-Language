#Dictionaries (ordered,mutable,allows different datatypes)
my_dict={1: "one",2:"two",3:"three"}
print(my_dict)
#length
print(len(my_dict))
#type
print(type(my_dict))
#accessing
print(my_dict[2])
print(my_dict.get(1))
#printing keys
print(my_dict.keys())
#printing values
print(my_dict.values())
#printing dictionary items
print(my_dict.items())

#Numbers datatype (integer, float, complex)
w=4
x=4.6
y=3j
z=-4.0
a=6+4j
print(type(w))
print(type(x))
print(type(y))
print(type(z))
print(type(a))

#convert from int to complex
b=complex(w)
print (b,type(b))
#int to float
print("Converting from int to float")
c=float(w)
print (c,type(c))
#float to complex
h=complex(x)
print(h, type(h))

#Casting-used to specify datatype, used for only integers, floats and strings
d=int(20)
e=int("40")
print(type(e))

#String datatype
print("Good afternoon")
#Assigning strings to variables
f="Good afternoon"
print(f)
#Multiline strings
g="""Am Ethel
Year two
Software engineering"""
print(g)
#Strings as arrays
f="  Good afternoon  "
print(f[3])
#Modifying strings
print(f.lower())
print(f.upper())
#remove whitespaces
print(f.strip())
#String concatenation
g="sir"
print(f+g)

#String formatting
age=25
name="I am Ethel and I am {}"
print(name.format(age))

name="Ethel"
age=25
me="I am {} and I am {}"
print(me.format(name,age))

#Boolean datatype
print(40<6)
print(40==40)
print(bool(56))
print(bool("Ethel"))
print(bool(""))
print(bool(0))


#Exercise 1
print("Exercise 1")
#1.using the values function to print values of a dictionary
my_dict={1: "one",2:"two",3:"three"}
print(my_dict.values())
#2.check if a key exists in a dictionary
if my_dict.get("4")==None:
    print("Key not present")
else:
    print("Key present")   
#3.Change dictionary items and update them
#Changing dictionary items
my_dict[2]="six"
print(my_dict)
#Update items
this_dict={3:"four"}
my_dict.update(this_dict)
print(my_dict)

#4. Adding and removing items
#Adding items
my_dict[5]="five"
print(my_dict)
#Removing items
del my_dict[3]
print(my_dict)
# or my_dict.pop(3)
#5.Looping through a dictionary and nesting dictionaries
#Looping through a dictionary
for x in my_dict:
    print(x)
for k, v in my_dict.items():
    print(k, v)
for v in my_dict.values():
    print(v)
#Nested dictionaries
ice_cream = {
    1:{"flavor":"vanilla","price":2000},
    2:{"flavor":"chocolate","price":3000},
    3:{"flavor":"mango","price":5000}
}
#accessing items
print("Accessing items")
print(ice_cream[1]["flavor"])
#adding items
ice_cream[3]["discount"] =True
print(ice_cream)
#Changing items
ice_cream[3]["price"]=4000
print(ice_cream)
#deleting items
del ice_cream[3]
print(ice_cream)
#iterating through items
for key,value in ice_cream.items():
    print(key,value)
    

#Exercise 2
print("Exercise 2")
#1.length of a string
f="Good"
print(len(f))
h="Good afternoon"
print(len(h))
#2.for loop in a string
for element  in h:
    print(element)
#reversed string
print("reversed string")
length=len(h)
for element in reversed(range(0,length)):
    print(h[element])
#printing some characters
print("printing some characters")
for element in h[0:5:1]:
    print(element)
#3.Slicing in strings
print("Slicing in strings")
string_name="STRING"
s1=slice(4)
s2=slice(1,5,2)
s3=slice(-1,-10,-2)
print(string_name[s1])
print(string_name[s2])
print(string_name[s3])

#Exercise 3
print("Exercise 3")
#1. Use of a conditional statement with booleans
a=0
if (not(a))==True:
    print("Not operator returns the reverse.")

booleans=[True, False]
for boolean in booleans:
    if (boolean==True):
        print("A true exists")
    elif (boolean==False):
        print("A false exists")
    else:
        print("Nothing exists")

a=10
b=5
if (a==10) and (b==5):
    print("A is ten and b is five")
elif (a>20) or (b==4):
    print("A is ten")
else:
    print("We have both A and B")