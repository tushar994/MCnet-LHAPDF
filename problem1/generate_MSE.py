import pandas as pd
import matplotlib.pyplot as plt
import math

files = ["./csv_files/interval_pi_by_2.csv", "./csv_files/interval_pi_by_4.csv" , "./csv_files/interval_pi_by_8.csv",
"./csv_files/interval_pi_by_16.csv", "./csv_files/interval_pi_by_32.csv"]

for index,file_name in enumerate(files):
    df = pd.read_csv (file_name)
    x = df['x']
    y = df['y']


    MSE = 0
    for i,x_val in enumerate(x):
        MSE += (y[i] - math.sin(x_val))**2
    MSE = MSE/len(x)
    print("MSE for pi/" + str(2**(index+1)) + " is " + str(MSE))

