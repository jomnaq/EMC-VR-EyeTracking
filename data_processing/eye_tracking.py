
import matplotlib.pyplot as plt
import csv

xx = []
yy = []
min_time = 0
max_time = 0
# Read the CSV file
with open('orb_path.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader) # Skip header row
    for i, row in enumerate(csv_reader):
        if(len(row) < 3):
            break
        xx.append(float(row[1]))
        yy.append(float(row[2]))
        if(i == 0):
            min_time = int(row[0])
        if(int(row[0]) > max_time):
            max_time = int(row[0])

print(min_time, max_time)

# Create the plot
# plt.plot(xx, yy, color='red')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('XY Coordinates')
# plt.show()




'''
The issue with the imported data is that it has the structure
1682548090125;(0.000029, -0.105919, 1.172371);(-0.024159, 0.946825, -0.047943, -0.317239);(-0.024123, 0.070461, 0.997223);2;0.8625677;-1.4;4.0;(-0.041224, 0.049087, 0.997943);(-0.007060, 0.091382, 0.995791)

This is bad because csv columns should be separated by columns, (hence the 
name), and not semicolons.

This loop works by
- replacing all of the extraneous characters " ();" with commans
- removing all the columns except for time, x, y, and z eye vector
- scaling the vector so z is always 10
'''
with open('in.csv', 'r') as input_file, open('cleaned.csv', 'w') as output_file:
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

        scale = 36
        adj_x = (x/z) * scale
        adj_y = (y/z) * scale + 1
        adj_z = (z/z) * scale

        out_line = f"{line_arr[0]},{adj_x},{adj_y},{adj_z}\n"

        # Write the processed line to the output file
        output_file.write(out_line)


x = []
y = []

# Read the CSV file
with open('cleaned.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader) # Skip header row
    for row in csv_reader:
        x.append(float(row[1]))
        y.append(float(row[2]))

# Create the plot
plt.plot(x, y)
plt.plot(xx, yy, color='red')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('XY Coordinates')
plt.show()