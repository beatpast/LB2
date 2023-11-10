from sys import argv
import numpy as np
vectors = []
k = int(argv[2])
def frequency(sequence):
    aa_frequency = {}
    lst_freq = []
    residues = "GAVPLIMFWYSTCNQHDEKR"
    for aa in residues:
        aa_frequency[aa] = 0
        if aa in sequence:
            aa_frequency[aa] = sequence.count(aa)
    for i in aa_frequency:
        lst_freq.append((aa_frequency[i]/sum(aa_frequency.values())))
    return lst_freq
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
for index in range(len(lst_sequences)):
    vector = frequency(lst_sequences[index][:k])
    vectors.append(vector)
with open(argv[3], "w") as file2:
    np.savetxt(file2, vectors)