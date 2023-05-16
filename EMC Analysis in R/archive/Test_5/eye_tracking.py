
import matplotlib.pyplot as plt
import csv
import os
import glob

def get_file_count(string):
    return int(''.join(char for char in string if char.isdigit()))


# The issue with the imported data is that it has the structure
# 1682548090125;(0.000029, -0.105919, 1.172371);(-0.024159, 0.946825, -0.047943, -0.317239);(-0.024123, 0.070461, 0.997223);2;0.8625677;-1.4;4.0;(-0.041224, 0.049087, 0.997943);(-0.007060, 0.091382, 0.995791)

# This is bad because csv columns should be separated by columns, (hence the 
# name), and not semicolons.

# This loop works by
# - replacing all of the extraneous characters " ();" with commans
# - removing all the columns except for time, x, y, and z eye vector
# - scaling the vector so z is always 10

def create_file(min_time, max_time, file_name):
    with open('in.csv', 'r') as input_file, open(file_name, 'w') as output_file:
        for i, line in enumerate(input_file):
            # Process each line of the input file here
            if(i == 0):
                output_file.write("time (milliseconds),x,y,z\n")
                continue
            clean_line = line
            clean_line = clean_line.replace(" ", "")
            clean_line = clean_line.replace("(", "")
            clean_line = clean_line.replace(")", "")
            clean_line = clean_line.replace(";", ",")
            line_arr = clean_line.split(",")
            
            if(len(line_arr) <= 11):
                break

            time = int(line_arr[0])
            if(time < min_time or time > max_time):
                continue

            x = float(line_arr[8])
            y = float(line_arr[9])
            z = float(line_arr[10])

            adj_x = (x/z) * 20
            adj_y = (y/z) * 20
            adj_z = (z/z) * 20

            out_line = f"{line_arr[0]},{adj_x},{adj_y},{adj_z}\n"

            # Write the processed line to the output file
            output_file.write(out_line)


# print out all orb_path files
directory_path = './orb_paths'
file_list = glob.glob(os.path.join(directory_path, '*.csv'))
sorted_file_list = sorted(file_list, key=get_file_count)

omin_time = 0
omax_time = 0
for j, file_path in enumerate(sorted_file_list):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        linecount = 0
        for line in lines:
            linecount += 1

        for i, line in enumerate(lines):
            if i == linecount - 1:
                break
            line_array = line.replace(' ','').split(',')
            if i == 1:
                omin_time = int(line_array[0])
            if i == linecount - 2:
                omax_time = int(line_array[0])
        print(omin_time, omax_time)
        create_file(omin_time, omax_time, f"./eye_paths/eyepath{j+1}.csv")