#Advanced python
#Regular expressions: this is a sequence of characters that forms a search pattern. Implemented using the 're' model inbuilt in python

"""
metacharacters(characters with special meaning) and special sequences used in regular expressions;
meta characters
.: matches any character except  new line
*: matches zero or more occurances of the preceeding character or group
+: matches one or more occurances of the preceeding character or group
?: matches zero or one occurance of the preceeding character or group
[]: matches any character within the square bracket
[^]: matches any character not within the square brackets
^: matches the start of the line
$: matches the end of the line 
{}:matches exactly the specified number of occurances eg "he.{2}"
(): capture and group
|: either or eg "rainny|sunny"
\: signals a special sequence
special sequences
\d:matches any digit (0-9)
\w:matches any alphanumeric character (0-9,a-z,A-Z)
\s:matches any whitespace character (space,tab, newline)
\A: returns a match if the specified characters are at the beginning of the string eg "\AThe"
\b:returns a match where the specified characters are at the beginning or at the end of the word eg r"\bain". THe r ensures that the string is being treated as a raw string
\B: returns a match where the specified characters are present but not at the beginning or at the end of the string eg r"\Bain". THe r ensures that the string is
\D: returns a match where the string doesn't contain digits
\S; returns a match where the string doesn't contain a white space character
\W: returns a match where the string doesn't contain any word characters
\Z: returns a match where the specified characters are at the end of the string eg "Spain\Z".

Sets
A set is a set of characters inside a pair of square brackets
[arn]: returns a match where one of the specified characters is present
[a-n]: returns a match for any lower case character btn a and n
[0-3][0-9]: returns a match for any two-digit numbers from 00 and 39
[a-zA-Z]: returns a match for any character alphabetically between a nd z lower or upper case
[+]: returns a match for any + character in the string

regex functions
The re module offers a set of funtions that allows searching of a string eg
 re.match(): searches only from the beginning of the string. if the match is found somewhere in the middle of the string, it returns none. 
 re.search(): returns a match object if there is a match anywhere in the string even if not at the beginning
 re.findall(): returns a list containing all matches
 re.split(): returns a list where the string has been split at each match
 re.sub(): replaces one or many matches with a string
 """

#example 1 demonstrating regex through matching first word, match group word, match all numbers
import re
text="Hello, I am Ethel"
#match first word
match=re.search(r"\w+",text) #or (r"\b\w+\b",text)
if match:
    print("Match:",match.group())
#example 2 searches for any digit in the text
matches=re.findall(r"\d+",text)
print("Matches:",matches)

#example 3
text="Hello, I am Ethel"
pattern=r"Ethel"
found=re.search(pattern,text)
if found:
    print("Pattern",pattern,"found")
else:
    print("Pattern",pattern,"not found")
#example 4 searching the string to see if it starts with "The" and ends with "Spain":
txt="The rain in Spain"
x=re.search("^The.*Spain$",txt)
if x:
    print("True")
else:
    print("False")
#example 5 returns a list of similar patterns in the text
text="The rain in Spain"
x=re.findall("ai",text)
print(x)
#example 6 searching for the first white space charater in the string
txt="The rain in Spain"
x=re.search("\s",txt)
print("The first white space character is found at position:",x.start())
#example 7
import re
txt="The rain in Spain"
x=re.split("\s",txt)  #splits txt where there are white spaces
print(x)
#example 8
txt="The rain in Spain"
x=re.sub("\s","*",txt)   #subsitutes whitespaces in string txt with *
print(x)
#example 9
#replacing the first two occurances
txt="The rain in Spain"
x=re.sub("\s","*",txt,2)
print(x)
#example 10
text="The rain in Spain"
x=re.search("ai",text)   #serach() returns the match object
print(x)
"""the match object has properties and methods used to retrieve information about the search and result
.span(): returns a tuple containing the start and end positions of the match
.string: returns the string passed into the function
.group(): returns the part of the string where there was a match"""
#example 11
text="The rain in Spain"
x=re.search(r"\bS\w+",text)   #looks for any word that starts with an uppercase S and returns its position
print(x.span())
#example 12
text="The rain in Spain"
x=re.search(r"\bS\w+",text)   #prints the string passed into the function
print(x.string)
#example 13
text="The rain in Spain"
x=re.search(r"\bS\w+",text)   #prints the word starting with upper case s (S)
print(x.group())

#example 14 validate email format
def validate_email(email):
    pattern= r'^[\w\.-]+@[\w\.-]+\.\w+$'  #r makes a raw string such that \ is not treated as an escape character
    if re.match(pattern, email):
        return True
    else:
        return False
email1="ethelnaggita@gmail.com"
email2="fghytgmail.com"
print(validate_email(email1))
print(validate_email(email2))
#Assignment validate a password
#A password should contain atleast 6 to 20 characters,at least one uppercase and uppercase letter, atleast one number and atleast one special symbol
def validate_password(password):
    regex=r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
    if re.match(regex,password):
        return True
    else:
        return False
password1="Elizajuly23$"
password2="fbhgd"
print(validate_password(password1))
print(validate_password(password2))



#generators and iterators
#generators are implemented using the 'yield' keyword, they are used to lazily create objects that can be iterated over
#generators save more space compared to iterators
#if the body of a function contains yield, the function automatically becomes a generator function. Generator functions use yield instead of return
#example 1  a generator function
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3
for value in simpleGeneratorFun():
    print(value)

#example 2 a generator object
#a generator function returns a generator object. Generator objects are used either by calling the next method or using the for loop
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3
#x is a generator object
x=simpleGeneratorFun()
#iterating over the generator object using next
print(next(x))
print(next(x))
print(next(x))
#example 3 without generators
def factorial(n):
    if n==0:
        return 1
    else:
        return n* factorial(n-1)
for i in range(1,10):
    print("Factorial of", i,":",factorial(i))

#using generators
def factorial(n):
    if n==0:
        yield 1
    else:
        fact=1
        for i in range(1, n+1):
            fact *=i
            yield fact
for i in range(1,5):
    print(*factorial(i))



#iterators : An iterator is an object that contains a countable number of values. It can be iterated upon.
#These implement the iterator protocol which consists of methods__iter__() and __next__()
#iter() method is used to get an iterator
#example 1
mytuple=("apple","banana","berry")
myit=iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))
#example 2   strings as iterable objects
mystring="banana"
myit=iter(mystring)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

#example 3 creating an ierator that returns numbers starting with 1 increasing the sequence by 1 and makes 20 iterations
class MyNumbers:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a<=20:
            x=self.a
            self.a+=1
            return x
        else:
            raise StopIteration
myclass=MyNumbers()
myiter=iter(myclass)
for x in myiter:
    print (x)


#example 4
def square():
    for i in range(1,10):
        yield i**2
#creating iterator object
squares_iterator=square()
for i in range(5):
    print(next(squares_iterator))



#decorators (allow modifying the behaviour of functions or classes without direct change of source code, it takes a function as an input and returns a new function)
# example 1treating functions as objects 
def shout(text):
    return text.upper()
print(shout("Hello"))
yell=shout
print(yell("Hello"))
#example 2   passing functions as arguments
def shout(text):
    return text.upper()
def whisper(text):
    return text.lower()
def greet(func):
    #storing the function in a variable
    greeting=func("Hello")
    print(greeting)
greet(shout)
greet(whisper)
#example 3 returning functions from other functions
def divider(x):
    def divide(y):
        return x/y
    return divide
div=divider(15)
print(div(3))
#example 4 decorators: In decorators, functions are taken as arguments in other functions and then called inside wrapper functions
def my_decorator(func):
    def inner():
        print("This is a decorator")
        func()
    return inner
@my_decorator
def outer_decorator():
    print("This is the outer decorator")
outer_decorator()


#Multi threading
#This is a way of achieving multi processing. A thread is an entity within a process tat can be scheduled for execution
#Multithreading is the ability of a processor to execute multiple threads concurrently through context switching
#this is achieved using the threading module
#example 1
import threading
def print_cube(num):
    print("Cube: {}" .format(num*num*num))
def print_square(num):
    print("Square: {}" .format(num*num))
if __name__ == "__main__":
    #creating the threads
    t1=threading.Thread(target=print_cube, args=(10,))
    t2=threading.Thread(target=print_square, args=(10,))
    #starting the threads
    t1.start()
    t2.start()
    #making the current program to wait until thread 1 and 2 are completely executed
    t1.join()
    t2.join()


#multiprocessing in python
#This is the ability of a system to support more than one processor at the same time
#it is implemeted using the multiprocessing module
#example 1 printing IDs of processes running target functions to show that the processes are executed and main(current) program first waits until their execution is done
import multiprocessing
import os
def worker1():
    #printing process id
    print("ID of process running worker1: {}" .format(os.getpid()))
def worker2():
    print("ID of process running worker2: {}" .format(os.getpid()))
if __name__ == "__main__":
    print("ID of main process: {}" .format(os.getpid()))
    #creating processes
    p1=multiprocessing.Process(target=worker1)
    p2=multiprocessing.Process(target=worker2)
    #starting processes
    p1.start()
    p2.start()
    #process IDs
    print("ID of process p1: {}" .format(p1.pid))
    print("ID of process p2: {}" .format(p2.pid))
    #main process waiting until the processes are done
    p1.join()
    p2.join()
    #both processes are finished
    print("Both processes are done executing")
    #checking if processes are alive
    print("Process p1 is alive:",p1.is_alive())
    print("Process p2 is alive:",p2.is_alive())

#Context managers in python
#these enable proper handling of resources  like file operations and databases. These resources are limited in supply therefore they must be released after uasage to prevent them from being released resource leakage or system crash among others
#when creating context managers using casses, __enter__() and __exit__() methods are used and the with keyword
#__enter__() returns the resource that needs to be managed while __exit__() returns nothing but performs the cleaning operations
#example 1
class ContextManager():
    def __init__(self):  #init function for initialization
        print("init method called")
    def __enter__(self):
        print("enter method called")
        return self
    def __exit__(self, exc_type, exc_value,exc_traceback):
        print("exit method called")
with ContextManager() as manager:
    print("with statement block")



