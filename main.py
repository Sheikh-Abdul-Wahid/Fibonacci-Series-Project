# Importing the time module to measure execution time
import time             

# Function to calculate Fibonacci using recursion
def FiboRecursion(num): 
    if (num == 0):      
        return 0
    if (num == 1):     
        return 1
    else:
        return FiboRecursion(num-1) + FiboRecursion(num-2) 

# Function to calculate Fibonacci using iteration
def FiboIteration(num): 
    previous_num = 0    
    current_num = 1    
    for i in range(0, num):  
        previous_to_previous_num = previous_num 
        previous_num = current_num               
        current_num = previous_num + previous_to_previous_num  
    return current_num                                         

# Infinite loop to keep asking the user for input until a valid number is provided
while True:
    n = int(input("Enter your Number: "))             
    if n < 0:                                        
        print("Please enter a non-negative integer")  
    else:
        initial_time = time.time()  # Record the start time
    
        # Calculate Fibonacci using iteration and display the result
        print(f"Using Iteration Method value of Fibonacci({n}) is: {FiboIteration(n)}")
        print(f"It took {time.time() - initial_time} seconds using Iteration Method")

        # Calculate Fibonacci using recursion and display the result
        print(f"Using Recursion Method value of Fibonacci({n}) is: {FiboRecursion(n)}")
        print(f"It took {time.time() - initial_time} seconds using Recursion Method")
        break  # Exit the loop after calculating Fibonacci
