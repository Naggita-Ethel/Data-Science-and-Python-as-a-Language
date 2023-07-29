#Control flow
age=20
if age<18:
  print("Underage")
elif age>=18 and age<=65:
  print("Adult")
else:
  print("Senior citizen")

#Loops
#For loop
  cars=["Fortuner", "TX", "V8"]
  for car in cars:
    print(car)

#while loop
x=0
while x<5:
  print (x)
  x+=1

planets=["earth","pluto","jupyter","venus","mercury"]
planets_count=0
while planets_count<len(planets):
  print(planets[planets_count])
  planets_count+=1

#break statement
for number in range(1,10):
  if number==5:
    break
  print(number)
#continue statement
for number in range(1,10):
  if number==5:
    continue
  print(number)

#Exceptional handling (try,except,finally)
try:
  x=10/0
except ZeroDivisionError:
  print("Error:Divion by zero")
finally:
  print("Always executes")
#Exercise
print("Welcome to mental health assessment")
name=input("What is your name?")

mental_scale={
  1:"Very bad, so sorry",
  2:"Very bad, so sorry",
  3:"Still bad, so sorry",
  4:"Still bad, so sorry",
  5:"Fair, still sorry",
  6:"Good, But still need improvement",
  7:"Good",
  8:"Very good",
  9:"Excellent",
  10:"Fantastic"
  
}
try:
  user_scale=int(input("Hello " + name + ",please rate your mental health on a scale of 1-10:"))
  print(mental_scale[user_scale])
except ValueError:
  print("Error:Please enter recognised input")
  