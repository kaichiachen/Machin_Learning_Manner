import sys
from numpy import mat, mean, power

def read_input(file):
    for line in file:
        yield line.rstrip()
        
input = read_input(sys.stdin)#creates a list of input lines
input = [float(line) for line in input] #overwrite with floats
numInputs = len(input)
input = mat(input)
sqInput = power(input,2)

#output size, mean, mean(square values)
print("%d\t%f\t%f" % (numInputs, mean(input), mean(sqInput))) #calc mean of columns
print("mapper report: still alive" , file=sys.stderr)