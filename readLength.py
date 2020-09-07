import numpy as np
import re
import math
def period_minus(a, b):
    if abs(a-b)<0.5:
        return abs(a-b)
    else:
        return 1-abs(a-b)

def read_bond_length(POSCAR, orderA, orderB, atom_number):
    #orderA and orderB are the order of two atoms
    with open(POSCAR) as file:
        line = file.readline()
        line = file.readline()
        paraA = float(file.readline().split()[0])
        paraB = float(file.readline().split()[1])
        paraC = float(file.readline().split()[2])

        while not re.search(r"D", line) and not re.search(r"d", line):
            line = file.readline()
        
        atoms=[0]*atom_number
        for i in range(atom_number):
            atoms[i] = file.readline().split()
    #print(type(atoms[orderB][2]))
    A = list(map(float, atoms[orderA]))
    B = list(map(float, atoms[orderB]))
    #print(A)
    #print(B)
    length = math.sqrt(period_minus(A[0], B[0])**2*paraA**2 + period_minus(A[1], B[1])**2*paraB**2 + period_minus(A[2], B[2])**2*paraC**2)
    print(length)

read_bond_length("POSCAR_opted", 3, 9, 16)
read_bond_length("POSCAR_opted", 5, 9, 16)
