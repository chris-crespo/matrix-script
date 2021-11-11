#!/usr/bin/python

import sys
import random
import numpy as np

def get_grade():
    try:
        return int(sys.argv[1])
    except:
        print("Grade is missing as argument.")
        sys.exit(1)

def get_sample_amount():
    try:
        return int(sys.argv[2])
    except IndexError:
        return 100
    except ValueError:
        return 100

def get_filename():
    try:
        int(sys.argv[3])
    except IndexError:
        try:
            int(sys.argv[2])
            return "samples"
        except IndexError:
            return "samples"
        except:
            return sys.argv[2]
    except:
        return sys.argv[3]

if __name__ == "__main__":
    argc = len(sys.argv)
    if argc == 1:
        print("Usage: ./main.py [grade [amount [output]]")
        sys.exit(0)

    grade = get_grade()
    samples = get_sample_amount()
    filename = get_filename()

    scalar = 3000

    with open(filename, "w") as f:
        for i in range(samples):
            matrix = np.random.rand(grade, grade) * scalar
            constants = np.random.rand(grade, 1) * scalar
            unknowns = np.linalg.solve(matrix, constants)

            f.write("%i\n"%grade)

            for (index, row) in enumerate(matrix):
                f.write(" ".join(map(str, row)))
                f.write(" %i\n"%constants[index])

            f.write(" ".join(map(lambda u : str(u[0]), unknowns)))
            f.write("\n")
