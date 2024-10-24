# -*- coding: utf-8 -*-
"""Files And Exceptional handling Assignment

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1w9aG6E2iviJQ_RTN38Ccg_IAlEW1uMRg
"""

#1. **Multithreading vs. Multiprocessing**:
 #  - **Multithreading** is preferable when tasks are I/O-bound (e.g., reading/writing files or network requests), as threads can handle multiple I/O operations without blocking each other. Threads share the same memory space, making communication between them faster.
  # - **Multiprocessing** is a better choice for CPU-bound tasks (e.g., number crunching, heavy computations) since each process has its own memory space and can run independently on multiple CPU cores, providing true parallelism.
#_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#2. **Process Pool**:
 #  - A **process pool** is a collection of worker processes used to execute tasks concurrently. It efficiently manages multiple processes by maintaining a pool of pre-spawned processes and reusing them for tasks. This reduces the overhead of creating and destroying processes
 # frequently and improves performance in scenarios with many short-lived tasks
 #______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#3. **Multiprocessing in Python**:
 #  - **Multiprocessing** allows Python programs to execute in parallel across multiple CPU cores, overcoming the limitations imposed by the Global Interpreter Lock (GIL) in multithreaded programs. It is useful for CPU-bound tasks and
 # is implemented using the `multiprocessing` module in Python, enabling the use of multiple processes to run different parts of a program simultaneously.
#_______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________


#4. **Multithreading Program (Adding and Removing Numbers)**:
import threading
import time

# Shared list
numbers = []

# Lock to avoid race conditions
lock = threading.Lock()

# Condition to ensure removal happens only after addition
condition = threading.Condition(lock)

# Function to add numbers
def add_numbers():
    for i in range(5):
        with condition:
            numbers.append(i)
            print(f'Added: {i}')
            # Notify the remove_numbers thread that an item has been added
            condition.notify()
            # Simulate a delay
            time.sleep(1)

# Function to remove numbers
def remove_numbers():
    for i in range(5):
        with condition:
            # Wait until there is something to remove
            while not numbers:
                condition.wait()
            print(f'Removed: {numbers.pop(0)}')
            # Simulate a delay
            time.sleep(1)

# Creating threads
thread1 = threading.Thread(target=add_numbers)
thread2 = threading.Thread(target=remove_numbers)

# Starting threads
thread1.start()
thread2.start()

# Waiting for threads to complete
thread1.join()
thread2.join()

print('Final List:', numbers)

#_________________________________________________________________________________________________________________________________________________________________________________________________

#5. **Sharing Data between Threads and Processes in Python**:
 #  - **Threads**: You can share data between threads using **threading.Lock**, **Queue**, and **ThreadLocal** for thread-specific data.
# - **Processes**: For sharing data between processes, Python provides **multiprocessing.Queue**, **multiprocessing.Pipe**, **Value**, and **Array** from the `multiprocessing` module.

#_____________________________________________________________________________________________________________________________________________________________________________________________________________
#6. **Handling Exceptions in Concurrent Programs**:
 #  - Exception handling in concurrent programs is critical to ensure program stability. Techniques include:
 #    - Using **try-except blocks** within threads or processes.
#   - In the case of thread pools, **concurrent.futures.as_completed()** can be used to capture and handle exceptions from tasks.
 #   - Ensuring proper synchronization when handling exceptions in shared resources to prevent inconsistent states.
#________________________________________________________________________________________________________________________________________________________________________________________________

#7. **Thread Pool for Factorial Calculation**:

from concurrent.futures import ThreadPoolExecutor
import math

def factorial(n):
    return math.factorial(n)

with ThreadPoolExecutor() as executor:
    # Submitting factorial tasks for numbers from 1 to 10
    results = list(executor.map(factorial, range(1, 11)))
    print(results)

#______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#8. **Multiprocessing Pool for Squaring Numbers**:

from multiprocessing import Pool
import time

def square(n):
       return n * n

   # Function to measure time
def pool_square(pool_size):
       with Pool(pool_size) as pool:
           start_time = time.time()
           results = pool.map(square, range(1, 11))
           end_time = time.time()
           print(f"Pool Size {pool_size}, Time Taken: {end_time - start_time} seconds")
           print(results)

   # Testing with different pool sizes
for size in [2, 4, 8]:
       pool_square(size)