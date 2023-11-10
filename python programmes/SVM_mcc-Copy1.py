import numpy as np
from sklearn.metrics import precision_recall_curve, confusion_matrix, matthews_corrcoef
k = ["20","21","22","23","24"]
string = "12345"
def create_lists(file_label,file_combo,output_prediction):
    file_label = open(file_label,"r")
    file_combo = open(file_combo,"r")
    output_prediction = open(output_prediction,"r")
    pept_label = []
    lst = []
    mcc = []
    listina = []
    pept_label = []
    for line in file_label:
        pept_label.append(line.strip())
    for line1 in file_combo:
        listina.append(line1.strip())
    for line2 in output_prediction:
        lst.append((line2.strip()).split(","))
    for inde in range(len(lst)):
        mcc.append(matthews_corrcoef(pept_label,lst[inde]))
    return pept_label, listina, mcc
for j in k:
    for i in string:
        l = "pept_label_%s.txt" %i
        c = "combo.txt"
        p = "prediction_round%s_%s.text" %(i,j) 
        pept_label, listina, mcc = create_lists(l,c,p)
        file_mcc = open("mcc_%s_%s.text" %(i,j),"w")
        for el in range(len(mcc)):
            file_mcc.write(str(listina[el]) + " mcc: "+ str(mcc[el]) + "\n")
        file_mcc.write(str(listina[mcc.index(max(mcc))])+ " max mcc:" + str(max(mcc)))
#print("max mcc:" + str(max(mcc)) + " combo: " + str(listina[mcc.index(max(mcc))]))
file_mcc.close()