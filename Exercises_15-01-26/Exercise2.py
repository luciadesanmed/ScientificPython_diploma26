if __name__=="__main__":
 print("Script is running directly")

#Exercise 2:
#Read in the cars.csv file as a dataframe
#Remove the row with the index 3, which contains a quote in the Model column.
#Add a new column called Price with the following values: [8000, 6500, 7000, 6800, 7500, 7300, 7000, 9000, 6500, 7800]
#Find the average Length of all the vehicles.
#Find the median Price of all the vehicles.
#Create a new dataframe that only contains the rows where the Price is greater than 7000.
#Sort the dataframe in descending order by the Price column.

import pandas as pd
import matplotlib.pyplot as plt

#Reading the file as a dataframe:
file=pd.read_csv('/home/desan/ScientificPython/ScientificPython_diploma26/data/cars.csv', index_col=0)
file=pd.DataFrame(file)

#Remove the row with the index 3:
file.drop(file.index[2],inplace=True)
file.reset_index(drop=True)

#Add a new column called Price with the following data:
file['Price']=[8000, 6500, 7000, 6800, 7500, 7300, 7000, 9000, 6500]

#Find the average length of all vehicles:
mean_length=file['Length'].mean(axis=0)

#Find the median price of all vehicles:
median_price=file['Price'].median(axis=0)

#Create a new data frame that only contains the rows where the Price is greater than 7000:
newdf=file.loc[file['Price']<7000]

#Sort the dataframe in descending order by the Price column:
newdf.sort_values(by=['Price'], inplace=True, ascending=False)
