if __name__=="__main__":
 print("Script is running directly")

import numpy as np
import pandas as pd
import sympy as sp
import matplotlib.pyplot as plt

#Function with non-linear model:
def non_linmod(x,b1,b2):
 res=b1/((np.exp(b2/x)-1)*x**5)
 return res

#b1 derivative:
def der_b1(x,b1,b2):
 res=1/((np.exp(b2/x)-1)*x**5)  
 return res

#b2 derivative:
def der_b2(x,b1,b2):
 res=-(b1*np.exp(b2/x))/((x**6)*(np.exp(b2/x)-1)**2)  
 return res

#Initial parameters:
erro=1.0e-6
a=0.1
maxiter=1
b1=1
b2=1

#Read the data:
xx=np.loadtxt('/home/desan/NumericalMethods/archivos/sun_data.txt',usecols=0)
yy=np.loadtxt('/home/desan/NumericalMethods/archivos/sun_data.txt',usecols=1)

eval_mod=np.zeros(len(xx))
j_mat=np.zeros([len(xx),2])

i=0
print(i)
db=[40000,40000]
while (db[0]**2+db[1]**2)>erro:
 r=yy-non_linmod(xx,b1,b2)
 j_mat[:, 0]=der_b1(xx,b1,b2)
 j_mat[:, 1]=der_b2(xx,b1,b2)
 j1=np.matmul(j_mat.transpose(),j_mat)
 j_inv=np.linalg.inv(j1)
 j_new=j_inv/np.linalg.det(j1)
 j_new2=np.matmul(j_new,j_mat.transpose())
 db=np.matmul(j_new2,r)
 b1=b1+db[0]*a
 b2=b2+db[1]*a
 i=i+1
 print(i)

#print(j_mat[:][1])
#print(len(j_new))
#print(len(j1[:][0]))
#print(len(j_new))
#print(len(j_new[:][0]))
#


#print(db)

#prueba=np.zeros(len(xx))
#prueba=nonlin_mod.subs([(x, xx), (b1, b0[0]), (b2, b0[1])])
#for i in range(maxiter):
 #residuals:
#i=0
#r=yy[i]-nonlin_mod.subs([(x, xx[i]), (b1, b0[0]), (b2, b0[1])])

#print(j_mat)

#Find the descent direction:
#j1=np.matmul(j_mat.transpose(),j_mat)
#Invert the matrix:
#j1=np.linalg.inv(j1)

#print(j_mat)
