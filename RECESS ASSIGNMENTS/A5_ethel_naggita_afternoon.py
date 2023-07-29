#Exceptional handling
#exceptions are raised when some internal events occur which change the normal flow of the program. They are handled using try,except,else and finally statements to enable further execution of the program.
#the try block holds code that is likely to cause an exception, the except block contains code to be printed in case the exception occurs, the else block contains code that is executed incase there is no exception, the finally block contains code that is always executed. 
#example 1
try:
    x=int(input("Enter first input:"))
    y=int(input("Enter second input:"))
    z= x + y
    print(z)
except:
    print("Error:Cannot add an int to a str")
#example 2 (contains the type of expection to be caught)
#types of exceptions include SyntaxError, TypeError, NameError, IndexError,KeyError, ValueError, AttributeError, IOError, ZeroDivisionError and ImportError
a=[1,2,3]
try:
    index=int(input("Enter an index:"))
    print("Value at index",index,"is",a[index])
except IndexError:
    print("Index not found") #executed if the index input is not in the list
except:
    print("Please enter an integer") #executed if the error is not concerning the index forexample entering a string as index
else:
    print(a) #executed if no exception is occurs
finally:
    print("This is exceptional handling") #always executed
#the raise keyword (this is used to force an eception in case a certain condition occurs)
x="LapTop"
if x != "laptop":
    raise Exception("x should always be 'laptop'")
#user defined exceptions
class InvalidAgeException(Exception):
    pass
try:
    age=int(input("Enter your age:"))
    if age<18:
        raise InvalidAgeException
    else:
        print("Your eligible to vote")
except InvalidAgeException:
    print("Exception occured: Invalid age")

#using the assert statement to raise a user defined exception, when the condition in the assert statement is not meant, an assertion error is raised.
#A message to be printed in case an assertion error is raised can also be added as the exception is handled

try:
    age=int(input("Enter your age:"))
    assert age>0
    print("Your age:",age)
    print("Your year of birth:",2023-age)
except AssertionError:
    print("Age should be a positive integer")

#creating a user defined exception class using a constructor and display function
#class UserError is extended from super class Exception
class AgeError(Exception):
    #constructor method
    def __init__(self, message):
        self.message = message
    #display function
    def __str__(self):
        return(repr(self.message))

try:
    name=input("Please enter your name:")
    age=int(input("Enter your age:"))
    if age<=0:
        raise(AgeError("Age should be a positive integer"))
        
    elif age>0 and age<18:
        raise(AgeError("Age should be atleast 18"))
    
    else:
        print("Welcome!!!")
#value of exception is stored in e
except AgeError as e:
    print("A new exception occured:", e.message)
#user defined exception class using multiple inheritance
class Error(Exception):
    pass
class ZeroError(Error):
    pass
try:
    num=float(input("Please enter a number:"))
    if num==0:
        raise ZeroError
    else:
        print("Your number:",num)
except ZeroError:
    print("Please enter a non-zero number")



#File handling
#Advantages: versatile, flexible
#Disadvantages: complex,security,performance
#modes of opening files: a-append (adds text to a file and creates a file if it doesn't exist),r-reading, w-writing( creates a file if doesn't exist), r+-reading and writing, a+-appending and reading, w+-writing and reading, x-creates a new file and retyrns an error if file already exists,
#b-opens a file in binary mode eg an image 
#writing to a file, +-opens a file for both reading and writing
#open()-opens a file, takes 2 parameters, the file name and mode of openeing
#write()-writes text to a file
#close()-closes a file
#read()-reads a file
file=open("sample.txt", "w")
file.write("Hello,this is a sample")
file.close()

#appending text to the file without writing open and close statements
with open ("sample.txt", "a") as file:
    file.write("\nThis is appended text")

#reading from the file 
with open ("sample.txt", "r") as file:
    content=file.read()
    print(content)
#reading a certain number of characters froma file
#reading 4 characters from sample2 file
with open ("sample.txt", "r") as file:
    print(file.read(5))

#printing each line in a file using a for loop
with open ("sample.txt", "r") as file:
    for line in file:
        print(line)
#readline() function, returns the first line of the file, if called twice, it returns the first two lines
with open ("sample.txt", "r") as file:
    line1=file.readline()
    line2=file.readline()
    print(line1)
    print(line2)

#readlines() function, returns all text in a file on one line
with open ("sample.txt", "r") as file:
    print(file.readlines())

#tell() function prints the byte number at which the file pointer currently exists
with open ("sample.txt", "r") as file:
    print("File pointer is ainitially at byte:",file.tell())
    file.read()
    print("After reading, file pointer is at:",file.tell())

#seek() function enables the user to externally determine the position of the file pointer
with open ("sample.txt", "r") as file:
    print("File pointer is ainitially at byte:",file.tell())
    #changing filepointer to location 10
    file.seek(10)
    print("File pointer is now at position",file.tell())
    print(file.read())



#using the rename and remove function from os module to rename and delete a file respectively
import os
def create_file(filename):
    try:
        with open (filename, "w") as f:
            f.write("Hi, this is the second sample text file")
            print("File created successfully")
    except IOError:
        print("Error:couldn't create file")

def rename_file(filename,newfilename):
    try:
        os.rename(filename, newfilename)
        print("File",filename, "renamed to ",newfilename) 
    except IOError:
        print("Error:couldn't rename file")    

def delete_file(filename):
    try:
        os.remove(filename)
        print("File",filename, "deleted successfully")
    except IOError:
        print("Error:couldn't delete file")
create_file("sample2.txt")
rename_file("sample2.txt", "sample3.txt")
delete_file("sample3.txt")
 
#creating a new directory
import os
os.mkdir("new")
#getcwd() method returns the current working directory
os.getcwd()
#changing the current working directory
os.chdir("new")
os.getcwd()
#deleting a directory
try:
    os.rmdir("new")
    print("Directory deleted successfully")
except:
    print("Failed to delete directory")