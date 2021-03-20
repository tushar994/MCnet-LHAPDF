import pandas as pd
from mpl_toolkits import mplot3d


# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt



df = pd.read_csv (r'./plot2.csv')
x = df['x']
y = df['y']
z = df['val']

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.scatter3D(x, y, z, c=z, cmap='Greens')

plt.show()
