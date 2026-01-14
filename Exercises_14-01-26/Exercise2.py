# Exercise 2: Create your own class for complex numbers. Make sure all the arithmetic operations work and that you can print it.
if __name__ == "__main__":
 print("Script is running directly")

import sympy as sp
#Class for complex numbers:
class Complex_numbers:
 def __init__(self,a=0,b=0):
  self.a=a
  self.b=b
 def complex_no(a,b):
  z=a+b*sp.I
  print(z)
  return z

test=Complex_numbers.complex_no(1,2)
