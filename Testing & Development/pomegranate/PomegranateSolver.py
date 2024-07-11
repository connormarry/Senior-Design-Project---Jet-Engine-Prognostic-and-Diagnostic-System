import numpy as np
from pomegranate import BayesianNetwork, DiscreteDistribution, ConditionalProbabilityTable, State

# Define the Bayesian Network structure
edges = [('EngineSpeed', 'Fault'),
         ('ExhaustGasTemp', 'Fault'),
         ('FuelFlowRate', 'Fault'),
         ('VibrationLevel', 'Fault'),
         ('OilPressure', 'Fault'),
         ('InletAirTemp', 'Fault'),
         ('Thrust', 'Fault'),
         ('BlackSmoke', 'Fault')]

# Create the Bayesian Network
model = BayesianNetwork()

# Define the CPDs using ConditionalProbabilityTable
cpd_engine_speed = ConditionalProbabilityTable(
    [[0, 0.9], [1, 0.1]], ['EngineSpeed'], [2]
)
cpd_exhaust_gas_temp = ConditionalProbabilityTable(
    [[0, 0.8], [1, 0.2]], ['ExhaustGasTemp'], [2]
)
cpd_fuel_flow_rate = ConditionalProbabilityTable(
    [[0, 0.85], [1, 0.15]], ['FuelFlowRate'], [2]
)
cpd_vibration_level = ConditionalProbabilityTable(
    [[0, 0.9], [1, 0.1]], ['VibrationLevel'], [2]
)
cpd_oil_pressure = ConditionalProbabilityTable(
    [[0, 0.9], [1, 0.1]], ['OilPressure'], [2]
)
cpd_inlet_air_temp = ConditionalProbabilityTable(
    [[0, 0.8], [1, 0.2]], ['InletAirTemp'], [2]
)
cpd_thrust = ConditionalProbabilityTable(
    [[0, 0.9], [1, 0.1]], ['Thrust'], [2]
)
cpd_black_smoke = ConditionalProbabilityTable(
    [[0, 0.85], [1, 0.15]], ['BlackSmoke'], [2]
)

# Connect the CPDs with the respective nodes in the Bayesian network
for node, cpd in zip(['EngineSpeed', 'ExhaustGasTemp', 'FuelFlowRate', 'VibrationLevel', 
                      'OilPressure', 'InletAirTemp', 'Thrust', 'BlackSmoke'],
                     [cpd_engine_speed, cpd_exhaust_gas_temp, cpd_fuel_flow_rate, cpd_vibration_level, 
                      cpd_oil_pressure, cpd_inlet_air_temp, cpd_thrust, cpd_black_smoke]):
    state = State(cpd, name=node)
    model.add_state(state)

# Add edges to the model
for edge in edges:
    parent, child = edge
    model.add_edge(parent, child)

# Fit the model to the data (random data for demonstration)
model.fit(np.random.randint(2, size=(1000, len(edges))))

# Print the CPDs (Optional)
for state in model.states:
    print(f"CPD of {state.name}:")
    print(state.distribution)
