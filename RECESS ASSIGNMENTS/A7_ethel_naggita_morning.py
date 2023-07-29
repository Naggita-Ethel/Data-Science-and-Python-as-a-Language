#Advanced python
#Context manager
#This is an object that defines a temporary context for a block of code. These also enable proper resource management
#example 1   demonstrating a context manager to open a file and return a context manager instance
"""def open_file(filename):
    f=open(filename,"r")
    def __enter__():   #the __enter__() method is called when entering the with block and it returns the file
        return f
    def __exit__(self, exc_type, exc_value, exc_tb):  #the __exit__() method is called when exiting the with block regardless of whether an axception has occured or not. It ensures that the close method is called on file object
        f.close()
        return __enter__, __exit__
with open_file("sample.txt") as f:
    contents = f.read()
    print (contents)"""
class FileManager:
    def __init__(self, file_name, mode):  #initialization method
        self.file_name= file_name
        self.mode= mode
        self.file= None
    def __enter__(self):   #the __enter__() method is called when entering the with block and it returns the file
        self.file=open(self.file_name, self.mode)
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):  #the __exit__() method is called when exiting the with block regardless of whether an axception has occured or not. It ensures that the close method is called on file object
        self.file.close()
with FileManager("sample.txt", "r") as file:
    contents=file.read()
    print(contents)
        
#example 2  demonstrating a context manager using a time series
import time
class TimeSeries:
    def __enter__(self):
        self.start_time = time.time()
    def __exit__(self, exc_type, exc_value, traceback):
        end_time = time.time()
        execution_time = end_time - self.start_time
        print(f"The time for this execution is {execution_time} seconds")
with TimeSeries():
    time.sleep(2)
#multithreading and multiprocessing 
#These improve performance of a python program
#multithreading is the process by which multiple threads are created within a single process. Threads of the same process share the same memory space
# multiprocessing is where multiple processes are xreated and  executed concurrently. Each process has its own memory space.
#multiprocessing is safer than multithreading because processes do not share memory while multithreading is more efficient than multiprocessing
#whether to carry out multiprocessing or multithreading depends on the complexity of the code, the no. of cores in the CPU and the type of task to be carried out.
#example 1 (multithreading)
import threading
def task(name):
    print(f"Running task {name}")
#create multiple threads
threads = []
for i in range(5):
    t=threading.Thread(target=task, args=(f"Thread {i}",))
    threads.append(t)
    t.start()
#waiting for all threads to finish executing
for t in threads:
    t.join()
#example 1 (multiprocessing)   demonstrating the use of multiprocessing
import multiprocessing
def process_task(name):
    print(f"Processing task {name}")
#creating a pool of processes
pool=multiprocessing.Pool(processes=5)
#submitting multiple tasks to the pool
for i in range(6):
    pool.apply_async(process_task, args=(f"process {i}"))
#closing the pool and waiting for all processes to first execute
pool.close()
pool.join()

#example 2 demonstrating both multithreading and multiprocessing
import threading
import multiprocessing
def task(name):
    print(f"Running task {name} on thread {threading.current_thread().name} with process {multiprocessing.current_process().name}")
#create multiple threads
threads= []
for i in range(5):
    t=threading.Thread(target=task, args=(f"Thread {i}",))
    threads.append(t)
    t.start()
#waiting for all threads to finish executing
for t in threads:
    t.join()

#Assignment
# 1. Context manager to handle files through automatic opening and closing
#a custom context manager is created using a generator function and the context manager decorator from the contextlib module
from contextlib import contextmanager
@contextmanager
def open_file (filename, mode):
    file=open(filename, mode)
    try:
        yield file
    #the finally block is always executed making sure that the file is closed
    finally:
        file.close()
with open_file("sample2.txt", "r") as f:
    data = f.read()
    print (data)

#2. Context manager for managing database connection
#checking for databases on localhost with root user
#importing the mysql.connector module for connecting to mysql database
import mysql.connector
#creating a connection object
conn=mysql.connector.connect(
host='localhost',
user='root',
password='')
if conn.is_connected():
    print("Connected to mysql server")
    #cursor object for database manipulation
    cursor=conn.cursor()
    #querry to retrieve the databases
    cursor.execute('SHOW DATABASES')
    #fetching all the rows returned by the querry
    databases=cursor.fetchall()
    #printing the databases
    print("Databases:")
    for database in databases:
        print(database[0])
        #closing the cursor and connection
        cursor.close()
        conn.close()
else:
    print("Failed to connect to mysql")

#implementing database connection using context managers
import mysql.connector
#defining database connection details
config={
    'user':'root',
    'password':'',
    'host':'localhost',
    'database':'atm',
    'raise_on_warnings': True
}
#defining a context manager for mysql connection
class MySQLConnection:
    def __init__(self, config):
        self.config=config
        self.conn=None
    def __enter__(self):  #this establishes database connection and returns a connection object to be used within the with block
        self.conn=mysql.connector.connect(**self.config)
        return self.conn
    def __exit__(self,exc_type, exc_val, exc_tb):   #This closes the connection when the with block is exited
        if self.conn.is_connected():
            self.conn.close()
#usage example
with MySQLConnection(config) as conn:
    if conn.is_connected():
        print("Successfully connected to MySQL database")
        #performing database operations
        cursor= conn.cursor()
        print("Data in the details table of the atm database")
        cursor.execute("SELECT * FROM details")
        rows=cursor.fetchall()
        for row in rows:
            print(row)
    else:
        print("Failed to connect to MySQL database")
#3. Multithreading and multiprocessing program that allows a function to run for different amounts of time
import threading
import multiprocessing
import time
#function to be executed for different durations
def run_function(duration):
    start_time=time.time()
    print(f"The time for this execution is {duration} seconds")
    while time.time() - start_time <duration:  #loop runs until specified duration
        pass
#run_with_threads function runs the function using multithreading
def run_with_threads(durations):
    threads=[]
    for duration in durations:
        thread=threading.Thread(target=run_function, args=(duration,))
        #joining the threads
        threads.append(thread)
        #starting a thred
        thread.start()
    for thread in threads:
        #waiting until all threads are done excuting
        thread.join()
#run_with_processes function runs function with multiprocessing
def run_with_processes(durations):
    processes=[]
    for duration in durations:
        process=multiprocessing.Process(target=run_function, args=(duration,))
        processes.append(process)
        #starting the process
        process.start()
    for process in processes:
        #waiting until all processes are done
        process.join()
if __name__== '__main__':
    #specifying different durations in a list to run the program
    durations=[5,10,15]
    print("Running with multithreading")
    run_with_threads(durations)
    print("Running with multiprocessing")
    run_with_processes(durations)
