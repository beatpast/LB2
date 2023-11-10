from sys import argv
import numpy as np
#file1 contains the sequences of the subset to test, file2 has the matrix with the scores from training and file3 is the result
file2 = open(argv[2], "r")
file3 = open(argv[3], "w")
lst_sequences = []
matrix = []
AA_compo_uniprot= {"A":8.25,"V":6.85,"L":9.65, "Q":3.93,"P":4.74,"H":2.27,"S":6.65,"G":7.07,"K":5.80,"E":6.72,"R":5.53,"T":5.36,"I":5.91,
   "D":5.46, "M":2.41, "N":4.06,  "W":1.10, "F":3.86,"Y":2.92, "C":1.38 }
lst_AA =[]
lst_COMPO =[]
lst_FREQ = []
for i in AA_compo_uniprot.keys():
    lst_AA.append(i)
for j in AA_compo_uniprot:
    lst_FREQ.append(AA_compo_uniprot[j])
for line2 in file2:
    matrix.append(line2.split()) 
#for element in range(len(matrix[0])):
  #  matrix[0][element] = matrix[0][element][:14]
with open(argv[1], "r") as file_training:
    seq = ""
    lst_sequences = []
    
    # Read the file line by line
    for line in file_training:
        line = line.strip()
        if line.startswith(">"):
            # Store the previous sequence if it's not empty
            if seq:
                lst_sequences.append(seq)
            # Start a new sequence
            seq = ""
        else:
            seq += line

    # Append the last sequence
    if seq:
        lst_sequences.append(seq)
# Define the function to predict scores for a subsequence
def predict(sequence, score_matrix):
    score = []
    scores_sum = []
    for index in range(0,min(90,len(sequence))-15+1):
        for i in range(15):
            for j in range(20):
                if sequence[index:index+15][i] == lst_AA[j]:
                    score.append(float(score_matrix[i][j]))
    for ind in range(0,min(90,len(score))-15+1):
        scores_sum.append(sum(score[ind:ind+14]))
    return max(scores_sum)

maximum_score = []

# Loop through protein sequences
for k in range(len(lst_sequences)):
    sequence_scores = predict(lst_sequences[k], matrix)
    maximum_score.append(sequence_scores)
for maxim in range(len(maximum_score)):
    file3.write(str(maximum_score[maxim])+"\n")

# Close the files
file2.close()
file3.close()




	