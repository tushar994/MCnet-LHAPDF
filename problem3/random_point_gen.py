import random

list = []
list_y = []

for i in range(0,100000):
    list.append(random.uniform(-2,2))
    list_y.append(random.uniform(-2,2))

final_string = str(list).replace("[","{")
final_string = final_string.replace("]","}")
print("x_array : " + final_string)

# final_string = str(list_y).replace("[","{")
# final_string = final_string.replace("]","}")
# print("y_array : " + final_string)