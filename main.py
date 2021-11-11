#!/usr/bin/python

import sys
import random
import numpy as np

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./main.py [grade]")
        sys.exit(1)

    grade = int(sys.argv[1])
    matrix = [[0] * (grade+1)] * grade

    for row in range(grade):
        for col in range(grade+1):
            matrix[row][col-1] = random.randrange(1000000000) 

    print(matrix)
