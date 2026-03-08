# Includes Joan's v1 of script + Sonia's changes: IUPAC + modification script
# References conditions code: https://www.w3schools.com/python/python_conditions.asp
# Reference IUPAC code: https://www.bioinformatics.org/sms/iupac.html

# Prepares sequence
seq = seq.upper()  

# Computes counts and percentages
# Adds IUPAC code
length = len(seq)
num_a = seq.count("A")
num_c = seq.count("C")
num_g = seq.count("G")
num_t = seq.count("T")
num_u = seq.count("U")
num_ambigous = seq.count("R") + seq.count("Y") + seq.count("S") + seq.count("W") + seq.count("K") + seq.count("M") + seq.count("B") + seq.count("D") + seq.count("H") + seq.count("V") + seq.count("N")
num_gap = seq.count(".") + seq.count("-")
per_a = round((num_a / length) * 100, 1)
per_c = round((num_c / length) * 100, 1)
per_g = round((num_g / length) * 100, 1)
per_t = round((num_t / length) * 100, 1)
per_u = round((num_u / length) * 100, 1)
per_ambigous = round((num_ambigous / length) * 100, 1)
per_gap = round((num_gap / length) * 100, 1)

# considers whether there are T and U in the same sequence: Mistake
if "T" in seq and "U" in seq:
     print("Error: the input sequence is not valid since it contains both T and U.")
     #sys.exit(1)

# for checking if bases are included within the IUPAC code
nucleotides = {"A", "T", "C", "G", "U"}
IUPAC = {"R", "Y", "S", "W", "K", "M", "B", "D", "H", "V", "N", ".", "-"}

# identifies sequences that have bases in nucleotides and IUPAC
# 
# Check reference for the if statement
IUPAC_sequence = (num_ambigous + num_gap) > 0
nucleotides_sequence = (num_a + num_c + num_g + num_t + num_u) > 0
bases_sequence = (IUPAC_sequence + nucleotides_sequence) > 0

# Considers two scenarios: When there is a T or a U. 
if "T" in seq:
    if IUPAC_sequence:
        print(f"DNA sequence with {per_a}% A, {per_c}% C, {per_g}% G, {per_t}% T, {per_ambigous}% ambigous bases, {per_gap}% gaps")
    else:
        print(f"DNA sequence with {per_a}% A, {per_c}% C, {per_g}% G, {per_t}% T")

elif "U" in seq:
    if IUPAC_sequence:
        print(f"RNA sequence with {per_a}% A, {per_c}% C, {per_g}% G, {per_u}% U, {per_ambigous}% ambigous bases, {per_gap}% gaps")
    else:
        print(f"RNA sequence with {per_a}% A, {per_c}% C, {per_g}% G, {per_u}% U")

else:
    if bases_sequence == False:
        print(f"Error: the input sequence contains unexpected bases")
    elif IUPAC_sequence:
        print(f"Nucleic acid sequence with {per_a}% A, {per_c}% C, {per_g}% G, {per_ambigous}% ambigous bases, {per_gap}% gaps")   
    else:
        print(f"Nucleic acid sequence with {per_a}% A, {per_c}% C, {per_g}% G")
