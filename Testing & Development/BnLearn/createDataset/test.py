import bnlearn as bn 
import numpy as np
from pgmpy.factors.discrete import TabularCPD

edges = [("Season", "Rain"), ("Season", "Sprinkler"), ("Rain", "Wet"), ("Sprinkler", "Wet")]

#Defining the CPD Tables
#Fall(0), Winter(1), Spring(2), Summer(3)
cpd_Season = TabularCPD("Season", 4, [[0.25], [0.25], [0.25], [0.25]])
cpd_Rain = TabularCPD("Rain", 2, [[0.45, 0.68, 0.22, 0.45], [0.54, 0.32, 0.78, 0.55]], 
                      evidence=["Season"], evidence_card=[4])
cpd_Sprinkler = TabularCPD("Sprinkler", 2, [[0.84, 0.92, 0.55, 0.15], [0.16, 0.08, 0.45, 0.85]], 
                      evidence=["Season"], evidence_card=[4])
cpd_Wet = TabularCPD("Wet_Grass", 2, [[0.95, 0.10, 0.10, 0.01], [0.05, 0.90, 0.90, 0.99]], 
                     evidence=["Sprinkler", "Rain"], evidence_card=[2, 2])

print(cpd_Season)
print()
print(cpd_Rain)
print()
print(cpd_Sprinkler)
print()
print(cpd_Wet)

DAG = bn.make_DAG(edges)
simple_figure = bn.plot(DAG)