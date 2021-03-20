import pandas as pd
import matplotlib.pyplot as plt
import math

files = ["./csv_files/interval_point_1.csv", "./csv_files/interval_point_2.csv" , "./csv_files/interval_point_4.csv",
"./csv_files/interval_point_5.csv"]
acc = [0.1,0.2,0.4,0.5]

for index,file_name in enumerate(files):
    df = pd.read_csv (file_name)
    x = df['x']
    y = df['y']
    val = df['val']

    MSE = 0
    for i,x_val in enumerate(x):
        MSE += (   val[i] - (  x[i]*(math.e**(-1*(x[i]**2 + y[i]**2)))     ) )**2
    MSE = MSE/len(x)
    print("MSE for interval " + str(acc[index]) + " is " + str(MSE))

