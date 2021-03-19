import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv (r'./plot2.csv')
x = df['x']
y = df['y']

plt.scatter(x,y)
plt.show()
# print(df)

