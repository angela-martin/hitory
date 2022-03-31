# Hitori puzzle
# Ángela María Martín García	login: angela.martin

import sys

# python3 encode.py < hitori1.txt > hitori1.lp
list_arg = sys.argv
input_file = list_arg[1]  # hitoriX.txt
output_file = list_arg[2]  # hitoriX.lp

# open text files.
f = open(input_file, 'r')
f_out = open(output_file, 'w')

# read text from the text file.
rows = f.readlines()

for row in range(len(rows)):
    # columns = len(row) - 1  # minus 1 to deal with \n
    for column in range(len(rows)):
        data = 'cell(' + str(column) + ',' + str(row) + ',' + str(rows[row][column]) + ').'
        f_out.write(data + '\n')

# close files.
f.close()
f_out.close()
