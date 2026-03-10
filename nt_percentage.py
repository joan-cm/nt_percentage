#!/usr/bin/env python3

# Includes Joan's v1 of script + Sonia's changes: IUPAC + modification script
# References conditions code: https://www.w3schools.com/python/python_conditions.asp
# Reference IUPAC code: https://www.bioinformatics.org/sms/iupac.html
# References sys: https://www.w3schools.com/python/ref_module_sys.asp AND https://docs.python.org/3/library/sys.html
# References argparse: https://docs.python.org/es/3/library/argparse.html

## Libraries
import sys
from argparse import ArgumentParser

## Argument parsing
parser = ArgumentParser(description = 'Calculate nucleotide percentage') # description displayed in the help message
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence") # as input, one argument is required and it needs to be a string

# Quality checks
# Did the user include all arguments?
# checks whether the user included an argument

if len(sys.argv) == 1:
    print("Percentage not computed. Missing argument")
    parser.print_help() 
    sys.exit(1) # exits printing the message

# args needed since the parser arguments were added
args = parser.parse_args()

# Prepares sequence, add args arguments to the start of the sequence!
args.seq = args.seq.upper()


## Run

# Prepares sequence
args.seq = args.seq.upper()

# Computes counts and percentages
# Adds IUPAC code
length = len(args.seq)
num_a = args.seq.count("A")
num_c = args.seq.count("C")
num_g = args.seq.count("G")
num_t = args.seq.count("T")
num_u = args.seq.count("U")
num_ambigous = args.seq.count("R") + args.seq.count("Y") + args.seq.count("S") + args.seq.count("W") + args.seq.count("K") + args.seq.count("M") + args.seq.count("B") + args.seq.count("D") + args.seq.count("H") + args.seq.count("V") + args.seq.count("N")
num_gap = args.seq.count(".") + args.seq.count("-")
per_a = round((num_a / length) * 100, 1)
per_c = round((num_c / length) * 100, 1)
per_g = round((num_g / length) * 100, 1)
per_t = round((num_t / length) * 100, 1)
per_u = round((num_u / length) * 100, 1)
per_ambigous = round((num_ambigous / length) * 100, 1)
per_gap = round((num_gap / length) * 100, 1)

# considers whether there are T and U in the same sequence: Mistake
if "T" in args.seq and "U" in args.seq:
     print("Error: the input sequence is not valid since it contains both T and U.")
     sys.exit(1)

# for checking if bases are included within the IUPAC code
nucleotides = {"A", "T", "C", "G", "U"}
IUPAC = {"R", "Y", "S", "W", "K", "M", "B", "D", "H", "V", "N", ".", "-"}

# identifies sequences that have bases in nucleotides, IUPAC and in neither (will print an error for the last scenario, see below)
# Check reference for the if statement
IUPAC_sequence = (num_ambigous + num_gap) > 0
nucleotides_sequence = (num_a + num_c + num_g + num_t + num_u) > 0
bases_sequence = (IUPAC_sequence + nucleotides_sequence) > 0

# Considers two scenarios: When there is a T or a U. Considers whether the sequence includes IUPAC bases or not.
if "T" in args.seq:
    if IUPAC_sequence:
        print(f"DNA sequence with {per_a}% A, {per_c}% C, {per_g}% G, {per_t}% T, {per_ambigous}% ambigous bases, {per_gap}% gaps")
    else:
        print(f"DNA sequence with {per_a}% A, {per_c}% C, {per_g}% G, {per_t}% T")

elif "U" in args.seq:
    if IUPAC_sequence:
        print(f"RNA sequence with {per_a}% A, {per_c}% C, {per_g}% G, {per_u}% U, {per_ambigous}% ambigous bases, {per_gap}% gaps")
    else:
        print(f"RNA sequence with {per_a}% A, {per_c}% C, {per_g}% G, {per_u}% U")

# No T and no U. Takes into account whether the bases are within nucleotides or IUPAC. Otherwise prints an error message.
else:
    if bases_sequence == False:
        print(f"Error: the input sequence contains unexpected bases")
    elif IUPAC_sequence:
        print(f"Nucleic acid sequence with {per_a}% A, {per_c}% C, {per_g}% G, {per_ambigous}% ambigous bases, {per_gap}% gaps")   
    else:
        print(f"Nucleic acid sequence with {per_a}% A, {per_c}% C, {per_g}% G")
