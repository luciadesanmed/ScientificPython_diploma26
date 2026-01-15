if __name__=="__main__":
 print("Script is running directly")

#Exercise 1:
#Give students in the example.csv file a bonus of 5 for all the courses. Find a way to replace all the values that are now greater than 30 by 30. Save the new data to a file. Make a plot with histograms for every course in the example file.

import pandas as pd
import matplotlib.pyplot as plt

#Extracting from csv file:
file=pd.read_csv('/home/desan/ScientificPython/ScientificPython_diploma26/data/example.csv', index_col=0)
print(file)
#Bonus of 5 for all the courses:
file=file+5

#Replace all the values greater than 30 by 30:
file.mask(file>30,30,inplace=True)

#Save the new data to a file:
file.to_csv('/home/desan/ScientificPython/ScientificPython_diploma26/data/new_example.csv')

#Make a plot with histograms for every course in the example file:
fig = plt.figure(figsize=(10,9))

plt.subplot(221)
file["course1"].plot(kind = 'hist', color='c')
plt.title('Course 1',fontweight='bold')
plt.ylabel('Frequency')
plt.xlabel('Grade')

plt.subplot(222)
file["course2"].plot(kind = 'hist', color='m')
plt.title('Course 2',fontweight='bold')
plt.ylabel('Frequency')
plt.xlabel('Grade')

plt.subplot(223)
file["course3"].plot(kind = 'hist', color='y')
plt.title('Course 3',fontweight='bold')
plt.ylabel('Frequency')
plt.xlabel('Grade')

plt.subplot(224)
file["course4"].plot(kind = 'hist', color='g')
plt.title('Course 4',fontweight='bold')
plt.ylabel('Frequency')
plt.xlabel('Grade')

plt.show()