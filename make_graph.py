#!/usr/bin/python3.7
import random
import csv
import matplotlib.pyplot as plt 

name_csv_file = 'data.csv'
list_points_X = []
list_points_Y = []
list_value_0_1 = []
list_points_COLOR = []
plt.xlim(-0.1, 1.1) 
plt.ylim(-0.1, 1.1) 


with open(name_csv_file, 'r') as file_to_parse:
    Line_data = csv.reader(file_to_parse)
    ALL_Data = list(Line_data)


print(".........DATA from file........")
for index_X,index_Y,index_value in ALL_Data:
    print('(', index_X, ',', index_Y, ')'  + "  Value: " + index_value)
    list_points_X.extend([float(index_X)])
    list_points_Y.extend([float(index_Y)])
    list_value_0_1.extend([int(index_value)])

    if int(index_value) == 0:
        list_points_COLOR.extend(['red'])
    else:
        list_points_COLOR.extend(['blue'])

print("...............END.............\n")

plt.scatter(list_points_X,list_points_Y,c=list_points_COLOR)
plt.show()