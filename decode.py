# Hitori puzzle
# Ángela María Martín García	login: angela.martin

import numpy
import subprocess
import sys
import math


def transcribe(line):
    sizem = int(math.sqrt(line.count('result')))
    array = numpy.chararray((sizem, sizem), unicode=True)
    for res in line.split(' '):
        values = res[7:].split(',')
        array[int(values[1])][int(values[0])] = values[2].replace(')', '')
    return array


# python3 encode.py solutionX.txt hitoriKB.lp hitoriX.lp
# list_arg = sys.argv
output_file = sys.argv[1]  # solutionX.txt
logic_file = sys.argv[2]  # hitoriKB.lp
problem_file = sys.argv[3]  # hitoriX.lp

# open text files.
f_out = open(output_file, 'w')
f_aux = open('merge.lp', 'w')

# merge hitoriKB.lp and hitoriX.lp
filenames = [problem_file, logic_file]
with f_aux as outfile:
    for f in filenames:
        with open(f) as infile:
            outfile.write(infile.read())

# execute clingo
try:
    subprocess.call(["clingo", "0", "merge.lp"], stdout=f_out)
except:
    print("ERROR")
    sys.exit()

# interpret results from clingo
file = open(output_file, "r+")
lines = file.readlines()
array = numpy.chararray

if "SATISFIABLE\n" in lines:
    print("\nSATISFIABLE\n")
    for line in lines:
        if "Answer: 1\n" in line:   # only obtain one result
            index_model = lines.index(line)
            model = lines[index_model + 1]
            array = transcribe(model)
else:
    print("\nUNSATISFIABLE\n")
    sys.exit()

# copy result into solution file
file.truncate(0)
file.seek(0)
for row in range(0, array.shape[0]):
    for col in range(0, array.shape[1]):
        char = array[row][col]
        if char == '0':
            file.write('*')
        else:
            file.write(char)
    file.write("\n")

# close files.
f_aux.close()
f_out.close()
file.close()
