import grn
import simulator
import numpy as np

my_grn = grn.grn()

my_grn.add_input_species("X")
my_grn.add_species("Y", 0.1)


my_grn.add_gene(
    5,  # Gene expression rate for X → Y
    regulators=[{'name': 'X', 'type': 1, 'Kd': 30, 'n': 4}],
    products=[{'name': 'Y'}]
)

my_grn.add_gene(
    3,  # Gene expression rate for Y → X
    regulators=[{'name': 'Y', 'type': -1, 'Kd': 15, 'n': 1}],
    products=[{'name': 'X'}]
)

my_grn.plot_network()

input_sequence = [
    (0),   
    (35),
    (0),
    (0),
    (0),
    (0)     
]

T, Y = simulator.simulate_sequence(my_grn, input_sequence, t_single=100)


