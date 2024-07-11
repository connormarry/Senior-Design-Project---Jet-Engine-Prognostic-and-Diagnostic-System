import pandas as pd
from pomegranate import BayesianNetwork, DiscreteDistribution, State

# Read the dataset into a pandas DataFrame
df_bnlearn = pd.read_csv('Dataset_test1.csv')

# Convert categorical variables into numerical representation
# Season: {'spring': 0, 'summer': 1, 'fall': 2, 'winter': 3}
# Rain, Sprinkler, Wet: binary variables
df_pomegranate = df_bnlearn.replace({'Season': {'spring': 0, 'summer': 1, 'fall': 2, 'winter': 3},
                                      'Rain': {'no': 0, 'yes': 1},
                                      'Sprinkler': {'no': 0, 'yes': 1},
                                      'Wet': {'no': 0, 'yes': 1}})

# Define the states
states = []
for col in df_pomegranate.columns:
    if col != 'Wet':
        states.append(State(DiscreteDistribution.from_samples(df_pomegranate[col]), name=col))
    else:
        states.append(State(DiscreteDistribution.from_samples(df_pomegranate[col]), name='Wet'))

# Create the Bayesian Network
model = BayesianNetwork.from_states(states)

# Fit the model to the data
model.fit(df_pomegranate.values)

# Print the model parameters (CPDs)
for state in model.states:
    print(state.name)
    print(state.distribution)

# You can now use the fitted model for inference or other tasks
