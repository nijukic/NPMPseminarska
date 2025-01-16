import grn
import simulator
import numpy as np

my_grn = grn.grn()

my_grn.add_input_species("X")
my_grn.add_species("Y", 0.1) 
my_grn.add_species("Z", 0.1)
my_grn.add_species("W", 0.1)


my_grn.add_gene(
    30,
    regulators=[{'name': 'X', 'type': -1, 'Kd': 60, 'n': 2}],
    products=[{'name': 'Y'}, {'name': 'Z'}]
)

my_grn.add_gene(
    10,
    regulators=[{'name': 'W', 'type': 1, 'Kd': 10, 'n': 2}],
    products=[{'name': 'Z'}]
)


my_grn.add_gene(
    10,
    regulators=[{'name': 'Y', 'type': 1, 'Kd': 10, 'n': 2}],
    products=[{'name': 'W'}]
)


my_grn.plot_network()

input_sequence = [
    (0),
    (100),
    (0),
    (0),
]

T, Y = simulator.simulate_sequence(my_grn, input_sequence, t_single=250)


