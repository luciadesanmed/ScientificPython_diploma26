if __name__=="__main__":
 print("Script is running directly")

#Exercise 3:
#create a random matrix with numpy
#save it to file
#read it back with numpy
#calculate some statistics on it with numpy
#read the same file with pandas
#calculate the same statistics on it with pandas

import numpy as np
import pandas as pd

#Create a random matrix with numpy:
n=4
A=np.random.rand(n,n)

#Save it to a file:
np.savetxt('/home/desan/ScientificPython/ScientificPython_diploma26/data/matrix.txt',A)

#Read it back with numpy:
A1=np.loadtxt('/home/desan/ScientificPython/ScientificPython_diploma26/data/matrix.txt')

#Calculate some statistics:
A1median=np.median(A1)
A1mean=np.mean(A1)
A1std=np.std(A1)
A1var=np.var(A1)

print('Numpy:', A1median, A1mean, A1std, A1var)

#Read the same file with pandas:
A2=pd.read_csv('/home/desan/ScientificPython/ScientificPython_diploma26/data/matrix.txt', sep=" ", header=None)

#Calculate the same statistics with pandas:
A2median=A2.stack().median()
A2mean=A2.stack().mean()
A2std=A2.stack().std()
A2var=A2.stack().var()

print('Pandas:', A2median, A2mean, A2std, A2var)