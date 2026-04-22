# we shall read in passengar airport data

# we are testing the hypothesis that the start of the Ukrain war
# has had an impact on the number of passengers flying in and out of airports in the world
# Specifically to or from the UK and Eastern Europe

# read data
import pandas as pd
import sktime as skpip
import matplotlib.pyplot as plt 
import numpy as np

pd.set_option("display.max_columns", None)  # or 1000
pd.set_option("display.max_rows", None)  # or 1000

table1 = pd.read_csv('data/table1.csv', skiprows=4, header=1) # skip the first row as it is not needed

# drop the top of the table which contains metadata and the bottom of the table which contains footnotes
table1.drop(table1.head(15).index,inplace = True)
table1.drop(columns=['Unnamed: 0', 'Unnamed: 1'], inplace=True)
table1.rename(columns={'Unnamed: 2': 'Date'}, inplace=True)
table1.dropna(how="all", inplace=True)
table1.drop(columns=['change', 'adjusted'], inplace=True)

# drop end junk 
table1.drop(table1.tail(4).index,inplace = True)


# Convert the columns to numeric values and remove commas
for col in table1.columns:
    if col != 'Date':
        table1[col] = table1[col].str.replace(',', '')  # remove commas from the numbers
        table1[col] = table1[col].astype(float)  # convert the column to float
        table1[col] = table1[col].astype(float) * 1000

# Check the data



# prepare the second table
table2 = pd.read_csv('data/table12020on.csv', skiprows=7, header=1) # skip the first row as it is not needed
table2.drop(table2.head(11).index,inplace = True)


table2.drop(columns=['Percentage\r\nchange\r\n[note 1]', 'Unnamed: 9', 'Unnamed: 10'], inplace=True)
table2.columns = table1.columns
table2.dropna(how="all", inplace=True)


# remove missing data and replace with zero
table2.replace('[x]', 0, inplace=True)

# replace NaN with zero
table2.fillna(0, inplace=True)

# Convert the columns to numeric values and remove commas
for col in table2.columns:
    if col != 'Date':
        table2[col] = table2[col].str.replace(',', '')  # remove commas from the numbers
        table2[col] = table2[col].astype(float)  # convert the column to float

# merge the two tables
table = pd.concat([table1, table2], ignore_index=True) 

# make a sedquence of timestamps in quartly formnat starting from 2009, Q1 to 2025, Q2
dates = pd.date_range(start='2009-01-01', end='2025-06-30', freq='QE')

# Replace the Date with a time series sequence of step Quarterly
table.Date = dates



#create line chart
# plt.plot(table.Date, table['America'], color='purple')
# plt.title('America Traffic Over Time', loc='left')
# plt.ylabel('America')
# plt.xlabel('Date')
# plt.show()



# normalising the data to be between 0 and 1
for col in table.columns:
    if col != 'Date':
        target_col = col + '_norm'
        min_val = table[col].min()
        max_val = table[col].max()
        table[target_col] = (table[col] - min_val) / (max_val - min_val)
        
print(table.head(10))

# # now display the normalised data       
# plt.plot(table.Date, table['Europe_norm'], color='purple')
# plt.plot(table.Date, table['America_norm'], color='red')
# plt.plot(table.Date, table['EU_norm'], color='blue')
# plt.plot(table.Date, table['EU15_norm'], color='green')
# plt.plot(table.Date, table['Other EU_norm'], color='yellow')
# plt.plot(table.Date, table['Countries_norm'], color='orange')
# plt.plot(table.Date, table['World_norm'], color='black')
# plt.title('Traffic Over Time', loc='left')
# # plt.xlabel(table.Date.MonthLocator(interval=1))
# # plt.xlabel(table.Date.DateFormatter('%Y-%b'))
# plt.ylabel('Traffic')
# plt.xlabel('Date')
# plt.legend(['Europe', 'America', 'EU', 'EU15', 'Other EU', 'Countries', 'World'])
# plt.show()

# Europe against EU
plt.plot(table.Date, table['EU15_norm'], color='green')
plt.plot(table.Date, table['Other EU_norm'], color='purple')
plt.title('Traffic Over Time', loc='left')
plt.ylabel('Traffic')
plt.xlabel('Date')
plt.legend([ 'EU15', 'Other EU'])
plt.show()

#table.to_csv('data/merged_table.csv', index=False)