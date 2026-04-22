import pandas as pd
import matplotlib.pyplot as plt 

#create DataFrame
df = pd.DataFrame({'day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                   'sales': [2, 4, 5, 8, 6, 12, 15, 19, 15, 22]})

#create line chart
plt.plot(df.day, df.sales, color='purple')
plt.title('Sales by Day', loc='left')
plt.ylabel('Sales')
plt.xlabel('Day')
plt.show()