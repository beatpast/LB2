from sys import argv
import numpy as np
from sklearn import preprocessing
vectors = []
k = int(argv[2])
hp_vectors = open(argv[4], "r")
hp_vectors2 = open(argv[5], "r")
average_hp = []
max_hp = []
for element in hp_vectors2:
    max_hp.append(element.split())
X_train = np.array(max_hp)
min_max_scaler = preprocessing.MinMaxScaler()
X_train_minmax = min_max_scaler.fit_transform(X_train)
for element in hp_vectors:
    average_hp.append(element.split())
X_train = np.array(average_hp)
min_max_scaler1 = preprocessing.MinMaxScaler()
X_train_minmax1 = min_max_scaler.fit_transform(X_train)
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
for i in range(len(vectors)):
    vectors[i].append(float(X_train_minmax[i]))
    vectors[i].append(float(X_train_minmax1[i]))
with open(argv[3], "w") as file2:
    np.savetxt(file2, vectors)