from pomegranate.bayesian_network import BayesianNetwork
import csv
import sys

###fits data to our bayesian network, prints CPD at index.
def fit_data(path,index):
    ###Basic Structure of Network where each index in list represents a node and each tuple is its parents
    #Season, Rain, Sprinkler, Wet, Slippery, Fall
    structure = [(),(0,),(0,),(1,2),(3,),(4,)]


    ###create test_model with structure
    test_model = BayesianNetwork(structure = structure)

    ###set path to csv file to import data
    path = path

    ###import data in usable format
    array = []
    with open(path, 'r') as data:
        csv_reader = csv.reader(data)

        next(csv_reader)
        
        for row in csv_reader:
            row_int = [int(float(value)) for value in row]
            array.append(row_int)

    ###fit Bayesian Network to data
    test_model.fit(array)

    categories = ['season','rain','sprinkler','wet','slippery','fall']
    print("Printing tensor for", categories[index],)
    print('==========================')
    print(test_model.distributions[index].probs[0])

### args are path to csv_file, list of indices to change, values to replace indices with in same order.  If indices do not match, will not produce correct result.
def replace_index(csv_file, index_list, replace_value_list):
    # Open the CSV file for reading and create a CSV reader
    with open(csv_file, 'r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)

    num_columns = len(rows[0])

    # Iterate through each row and replace the values at the specified index
    for x in range(len(index_list)):
        for row in range(1, len(rows)):
            for i in range(index_list[x], num_columns, 5):
                rows[row][i] = replace_value_list[x]

    # Write the updated rows to a new CSV file
    
    # name1 = ''
    # name2 = ''

    # for i in index_list:
    #     name1 = name1 + str(i)
    
    # for j in replace_value_list:
    #     name2 = name2 + str(j)
    #with open(str(csv_file[0:-5])+name1+'='+name2, 'w', newline='') as file:
    with open("temp_dataset", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print("Replacement completed. Output written to temp_dataset")

def test_pomegranate(file_name):
    ##################################################################################################
     #                                             TESTING
    ##################################################################################################
    print("=================================== SCENARIO 1 =====================================")
    
    # ===========================  SCENARIO 1 ===============================================
    #MAIN IDEA: Rain and Slippery are Dependent on Each other, until they are conditioned on Wet which is 
    #           a blocking node, making Rain and Slippery Dependent
    
    print("SCENARIO 1: Rain and Slippery Should be DEPENDENT ===========================================")
    replace_index(file_name, [1],[0])
    print('Slippery | Rain = 0')
    print('========================')
    fit_data("temp_dataset", 4)
    
    print()

    replace_index(file_name, [1],[1])
    print('Slippery | Rain = 1')
    print('========================')
    fit_data("temp_dataset", 4)
    print()
    
    replace_index(file_name, [1],[2])
    print('Slippery | Rain = 2')
    print('========================')
    fit_data("temp_dataset", 4)
    
    print()
    print("SCENARIO 1: Rain and Slippery Should be INDEPENDENT ===========================================")
    replace_index(file_name, [1,3],[0,2])
    print("Slippery | Rain = 0, Wet = 2")
    print('========================')
    fit_data("temp_dataset", 4)
    
    print()

    replace_index(file_name, [1,3],[1,2])
    print("Slippery | Rain = 1, Wet = 2")
    print('========================')
    fit_data("temp_dataset", 4)
    
    print()

    replace_index(file_name, [1,3],[2,2])
    print("Slippery | Rain = 2, Wet = 2")
    print('========================')
    fit_data("temp_dataset", 4)
    
    print("=================================== SCENARIO 2 =====================================")
    # ===========================  SCENARIO 2 ===============================================
     #MAIN IDEA: Rain and Sprinkler should be dependent on each other naturally. When conditioned 
     #           on Season, they should then be independent
    
    print("SCENARIO 2: Rain and Sprinkler are DEPENDENT when not conditioned on Season=====================")
    
    replace_index(file_name, [1],[0])
    print("Pr(Sprinkler | Rain = 0)")
    print('========================')
    fit_data("temp_dataset", 2)
    
    print()
    
    replace_index(file_name, [1],[1])
    print("Pr(Sprinkler | Rain = 1)")
    print('========================')
    fit_data("temp_dataset", 2)
    
    print()
    
    replace_index(file_name, [1],[2])
    print("Pr(Sprinkler | Rain = 2)")
    print('========================')
    fit_data("temp_dataset", 2)
    
    print()
    print("SCENARIO 2: When Conditioned on Season, they should be INDEPENDENT===============================")
    
    replace_index(file_name, [0, 1],[1, 0])
    print("Pr(Sprinkler | Rain = 0, Season = 1)")
    print('========================')
    fit_data("temp_dataset", 2)
    
    print()
    
    replace_index(file_name, [0, 1],[1, 1])
    print("Pr(Sprinkler | Rain = 1, Season = 1)")
    print('========================')
    fit_data("temp_dataset", 2)
    
    print()
    
    replace_index(file_name, [0, 1],[1, 2])
    print("Pr(Sprinkler | Rain = 2, Season = 1)")
    print('========================')
    fit_data("temp_dataset", 2)
    
    print("=================================== SCENARIO 3 =====================================")
    # ===========================  SCENARIO 3 ===============================================
     #MAIN IDEA: Rain and Sprinkler should be Independent of one another due to blocking path 3, 
     #           but when consitioned on Wet/Slippery or Fall Down, they should no longer be ind.
    
    print("SCENARIO 3: Rain and Sprinkler are INDEPENDENT -- there is a blocking path between them ===============")
    replace_index(file_name, [0,2],[0,1])
    print("Rain | Season = 0, Sprinkler = 1")
    print('========================')
    fit_data("temp_dataset", 1)
    
    print()

    replace_index(file_name, [0,2],[0,0])
    print("Rain | Season = 0, Sprinkler = 0")
    print('========================')
    fit_data("temp_dataset", 1)
    
    print()
    print("SCENARIO 3: Rain and Sprinkler are DEPENDENT conditioned on Fall Down ==================================")
    replace_index(file_name, [0,2,5],[0,1,1])
    print("Rain | Season = 0, Sprinkler = 1, Fall_Down = 1")
    print('========================')
    fit_data("temp_dataset", 1)
    
    print()

    replace_index(file_name, [0,2,5],[0,0,1])
    print("Rain | Season = 0, Sprinkler = 0, Fall_Down = 1")
    print('========================')
    fit_data("temp_dataset", 1)

if __name__ == "__main__":
    with open(f"test.txt", 'w') as sys.stdout:
        test_pomegranate("dataset.csv")
