k = ["20","21","22","23","24"]
string = "12345"
file_best_combo = open("all_combinations_all_rounds.text","w")
def best_combo_concatenate(best_combo, k):
    best_combo = "k:" + k + " " + best_combo 
    return best_combo
def create_lists(file_mcc):
    file_mcc = open(file_mcc,"r")
    combos = []
    for line in file_mcc:
        combos.append(line.strip())
        best_combo = combos[-1] 
    return best_combo
for i in string:
    for j in k:
        results =[]
        best_combo = create_lists("mcc_%s_%s.text" %(i,j))
        results.append( best_combo_concatenate(best_combo, j))
        file_best_combo.write("round%s" %(i) + str(results) + "\n") 
file_best_combo.close()