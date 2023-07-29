#Exercise 1
print("Exercise 1")
#1.
name_list=["ethel","eve","eron","eleanor","elsa"]
print(name_list[1])
#2.
name_list[0]="enid"
print(name_list)
#3.
name_list.append("elisha")
print(name_list)
#4.
name_list.insert(2,"Bathel")
print(name_list)
#5.
name_list.remove("eron")
print(name_list)
#6.
print(name_list[-1])
#7.
new_list=[1,2,3,4,5,6,7]
print(new_list[2:5])
#8.
country=["uganda","kenya","rwanda","sudan"]
new_country=country.copy()
print(new_country)
#9.
for x in country:
    print(x)
#10.
animal=["dog","cat","frog","sheep"]
#ascending order
animal.sort()
print(animal)
#descending order
animal.sort(reverse=True)
print(animal)

#11.
for item in animal:
    if "a" in item:
        print(item)
#12.
first_name=["John", "Jane","Bob"]
second_name=["Smith", "Johnson", "Martin"]
name= first_name+second_name
print(name)

#Exercise2
print("Exercise 2")
#1.
x=("samsung","iphone","tecno","redmi")
print(x[1])
#2.
print(x[-2])
#3.
x=list(x)
x[1]="itel"
x=tuple(x)
print(x)
#4.
x=list(x)
x.append("Huawei")
x=tuple(x)
print(x)
#5.
for item in x:
    print(item)
#6.
x=list(x)
x.remove("samsung")
x=tuple(x)
print(x)
#7.
cities=tuple(("kampala","jinja","hoima","mukono"))
#8.
a,b,c,d=cities
print(a,b,c,d)
#9  
print(cities[1:4])
#10 
first_name=("John", "Jane","Bob")
second_name=("Smith", "Johnson", "Martin")
name= first_name+second_name
print(name)
#11
colors=("red", "green", "blue", "yellow")
multiply=colors*3
print(multiply)
#12
thistuple=(1,3,7,8,7,5,4,6,8,5)
eight=thistuple.count(8)
print(eight)

#Exercise 3
print("Exercise 3")
#1.
set=set({"water","soda","juice"})
#2.
set.add("milk")
set.add("ribena")
print(set)
#3.
myset={"oven","kettle","microwave","refrigerator"}
if "microwave" in myset:
    print("microwave is in myset")
else:
    print("microwave is not in myset")
#4
myset.remove("kettle")
print(myset)
#5
for item in myset:
    print(item)
#6

this_set={1,2,3,4}
this_list=[5,6]
this_set.update(this_list)
print(this_set)
#7
first_name={"John", "Jane","Bob"}
age={30,67,45}
name_age=first_name.union(age)
print(name_age)

#Exercise 4
print("Exerise 4")
#1
num=10
text=" years old"
concatenate= str(num) + text
print(concatenate)
#2
txt="   Hello,   Uganda!   "
new_txt=txt.replace(" ","")
print(new_txt)
#3
print(txt.upper())
#4
print(txt.replace(" U", "V"))
#5
y="I am proudly Ugandan"
print(y[1:4])
#6
x="All \"Data Scientists\" are cool!"
print(x)
#EXercise 5
print("Exercise 5")
#1
shoes={
    "brand":"Nick",
    "color":"black",
    "size":40
}
print(shoes["size"])
#2
shoes["brand"]="adidas"
print(shoes)
#3
shoes["type"]="sneakers"
print(shoes)
#4
print(shoes.keys())
#5
print(shoes.values())
#6
if "size" in shoes.keys():
    print ("Size key exists")
else:
    print ("Size key does not exist")
#7
for key, value in shoes.items():
    print(key, value)
#8
shoes.pop("color")
print(shoes)
#9
shoes.clear()
print(shoes)
#10
me ={
    "name": "ethel",
    "age": 20,
    "course": "BSSE"
}
print(me.copy())
#11
ice_cream = {
    1:{"flavor":"vanilla","price":2000},
    2:{"flavor":"chocolate","price":3000},
    3:{"flavor":"mango","price":5000}
}
print(ice_cream)
