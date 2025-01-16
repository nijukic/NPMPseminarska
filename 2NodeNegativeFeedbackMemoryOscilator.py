import grn
import simulator
import numpy as np

# Construct the GRN
my_grn = grn.grn()

# Define the species
my_grn.add_input_species("X")  # Node 1 with a degradation rate
my_grn.add_species("Y", 0.1)  # Node 2 with a degradation rate

# Add the genes
# X activates Y
my_grn.add_gene(
    5,  # Gene expression rate for X → Y
    regulators=[{'name': 'X', 'type': 1, 'Kd': 30, 'n': 4}],  # Strong positive feedback
    products=[{'name': 'Y'}]
)

# Y activates X
my_grn.add_gene(
    3,  # Gene expression rate for Y → X
    regulators=[{'name': 'Y', 'type': -1, 'Kd': 15, 'n': 1}],  # Strong positive feedback
    products=[{'name': 'X'}]
)

# Visualize the network
#my_grn.plot_network()

# --- Single Simulation ---
# Initial input values for X and Y  
# # Start with no initial input for X and Y
#T, Y = simulator.simulate_single(my_grn, 50)

# --- Sequence Simulation ---
# Define a sequence of input changes for X and Y
input_sequence = [
    (0),    # Both X and Y off
    (35),
    (0),
    (0),
    (0),
    (0)     
]

# Simulate the sequence
T, Y = simulator.simulate_sequence(my_grn, input_sequence, t_single=100)


