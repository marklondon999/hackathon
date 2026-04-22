# we shall read in passengar airport data

# we are testing the hypothesis that the start of the Ukrain war
# has had an impact on the number of passengers flying in and out of airports in the world
# Specifically to or from the UK and Eastern Europe

# read data
import pandas as pd
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
print(table1.tail(10))


# prepare the second table
table2 = pd.read_csv('data/table12020on.csv', skiprows=7, header=1) # skip the first row as it is not needed
table2.drop(table2.head(11).index,inplace = True)

print(table2.columns)
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
print(table.head(10))