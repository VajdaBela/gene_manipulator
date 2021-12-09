#!/usr/bin/python3
import sys

#sequence is genomial only if all of its genes are one of A C T or G
possible_genes = ['A', 'C', 'T', 'G']

if __name__ == "__main__":
    if not len(sys.argv) == 2:
        print("Usage: chkgen.py <file>")
        sys.exit(1)


    in_file = sys.argv[1]
    in_file = open(in_file, "r")
    sequence = in_file.read().strip()
    in_file.close()

    is_genomial = all([x in possible_genes for x in sequence])

    if is_genomial == True:
        print("is genomial")
    else:
        print("is not genomial")
    sys.exit(0)

