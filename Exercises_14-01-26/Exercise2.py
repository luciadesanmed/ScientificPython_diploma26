# Exercise 2: Create your own class for complex numbers. Make sure all the arithmetic operations work and that you can print it.
if __name__ == "__main__":
 print("Script is running directly")

import sympy as sp
#Class for complex numbers:
class Complex_numbers:
 def __init__(self,a=0,b=0):
  self.a=a
  self.b=b

 def __add__(self,other):   
  a=self.a+other.a
  b=self.b+other.b
  return Complex_numbers(a,b)
    
 def __sub__(self,other):   
  a=self.a-other.a
  b=self.b-other.b
  return Complex_numbers(a,b)

 def __mul__(self,other):   
  a=self.a*other.a-self.b*other.b
  b=self.a*other.b+self.b*other.a
  return Complex_numbers(a,b)

 def __str__(self):
  return "{0},{1}".format(self.a, self.b) #"converts" class to a string

test=Complex_numbers(1,2)
test2=Complex_numbers(4,5)

print(test+test2)
print(test*test2)
