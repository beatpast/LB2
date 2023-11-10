from sys import argv
import numpy as np
# Import the svm module
from sklearn import svm
from sklearn.metrics import precision_recall_curve, confusion_matrix, matthews_corrcoef
k = ["20","21","22","23","24"]
C = [1,2,4,8]
gamma = [0.5,1,2,"scale"]
cross = ["234","034","014","012","123"] 
string = "12345"
#file contains the matrix from cross validation dataset, file_pept_label contains the labeling [0,1] and file2 the matrix from validation dataset
def create_lists(file,file_pept_label,file2):
    file = open(file,"r")
    file_pept_label = open(file_pept_label,"r")
    file2 = open(file2,"r")
    X_train =[]
    X_test = []
    pept_label = []
    for label in file_pept_label:
        pept_label.append(int(label.strip()))
    for element in file:
        X_train.append(element.split())
    for elemento in range(len(X_train[0])):
        X_train[0][elemento] = float(X_train[0][elemento])
    for element2 in file2:
        X_test.append(element2.split())
    return X_train, pept_label, X_test
def array_values(X_train, pept_label, X_test, i, j):
    mySVC = svm.SVC(C=i, kernel='rbf', gamma=j)
    # Train (fit) the model on training data
    mySVC.fit(X_train, pept_label)
    # Predict classes on validation data
    # Write the predictions and parameters to the output file
    return np.array(mySVC.predict(X_test))
for j in k:
    for i in string:
        t = "X__hp_train%s_%s.text" %(j,i)
        l = "pept_label_%s.txt" %cross[string.index(i)]
        s = "X__hp_test%s_%s.text" %(j,i) 
        X_train, pept_label, X_test = create_lists(t,l,s)
        arrays = []
        lst = []
        for elem in C:
            for elem1 in gamma:
                array = array_values(X_train, pept_label, X_test, elem, elem1)
                arrays.append(array)
                combination = 'C:%s ' %elem + "gamma:%s " %elem1
                lst.append(combination)
                np.savetxt("prediction_round%s_%s.text" %(i,j), arrays, fmt='%d', delimiter=',')
                combo = open("combo.txt", "w")
                for item in lst:
                    combo.write(str(item) + "\n")
combo.close()