import math

list = []
frequency = 0.1
current_x = -2
while(current_x<=2):
    list.append(current_x)
    current_x+=frequency

if(current_x-frequency<2):
    list.append(2)

final_string = str(list).replace("[","{")
final_string = final_string.replace("]","}")
print("x_array : " + final_string)
print("y_array : " + final_string)

values = []
for i,val in enumerate(list):
    values.append([])
    for j,val2 in enumerate(list):
        values[i].append(val*(math.e**(-1*(val**2 + val2**2))))

final_string = str(values).replace("[","{")
final_string = final_string.replace("]","}")
print("values: " + final_string)

print("length : " + str(len(list)))