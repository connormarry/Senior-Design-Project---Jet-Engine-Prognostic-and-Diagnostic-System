

###fits data to our bayesian network, prints CPD at index.
def fit_data(path,index):


    from pomegranate.bayesian_network import BayesianNetwork
    import csv

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



if __name__ == '__main__':
    ###season = 0, rain = 1, sprinkler = 2, wet = 3, slippery = 4, fall = 5
    ###Each path is a csv with interventions made on the dataset according to the conditional probability statement above it.
    ###CSV creation was done using intervene.py
    print('High Noise Tests:')
    print('=================')
    print()
    print()

    print('Slippery | Rain = 0')
    print('==================')
    fit_data("C:\\Users\\Chillow\\Data_Sets\\High_Noise_Datase1=0",4)
    
    print()

    print('Slippery | Rain = 1')
    print('==================')
    fit_data("C:\\Users\\Chillow\\Data_Sets\\High_Noise_Datase1=1",4)
    print()

    print('Slippery | Rain = 2')
    print('==================')
    fit_data("C:\\Users\\Chillow\\Data_Sets\\High_Noise_Datase1=2",4)
    
    print()

    print("Slippery | Rain = 0, Wet = 2")
    print('==================')
    fit_data("C:\\Users\\Chillow\\Data_Sets\\High_Noise_Datase13=02",4)
    
    print()

    print("Slippery | Rain = 1, Wet = 2")
    print('==================')
    fit_data("C:\\Users\\Chillow\\Data_Sets\\High_Noise_Datase13=12",4)
    
    print()

    print("Slippery | Rain = 2, Wet = 2")
    print('==================')
    fit_data("C:\\Users\\Chillow\\Data_Sets\\High_Noise_Datase13=22",4)
    
    print()

    print("Rain | Season = 0, Sprinkler = 1")
    print('==================')
    fit_data("C:\\Users\\Chillow\\Data_Sets\\High_Noise_Datase02=01",1)
    
    print()

    print("Rain | Sprinkler = 0")
    print('==================')
    fit_data("C:\\Users\\Chillow\\Data_Sets\\High_Noise_Datase2=0",1)
    
    print()

    print("Rain | Season = 0, Sprinkler = 1, Fall_Down = 1")
    print('==================')
    fit_data("C:\\Users\\Chillow\\Data_Sets\\High_Noise_Datase025=011",1)
    
    print()

    print("Rain | Sprinkler = 0, Fall_Down = 1")
    print('==================')
    fit_data("C:\\Users\\Chillow\\Data_Sets\\High_Noise_Datase25=01",1)
    
    print()

    print('=================')
    print('=================')
    print('=================')
    print('=================')
    print('=================')

    print('Mid Noise Tests:')
    print('=================')
    print()
    print()

    print('Slippery | Rain = 0')
    print('==================')
    fit_data("C:\\Users\\Chillow\\Data_Sets\\Mid_Noise_Datase1=0",4)
    
    print()

    print('Slippery | Rain = 1')
    print('==================')
    fit_data("C:\\Users\\Chillow\\Data_Sets\\Mid_Noise_Datase1=1",4)
    print()

    print('Slippery | Rain = 2')
    print('==================')
    fit_data("C:\\Users\\Chillow\\Data_Sets\\Mid_Noise_Datase1=2",4)
    
    print()

    print("Slippery | Rain = 0, Wet = 2")
    print('==================')
    fit_data("C:\\Users\\Chillow\\Data_Sets\\Mid_Noise_Datase13=02",4)
    
    print()

    print("Slippery | Rain = 1, Wet = 2")
    print('==================')
    fit_data("C:\\Users\\Chillow\\Data_Sets\\Mid_Noise_Datase13=12",4)
    
    print()

    print("Slippery | Rain = 2, Wet = 2")
    print('==================')
    fit_data("C:\\Users\\Chillow\\Data_Sets\\Mid_Noise_Datase13=22",4)
    
    print()

    print("Rain | Season = 0, Sprinkler = 1")
    print('==================')
    fit_data("C:\\Users\\Chillow\\Data_Sets\\Mid_Noise_Datase02=01",1)
    
    print()

    print("Rain | Sprinkler = 0")
    print('==================')
    fit_data("C:\\Users\\Chillow\\Data_Sets\\Mid_Noise_Datase2=0",1)
    
    print()

    print("Rain | Season = 0, Sprinkler = 1, Fall_Down = 1")
    print('==================')
    fit_data("C:\\Users\\Chillow\\Data_Sets\\Mid_Noise_Datase025=011",1)
    
    print()

    print("Rain | Sprinkler = 0, Fall_Down = 1")
    print('==================')
    fit_data("C:\\Users\\Chillow\\Data_Sets\\Mid_Noise_Datase25=01",1)
    
    print()
    print('=================')
    print('=================')
    print('=================')
    print('=================')
    print('=================')

    print('Low Noise Tests:')
    print('=================')
    print()
    print()

    print('Slippery | Rain = 0')
    print('==================')
    fit_data("C:\\Users\\Chillow\\Data_Sets\\Low_Noise_Datase1=0",4)
    
    print()

    print('Slippery | Rain = 1')
    print('==================')
    fit_data("C:\\Users\\Chillow\\Data_Sets\\Low_Noise_Datase1=1",4)
    print()

    print('Slippery | Rain = 2')
    print('==================')
    fit_data("C:\\Users\\Chillow\\Data_Sets\\Low_Noise_Datase1=2",4)
    
    print()

    print("Slippery | Rain = 0, Wet = 2")
    print('==================')
    fit_data("C:\\Users\\Chillow\\Data_Sets\\Low_Noise_Datase13=02",4)
    
    print()

    print("Slippery | Rain = 1, Wet = 2")
    print('==================')
    fit_data("C:\\Users\\Chillow\\Data_Sets\\Low_Noise_Datase13=12",4)
    
    print()

    print("Slippery | Rain = 2, Wet = 2")
    print('==================')
    fit_data("C:\\Users\\Chillow\\Data_Sets\\Low_Noise_Datase13=22",4)
    
    print()

    print("Rain | Season = 0, Sprinkler = 1")
    print('==================')
    fit_data("C:\\Users\\Chillow\\Data_Sets\\Low_Noise_Datase02=01",1)
    
    print()

    print("Rain | Sprinkler = 0")
    print('==================')
    fit_data("C:\\Users\\Chillow\\Data_Sets\\Low_Noise_Datase2=0",1)
    
    print()

    print("Rain | Season = 0, Sprinkler = 1, Fall_Down = 1")
    print('==================')
    fit_data("C:\\Users\\Chillow\\Data_Sets\\Low_Noise_Datase025=011",1)
    
    print()

    print("Rain | Sprinkler = 0, Fall_Down = 1")
    print('==================')
    fit_data("C:\\Users\\Chillow\\Data_Sets\\Low_Noise_Datase25=01",1)  