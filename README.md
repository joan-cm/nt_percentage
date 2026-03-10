Python script to calculate the percentage of each nucleotide in a DNA or RNA sequence.
SVH: Updated code with references, IUPAC sequences, rearranged and mofidied the code. Deleted the loop for checking whether within a sequence there are nucleotides, IUPAC or neither.
SVH: Script fully working from the terminal --> I also corrected a previous mistake of the code I wrote

Doc tests:

python3 nt_percentage.py -s ACTGU

PRINTS: Error: the input sequence is not valid since it contains both T and U


python3 nt_percentage.py -s ACTGT

PRINTS: DNA sequence with 20.0% A, 20.0% C, 20.0% G, 40.0% T


python3 nt_percentage.py -s ACuGU

PRINTS: RNA sequence with 20.0% A, 20.0% C, 20.0% G, 40.0% U


python3 nt_percentage.py -s acgca

PRINTS: Nucleic acid sequence with 40.0% A, 40.0% C, 20.0% G


python3 nt_percentage.py -s ACTGTTT.-.-

PRINTS: DNA sequence with 9.1% A, 9.1% C, 9.1% G, 36.4% T, 0.0% ambigous bases, 36.4% gaps


python3 nt_percentage.py -s ACUGUNNNN.-.-

PRINTS: RNA sequence with 7.7% A, 7.7% C, 7.7% G, 15.4% U, 30.8% ambigous bases, 30.8% gaps


python3 nt_percentage.py -s ACUGU.-.-F

PRINTS: Error: the input sequence contains unexpected bases

