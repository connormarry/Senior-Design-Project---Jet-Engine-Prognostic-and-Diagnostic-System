import pandas as pd
import os
import sys
from pgmpy.models import BayesianNetwork
from pgmpy.independencies import Independencies, IndependenceAssertion
from pgmpy.inference import VariableElimination
import matplotlib.pyplot as plt
import networkx as nx

def test_pgmpy(filename):
    print("Testing file: ", filename)

    # -------------------------------------------- Build the Network and Inference Object ------------------------------------------
    data = pd.read_csv(filename)

    edges = [
        ("Season", "Rain"),
        ("Season", "Sprinkler"),
        ("Rain", "Wet"),
        ("Sprinkler", "Wet"),
        ("Wet", "Slippery"),
        ("Slippery", "Fall_Down"),
    ]

    # Fits the network with noise
    model = BayesianNetwork(edges)
    model.fit(data)

    # We only want to plot the BN once since it is the same regardless of the dataset used
    if filename == 'datasets/High_Noise_Dataset.csv':
        # Manually specify node positions for the plot
        pos = {
            "Season": (1.5, 4),
            "Rain": (1, 3), "Sprinkler": (2, 3),
            "Wet": (1.5, 2),
            "Slippery": (1.5, 1),
            "Fall_Down": (1.5, 0)
        }

        # Plot the DAG with custom node positions
        plt.figure(figsize=(10, 8))
        nx.draw(model, pos=pos, with_labels=True, node_size=7000, node_color='lightblue', font_size=12,
                font_weight='bold')
        plt.title(f"Bayesian Network Structure (DAG)")
        plt.show()

    # print cpds for the model
    '''
    print(f"\n==============================================================="
          f"\nCPDs for {filename}:"
          f"\n===============================================================")

    for cpd in model.get_cpds():
        print("CPD of {variable}:".format(variable=cpd.variable))
        print(f"{cpd}\n")
        
    '''

    # Inference object for quering in pgmpy
    infer = VariableElimination(model)

    ##################################################################################################
    #                                             TESTING
    ##################################################################################################

    # ----------------------------------- Tests for condional independence ------------------------------------
    # Compute Indepedence Test on the model
    ## Any two nodes are associated in the model if the p value < significance value
    ## Prints results of the independence test

    # Compute Independence Test
    print(f"\n==============================================================="
          f"\nIndependence Test Results for {filename}:"
          f"\n===============================================================\n")
    for node in model.nodes():
        independencies = model.local_independencies(node)
        print(f"Independencies for node {node}: {independencies}")

    # ===============  Conditional Testing -- Pr(Rain || Sprinkler), Pr(Sprinkler || Rain) =============
    # Key Idea: Rain and Sprinkler are Independent of Each Other
    print(f"\n==============================================================="
          f"\nConditional Testing for {filename}:"
          f"\n===============================================================\n")
    print("Pr(Rain || Sprinkler), Pr(Sprinkler || Rain)")

    # Sprinkler On
    print()
    print("Pr(Rain|Season=0, Sprinkler = 1)")
    rSp = infer.query(variables=["Rain"], evidence={"Season": 0.0, "Sprinkler": 1})
    print(rSp)

    # Sprinkler off
    print()
    print("Pr(Rain|Season=0, Sprinkler = 0)")
    rSp1 = infer.query(variables=["Rain"], evidence={"Season": 0.0, "Sprinkler": 0})
    print(rSp1)

    # Rain on
    print()
    print("Pr(Sprinkler|Season=0, Rain = 1)")
    spR = infer.query(variables=["Sprinkler"], evidence={"Season": 0.0, "Rain": 1})
    print(spR)

    # Rain off
    print()
    print("Pr(Sprinkler|Season=0, Rain = 0)")
    spR2 = infer.query(variables=["Sprinkler"], evidence={"Season": 0.0, "Rain": 0})
    print(spR2)

    print("\nConclusion: Rain and Sprinkler are INDEPENDENT of each other")

    # ===============   Seperation Theorems: Conditional Independence Between Nodes  ===================
    
    # ===========================  SCENARIO 1 ===============================================
     #MAIN IDEA: Rain and Slippery are Dependent on Each other, until they are conditioned on Wet which is 
     #           a blocking node, making Rain and Slippery Dependent
    print(f"\n==============================================================="
          f"\nSeparation Theorem Results for {filename}:"
          f"\n===============================================================\n")
    print(
        "Scenario 1: Rain and Slippery are NOT INDEPENDENT with no blocking path:"
    )
    print()
    print("Pr(Slippery | Rain = 0)")
    slR = infer.query(variables=["Slippery"], evidence={"Rain": 0})
    print(slR)

    print()
    print("Pr(Slippery | Rain = 1)")
    slR = infer.query(variables=["Slippery"], evidence={"Rain": 1})
    print(slR)

    print()
    print("Pr(Slippery | Rain = 2)")
    slR = infer.query(variables=["Slippery"], evidence={"Rain": 2})
    print(slR)

    # Now, we specify a blocking node of Wet -- Rain and Slippery should be independent
    print()
    print(
        "Rain and Slippery are INDEPENDENT with a blocking node of Wet -- Scenario 2:"
    )
    print()
    print("Pr(Slippery | Rain = 0, Wet = 2)")
    slR = infer.query(variables=["Slippery"], evidence={"Wet": 2,
                                                        "Rain": 0})
    print(slR)

    print()
    print("Pr(Slippery | Rain = 1, Wet = 2)")
    slR = infer.query(variables=["Slippery"], evidence={"Wet": 2,
                                                        "Rain": 1})
    print(slR)

    print()
    print("Pr(Slippery | Rain = 2, Wet = 2)")
    slR = infer.query(variables=["Slippery"], evidence={"Wet": 2,
                                                        "Rain": 2})
    print(slR)

    # ===========================  SCENARIO 2 ===============================================
    # MAIN IDEA: Rain and Sprinkler should be dependent on each other naturally. When conditioned 
    #           on Season, they should then be independent
     
    print("SCENARIO 2: Rain and Sprinkler are DEPENDENT when not conditioned on Season=====================")
    print()
     
    #Rain = 0
    print("Pr(Sprinkler | Rain = 0)")
    rSp = infer.query(variables=['Sprinkler'], evidence={'Rain': 0})
    print(rSp)
    
    #Rain = 1
    print()
    print("Pr(Sprinkler | Rain = 1)")
    rSp = infer.query(variables=['Sprinkler'], evidence={'Rain': 1})
    print(rSp)
    
    #Rain = 2
    print()
    print("Pr(Sprinkler | Rain = 2)")
    rSp = infer.query(variables=['Sprinkler'], evidence={'Rain': 2})
    print(rSp)
    
    print()
    print("SCENARIO 2: When Conditioned on Season, they should be INDEPENDENT===============================")
    #Rain = 0
    print("Pr(Sprinkler | Rain = 0, Season = 1)")
    rSp = infer.query(variables=['Sprinkler'], evidence={'Season': 1,
                                                         'Rain': 0})
    print(rSp)
    
    #Rain = 1
    print()
    print("Pr(Sprinkler | Rain = 1, Season = 1)")
    rSp = infer.query(variables=['Sprinkler'], evidence={'Season': 1,
                                                         'Rain': 1})
    print(rSp)
    
    #Rain = 2
    print()
    print("Pr(Sprinkler | Rain = 2, Season = 1)")
    rSp = infer.query(variables=['Sprinkler'], evidence={'Season': 1,
                                                         'Rain': 2})
    print(rSp)
    # ===========================  SCENARIO 3 ===============================================
    # MAIN IDEA: Rain and Sprinkler should be Independent of one another due to blocking path 3, 
    #           but when consitioned on Wet/Slippery or Fall Down, they should no longer be ind.

    print()
    print("Rain and Sprinkler are INDEPENDENT when there is a blocking path between them -- Scenario 3:")
    print()
    # Sprinkler On
    print("Pr(Rain|Season=0, Sprinkler = 1)")
    rSp = infer.query(variables=["Rain"], evidence={"Season": 0, "Sprinkler": 1})
    print(rSp)

    # Sprinkler off
    print()
    print("Pr(Rain|Sprinkler = 0)")
    rsp1 = infer.query(variables=["Rain"], evidence={"Season": 0, "Sprinkler": 0})
    print(rsp1)

    print()
    print(
        "Rain and Sprinkler are NOT INDEPENDENT conditioned on Fall Down -- Scenario 3:"
    )
    print()
    # Sprinkler On
    print("Pr(Rain|Season=0, Sprinkler = 1, Fall_Down=1)")
    rsp = infer.query(
        variables=["Rain"], evidence={"Season": 0, "Sprinkler": 1, "Fall_Down": 1}
    )
    print(rsp)

    # Sprinkler off
    print()
    print("Pr(Rain|Sprinkler = 0, Fall_Down=1)")
    rsp1 = infer.query(
        variables=["Rain"], evidence={"Season": 0, "Sprinkler": 0, "Fall_Down": 1}
    )
    print(f'{rsp1}\n\n')


# if __name__ == "__main__":
#     test_dir = os.listdir("datasets/")
#     for file in test_dir:
#         test_pgmpy(os.path.join("datasets", file))
