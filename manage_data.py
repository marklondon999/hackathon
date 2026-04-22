# we shall read in passengar airport data

# we are testing the hypothesis that the start of the Ukrain war
# has had an impact on the number of passengers flying in and out of airports in the world
# Specifically to or from the UK and Eastern Europe

# read data
import pandas as pd
pd.set_option("display.max_columns", None)  # or 1000
pd.set_option("display.max_rows", None)  # or 1000

table1 = pd.read_csv('D:/repos/hackathon/table1.csv', skiprows=4, header=1) # skip the first row as it is not needed
table1.drop(table1.head(15).index,inplace = True)
table1.drop(columns=['Unnamed: 0', 'Unnamed: 1'], inplace=True)
table1.rename(columns={'Unnamed: 2': 'Date'}, inplace=True)
table1.dropna(how="all", inplace=True)
table1.drop(columns=['change', 'adjusted'], inplace=True)
table1.drop(table1.tail(4).index,inplace = True)
# correct figures to show thousands of passengers
#table1['Passengers'] = table1['Passengers'] * 1000

# prepare the second table
table2 = pd.read_csv('D:/repos/hackathon/table12020on.csv', skiprows=7, header=1) # skip the first row as it is not needed
table2.drop(table2.head(11).index,inplace = True)
table2.drop(columns=['Percentage\nchange\n[note 1]', 'Unnamed: 9', 'Unnamed: 10'], inplace=True)
table2.columns = table1.columns
table2.dropna(how="all", inplace=True)

# merge the two tables
table = pd.concat([table1, table2], ignore_index=True) 
print(table)