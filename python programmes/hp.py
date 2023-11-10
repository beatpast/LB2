### this code finds the position of the maximum value of hydrophobicity for each protein
from sys import argv
import numpy as np
import pandas as pd
from Bio.SeqUtils.ProtParam import ProteinAnalysis
kd = {"A": 1.8, "R": -4.5, "N": -3.5, "D": -3.5, "C": 2.5,
      "Q": -3.5, "E": -3.5, "G": -0.4, "H": -3.2, "I": 4.5,
      "L": 3.8, "K": -3.9, "M": 1.9, "F": 2.8, "P": -1.6,
      "S": -0.8, "T": -0.7, "W": -0.9, "Y": -1.3, "V": 4.2, "X":0.00, "Z":0.00,"U":0.00, "B":0.00}
vectors = []
k = int(argv[2])
def hp(sequence,k):
    new_sequence = "XX" + sequence + "XX"
    pa=ProteinAnalysis(new_sequence)
    hp = pa.protein_scale(kd, 5)
    average = sum(hp)/len(hp)
    return hp.index(max(hp))/k
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
    vector = hp(lst_sequences[index][:k],k)
    vectors.append(vector)
with open(argv[3], "w") as file2:
    np.savetxt(file2, vectors)