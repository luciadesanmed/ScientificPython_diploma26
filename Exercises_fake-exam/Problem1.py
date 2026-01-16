if __name__=="__main__":
 print("Script is running directly")

import numpy as np
#Write a function that calculates the first N Fibonacci numbers.

def fibonacci(N):
    #intial conditions:
    x1=1
    x2=1
    n=3
    numbers=np.ones(N)
    
    while n<N:
        x3=x1+x2
        numbers[n]=x3
        x1=x2
        x2=x3
        n=n+1
    return numbers
    
print(fibonacci(10))