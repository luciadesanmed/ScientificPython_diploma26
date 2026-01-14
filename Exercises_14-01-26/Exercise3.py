# Exercise 3: Create a "wrapper class" for around numpy array for operations on matrices. You should be able to execute the following code:
import numpy as np

class MyMatrix:
 def __init__(self,N):
  self.data=np.random.rand(N,N)
     
 def __add__(self,other):
  return self.data+other.data
     
 def __sub__(self,other):
  return self.data-other.data
    
 def __mul__(self,other):
  return np.matmul(self.data,other.data)

 def __str__(self):
  return "{0}".format(self.data) #"converts" class to a string
    
 def inverse(self):
  return np.linalg.inv(self.data)
     
 def determinant(self):
  return np.linalg.det(self.data)
     
 def eigenvalues(self):
  return np.linalg.eig(self.data)

    
N=4
matrix1=MyMatrix(N) #creates a square matrix
matrix2=MyMatrix(N)
print(matrix1.inverse())
print(matrix1.determinant())
print(matrix1.eigenvalues())
print(matrix1+matrix2)
print(matrix1*matrix2)