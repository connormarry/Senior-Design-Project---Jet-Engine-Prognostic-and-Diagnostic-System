import csv

### args are path to csv_file, list of indices to change, values to replace indices with in same order.  If indices do not match, will not produce correct result.
def replace_index(csv_file, index_list, replace_value_list):
    # Open the CSV file for reading and create a CSV reader
    with open(csv_file, 'r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)

    num_columns = len(rows[0])

    # Iterate through each row and replace the values at the specified index
    for x in range(len(index_list)):

        for row in rows:
            for i in range(index_list[x], num_columns, 5):
                row[i] = replace_value_list[x]

    # Write the updated rows to a new CSV file
    
    name1 = ''
    name2 = ''

    for i in index_list:
        name1 = name1 + str(i)
    
    for j in replace_value_list:
        name2 = name2 + str(j)
    with open(str(csv_file[0:-5])+name1+'='+name2, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print("Replacement completed. Output written to",str(csv_file[0:-5])+name1+'='+name2)


if __name__ == '__main__':
    #Season = 0, Rain = 1, Sprinkler = 2, Wet = 3, Slippery = 4, Fall = 5
    ###Creating csvs for scenario 1 
    replace_index("C:\\Users\\Chillow\\Data_Sets\\High_Noise_Dataset.txt", [1],[0])
    replace_index("C:\\Users\\Chillow\\Data_Sets\\High_Noise_Dataset.txt", [1],[1])
    replace_index("C:\\Users\\Chillow\\Data_Sets\\High_Noise_Dataset.txt", [1],[2])

    replace_index("C:\\Users\\Chillow\\Data_Sets\\Low_Noise_Dataset.txt", [1],[0])
    replace_index("C:\\Users\\Chillow\\Data_Sets\\Low_Noise_Dataset.txt", [1],[1])
    replace_index("C:\\Users\\Chillow\\Data_Sets\\Low_Noise_Dataset.txt", [1],[2])

    replace_index("C:\\Users\\Chillow\\Data_Sets\\Mid_Noise_Dataset.txt", [1],[0])
    replace_index("C:\\Users\\Chillow\\Data_Sets\\Mid_Noise_Dataset.txt", [1],[1])
    replace_index("C:\\Users\\Chillow\\Data_Sets\\Mid_Noise_Dataset.txt", [1],[2])


    ###Creating csvs for scenario 2
    replace_index("C:\\Users\\Chillow\\Data_Sets\\High_Noise_Dataset.txt", [1,3],[0,2])
    replace_index("C:\\Users\\Chillow\\Data_Sets\\High_Noise_Dataset.txt", [1,3],[1,2])
    replace_index("C:\\Users\\Chillow\\Data_Sets\\High_Noise_Dataset.txt", [1,3],[2,2])

    replace_index("C:\\Users\\Chillow\\Data_Sets\\Low_Noise_Dataset.txt", [1,3],[0,2])
    replace_index("C:\\Users\\Chillow\\Data_Sets\\Low_Noise_Dataset.txt", [1,3],[1,2])
    replace_index("C:\\Users\\Chillow\\Data_Sets\\Low_Noise_Dataset.txt", [1,3],[2,2])

    replace_index("C:\\Users\\Chillow\\Data_Sets\\Mid_Noise_Dataset.txt", [1,3],[0,2])
    replace_index("C:\\Users\\Chillow\\Data_Sets\\Mid_Noise_Dataset.txt", [1,3],[1,2])
    replace_index("C:\\Users\\Chillow\\Data_Sets\\Mid_Noise_Dataset.txt", [1,3],[2,2])

    ###Creating csvs for scenario 3

    replace_index("C:\\Users\\Chillow\\Data_Sets\\High_Noise_Dataset.txt", [0,2],[0,1])
    replace_index("C:\\Users\\Chillow\\Data_Sets\\High_Noise_Dataset.txt", [2],[0])
    replace_index("C:\\Users\\Chillow\\Data_Sets\\High_Noise_Dataset.txt", [0,2,5],[0,1,1])
    replace_index("C:\\Users\\Chillow\\Data_Sets\\High_Noise_Dataset.txt", [2,5],[0,1])

    replace_index("C:\\Users\\Chillow\\Data_Sets\\Mid_Noise_Dataset.txt", [0,2],[0,1])
    replace_index("C:\\Users\\Chillow\\Data_Sets\\Mid_Noise_Dataset.txt", [2],[0])
    replace_index("C:\\Users\\Chillow\\Data_Sets\\Mid_Noise_Dataset.txt", [0,2,5],[0,1,1])
    replace_index("C:\\Users\\Chillow\\Data_Sets\\Mid_Noise_Dataset.txt", [2,5],[0,1])

    replace_index("C:\\Users\\Chillow\\Data_Sets\\Low_Noise_Dataset.txt", [0,2],[0,1])
    replace_index("C:\\Users\\Chillow\\Data_Sets\\Low_Noise_Dataset.txt", [2],[0])
    replace_index("C:\\Users\\Chillow\\Data_Sets\\Low_Noise_Dataset.txt", [0,2,5],[0,1,1])
    replace_index("C:\\Users\\Chillow\\Data_Sets\\Low_Noise_Dataset.txt", [2,5],[0,1])