import bnlearn as bn
import numpy as np
import pandas as pd
import sys
import os

def bnLearn_Tests(file_name):
     #turn csv file into a pandas dataframe
     df = pd.read_csv(file_name)
     #print(df)

     #create a network and structure learn the network on the dataset
     edges = [
          ("Season", "Rain"),
          ("Season", "Sprinkler"),
          ("Rain", "Wet"),
          ("Sprinkler", "Wet"),
          ("Wet", "Slippery"), 
          ("Slippery", "Fall_Down")
     ]
     DAG = bn.make_DAG(edges)
     #bn.plot(DAG)

     #fit the data in the dataframe to the model and plot the model
     model = bn.parameter_learning.fit(DAG, df)

     bn.plot(model)
     #bn.plot(model, interactive=True)

     ##################################################################################################
     #                                             TESTING
     ##################################################################################################

     #Compute Indepedence Test on the model 
     ## Any two nodes are associated in the model if the p value < significance value 
     ## Prints results of the independence test 
     print("Independence Test Results")
     independenceModel = bn.independence_test(model, df, test='chi_square')
     print(independenceModel['independence_test'])
     print()

     #===============  Conditional Testing -- Pr(Rain || Sprinkler), Pr(Sprinkler || Rain) =============
     #Key Idea: Rain and Sprinkler are Independent of Each Other 
     print("Pr(Rain || Sprinkler), Pr(Sprinkler || Rain)")
     print()
     #Sprinkler On
     print("Pr(Rain|Season=0, Sprinkler = 1)")
     rSp = bn.inference.fit(model, variables=['Rain'], evidence={'Season': 0.0, 
                                                                 'Sprinkler': 1})
     #sprinkler Off
     print("Pr(Rain|Season=0, Sprinkler = 0)")
     rSp1 = bn.inference.fit(model, variables=['Rain'], evidence={'Season': 0.0,
                                                                 'Sprinkler': 0})

     print()
     #Rain On
     print("Pr(Sprinkler|Season=0, Rain = 1)")
     spR = bn.inference.fit(model, variables=['Sprinkler'], evidence= {'Season': 0.0, 
                                                                      'Rain': 1})
     #Rain Off
     print("Pr(Sprinkler|Season=0, Rain = 0)")
     spR2 = bn.inference.fit(model, variables=['Sprinkler'], evidence={'Season': 0.0, 
                                                                      'Rain': 0})

     #===============   Seperation Theorems: Conditional Independence Between Nodes  ===================

     # ===========================  SCENARIO 1 ===============================================
     #MAIN IDEA: Rain and Slippery are Dependent on Each other, until they are conditioned on Wet which is 
     #           a blocking node, making Rain and Slippery Dependent
     print()
     print("SCENARIO 1: Rain and Slippery Should be DEPENDENT ===========================================")
     print("Pr(Slippery | Rain = 0)")
     slR = bn.inference.fit(model, variables=['Slippery'], evidence={'Rain': 0})
     print()
     print("Pr(Slippery | Rain = 1)")
     slR = bn.inference.fit(model, variables=['Slippery'], evidence={'Rain': 1})
     print()
     print("Pr(Slippery | Rain = 2)")
     slR = bn.inference.fit(model, variables=['Slippery'], evidence={'Rain': 2})
     
     #Now, we specify a blocking node of Wet -- Rain and Slippery should not be independent 
     print()
     print("SCENARIO 1: Rain and Slippery Should be INDEPENDENT ===========================================")
     print("Pr(Slippery | Rain = 0, Wet = 2)")
     slR = bn.inference.fit(model, variables=['Slippery'], evidence={'Wet': 2, 
                                                                      'Rain': 0})
     print()
     print("Pr(Slippery | Rain = 1, Wet = 2)")
     slR = bn.inference.fit(model, variables=['Slippery'], evidence={'Wet': 2, 
                                                                     'Rain': 1})
     print()
     print("Pr(Slippery | Rain = 2, Wet = 2)")
     slR = bn.inference.fit(model, variables=['Slippery'], evidence={'Wet': 2, 
                                                                     'Rain': 2})

     # ===========================  SCENARIO 2 ===============================================
     #MAIN IDEA: Rain and Sprinkler should be dependent on each other naturally. When conditioned 
     #           on Season, they should then be independent
     
     print("SCENARIO 2: Rain and Sprinkler are DEPENDENT when not conditioned on Season=====================")
     print()
     
     #Rain = 0
     print("Pr(Sprinkler | Rain = 0)")
     rSp = bn.inference.fit(model, variables=['Sprinkler'], evidence={'Rain': 0})
     #Rain = 1
     print("Pr(Sprinkler | Rain = 1)")
     rSp = bn.inference.fit(model, variables=['Sprinkler'], evidence={'Rain': 1})
     #Rain = 2
     print("Pr(Sprinkler | Rain = 2)")
     rSp = bn.inference.fit(model, variables=['Sprinkler'], evidence={'Rain': 2})

     print()
     print("SCENARIO 2: When Conditioned on Season, they should be INDEPENDENT===============================")
     #Rain = 0
     print("Pr(Sprinkler | Rain = 0, Season = 1)")
     rSp = bn.inference.fit(model, variables=['Sprinkler'], evidence={'Season': 1,
                                                                      'Rain': 0})
     #Rain = 1
     print("Pr(Sprinkler | Rain = 1)")
     rSp = bn.inference.fit(model, variables=['Sprinkler'], evidence={'Season': 1,
                                                                      'Rain': 1})
     #Rain = 2
     print("Pr(Sprinkler | Rain = 2)")
     rSp = bn.inference.fit(model, variables=['Sprinkler'], evidence={'Season': 1,
                                                                      'Rain': 2})
     
     # ===========================  SCENARIO 3 ===============================================
     #MAIN IDEA: Rain and Sprinkler should be Independent of one another due to blocking path 3, 
     #           but when consitioned on Wet/Slippery or Fall Down, they should no longer be ind.

     print("SCENARIO 3: Rain and Sprinkler are INDEPENDENT -- there is a blocking path between them===================================")
     print()
     #Sprinkler On
     print("Pr(Rain|Season=0, Sprinkler = 1)")
     rSp = bn.inference.fit(model, variables=['Rain'], evidence={'Season': 0.0, 
                                                                 'Sprinkler': 1})
     #sprinkler Off
     print("Pr(Rain|Sprinkler = 0)")
     rSp1 = bn.inference.fit(model, variables=['Rain'], evidence={'Season': 0.0,
                                                                 'Sprinkler': 0})

     print("SCENARIO 3: Rain and Sprinkler are DEPENDENT conditioned on Fall Down=================================")
     print()
     #Sprinkler On
     print("Pr(Rain|Season=0, Sprinkler = 1, Fall_Down=1)")
     rSp = bn.inference.fit(model, variables=['Rain'], evidence={'Season': 0.0, 
                                                                 'Sprinkler': 1,
                                                                 'Fall_Down': 1})
     #sprinkler Off
     print("Pr(Rain|Sprinkler = 0, Fall_Down=1)")
     rSp1 = bn.inference.fit(model, variables=['Rain'], evidence={'Season': 0.0,
                                                                 'Sprinkler': 0,
                                                                 'Fall_Down': 1})

if __name__ == '__main__':
     # # Save the original stdout
     # original_stdout = sys.stdout
     file = "dataset.csv"

     # Redirect stdout to a file
     with open('t1.txt', 'w') as f:
          sys.stdout = f
          bnLearn_Tests(file)
     # entries = os.listdir('datasets/')
     # for e in entries:
     #      print(e)
