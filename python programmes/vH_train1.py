import math
import numpy as np
from sys import argv

# Open files
#file2 is the output file
file2 = open(argv[2], "w")
#file3 is the text file with the lengths of signal peptides
file3 = open(argv[3], "r")
pept_length = []
lst_sequences = []
#list with indexes short signal peptides to remove from fasta file for the final round
to_remove2 = [306, 366, 406, 582, 583, 759, 762, 827, 925, 936]
for line_length in file3:
    pept_length.append(int(line_length.strip()))

AA_compo_uniprot = {"A": 8.25, "V": 6.85, "L": 9.65, "Q": 3.93, "P": 4.74, "H": 2.27, "S": 6.65, "G": 7.07, "K": 5.80,
                   "E": 6.72, "R": 5.53, "T": 5.36, "I": 5.91, "D": 5.46, "M": 2.41, "N": 4.06, "W": 1.10, "F": 3.86, "Y": 2.92, "C": 1.38}
lst_AA = []
lst_FREQ = []

for i in AA_compo_uniprot.keys():
    lst_AA.append(i)
for j in AA_compo_uniprot:
    lst_FREQ.append(AA_compo_uniprot[j] / 100)

with open(argv[1], "r") as file_training:
    seq = ""
    lst_sequences = []

    for line in file_training:
        line = line.strip()
        if line.startswith(">"):
            if seq:
                lst_sequences.append(seq)
            seq = ""
        else:
            seq += line

    if seq:
        lst_sequences.append(seq)



#use this only with the final round
to_remove2.sort(reverse=True)  # Sort in reverse order
for index in to_remove2:  # Iterate through to_remove2 in reverse order
    if index < len(lst_sequences):
        lst_sequences.pop(index)  # Remove element at the specified index
# Now, lst_sequences contains the elements after removing those at the indices in to_remove2

scores = [[1 for _ in range(len(lst_AA))] for _ in range(15)]
lst_seqs = []
for k in range(len(lst_sequences)):
    if pept_length[k] > 13:
    #if pept_length[k] - 13 >= 0 and pept_length[k] + 2 <= len(lst_sequences[k]):
        lst_seqs.append(lst_sequences[k][pept_length[k] - 14: pept_length[k] + 1])

for w in range(len(lst_seqs)):
    for i in range(len(lst_seqs[w])):
        for j in range(len(lst_AA)):
            if lst_seqs[w][i] == lst_AA[j]:
                scores[i][j] += 1

for i in range(len(lst_AA)):
    for j in range(15):
        scores[j][i] = scores[j][i] / (len(lst_seqs) + 20)
        scores[j][i] = scores[j][i] / lst_FREQ[i]
        scores[j][i] = math.log(scores[j][i])

# Open file2 for writing before using np.savetxt
with open(argv[2], "w") as file2:
    np.savetxt(file2, scores)