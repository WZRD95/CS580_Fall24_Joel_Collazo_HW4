#!/usr/bin/python3.7
import random
import csv
import matplotlib.pyplot as plt 

name_csv_file = 'data.csv'
new_Y = 0
list_points_X = []
list_points_Y = []
list_points_COLOR = []
list_value_0_1 = []
weight_1 = random.random()
weight_2 = random.random()
add_bais = random.random()
list_end_X =[]
list_end_Y =[]
error_guess = 0
rate_of_change = 0.01
plt.xlim(-0.1, 1.1) 
plt.ylim(-0.1, 1.1) 

print(".........Random Weights........")
print(weight_1)
print(weight_2)
print(add_bais)
print("...............END.............\n")

with open(name_csv_file, 'r') as file_to_parse:
    Line_data = csv.reader(file_to_parse)
    ALL_Data = list(Line_data)

size_of_list = len(ALL_Data)

print(".........DATA from file........")
for index_X,index_Y,index_value in ALL_Data:
    list_points_X.extend([float(index_X)])
    list_points_Y.extend([float(index_Y)])
    list_value_0_1.extend([int(index_value)])

    if int(index_value) == 0:
        list_points_COLOR.extend(['red'])
    else:
        list_points_COLOR.extend(['blue'])

print("...............END.............\n")

# *** Make a line *** -------------------------------
new_Y_start = (-1*(weight_1*-1 + add_bais))/weight_2
new_Y_end = (-1*(weight_1*2 + add_bais))/weight_2

list_end_X.extend([float(-1)])
list_end_Y.extend([float(new_Y_start)])
list_end_X.extend([float(2)])
list_end_Y.extend([float(new_Y_end)])

plt.plot(list_end_X, list_end_Y,color='red')


# *** MAIN funtion here *** -------------------------------
counter = 0
loops_to_do = 0
ERROR_watch = 1
while loops_to_do < 10:

    for index in range(size_of_list):

        get_z = (weight_1*list_points_X[index]) + (weight_2*list_points_Y[index])  + add_bais

        if get_z >= 0:
            y_hat_guess = 1
        else:
            y_hat_guess = 0

        error_guess = list_value_0_1[index] - y_hat_guess
        ERROR_watch = ERROR_watch + rate_of_change*error_guess

        if error_guess != 0:
            add_bais = add_bais + rate_of_change*error_guess
            weight_1 = weight_1 + (rate_of_change*list_points_X[index]*error_guess)
            weight_2 = weight_2 + (rate_of_change*list_points_Y[index]*error_guess) 

        if weight_2 == 0:
            new_Y_start = 0
            new_Y_end = 0
        else:
            new_Y_start = (-1*(weight_1*-1 + add_bais))/weight_2
            new_Y_end = (-1*(weight_1*2 + add_bais))/weight_2

        list_end_X.clear()
        list_end_Y.clear()
        list_end_X.extend([float(-1)])
        list_end_Y.extend([float(new_Y_start)])
        list_end_X.extend([float(2)])
        list_end_Y.extend([float(new_Y_end)])

        plt.plot(list_end_X, list_end_Y,color='green', linestyle='dashed')
        counter = counter + 1
        print('(' +  str(counter) + ',' + str(ERROR_watch) +')')
        

    loops_to_do = loops_to_do + 1

# End Line -------------------------------
new_Y_start = (-1*(weight_1*-1 + add_bais))/weight_2
new_Y_end = (-1*(weight_1*2 + add_bais))/weight_2

list_end_X.clear()
list_end_Y.clear()
list_end_X.extend([float(-1)])
list_end_Y.extend([float(new_Y_start)])
list_end_X.extend([float(2)])
list_end_Y.extend([float(new_Y_end)])

plt.plot(list_end_X, list_end_Y,color='black')

plt.scatter(list_points_X,list_points_Y,c=list_points_COLOR)
plt.show()

