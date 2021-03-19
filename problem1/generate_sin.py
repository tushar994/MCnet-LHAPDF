import math

list = []
frequency = math.pi/2
current_x = 0
while(current_x<=10):
    list.append([current_x, math.sin(current_x)])
    current_x+=frequency

if(current_x-frequency<10):
    list.append([10,math.sin(10)])

final_string = str(list).replace("[","{")
final_string = final_string.replace("]","}")
print(final_string)

print("length : " + str(len(list)))