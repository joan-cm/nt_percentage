seq = seq.upper()

characters = {"A", "C", "G", "T", "U"}
for nt in seq:
    if nt not in characters:
        print("Error: the input sequence contains unexpected characters.")

length = len(seq)
num_a = seq.count("A")
num_c = seq.count("C")
num_g = seq.count("G")
per_a = round((num_a / length) * 100, 1)
per_c = round((num_c / length) * 100, 1)
per_g = round((num_g / length) * 100, 1)

if "T" in seq and "U" in seq:
    print("Error: the input sequence is not valid since it contains both T and U.")

elif "T" in seq:
    num_t = seq.count("T")
    per_t = round((num_t / length) * 100, 1)
    print(f"DNA sequence with {per_a}% A, {per_c}% C, {per_g}% G, {per_t}% T")

elif "U" in seq:
    num_u = seq.count("U")
    per_u = round((num_u / length) * 100, 1)
    print(f"RNA sequence with {per_a}% A, {per_c}% C, {per_g}% G, {per_u}% U")

else:
    print(f"Nucleic acid sequence with {per_a}% A, {per_c}% C, {per_g}% G")
