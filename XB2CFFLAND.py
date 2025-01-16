import grn
import simulator
import numpy as np


my_grn = grn.grn()

my_grn.add_input_species("S") 
my_grn.add_species("X", 0.1)
my_grn.add_species("Y", 0.06) 
my_grn.add_species("Z", 0.11)


my_grn.add_gene(
    2,
    regulators=[{'name': 'S', 'type': 1, 'Kd': 20, 'n': 5}],
    products=[{'name': 'X'}]
)


my_grn.add_gene(
    6.4,
    regulators=[{'name': 'X', 'type': 1, 'Kd': 20, 'n': 2}],
    products=[{'name': 'Y'}] 
)

my_grn.add_gene(
    10.5,
    regulators=[{'name': 'Y', 'type': 1, 'Kd': 20, 'n': 2}],
    products=[{'name': 'X'}] 
)

my_grn.add_gene(
    11.2,
    regulators=[{'name': 'X', 'type': 1, 'Kd': 10, 'n': 5},
                {'name': 'Y', 'type': 1, 'Kd': 14, 'n': 5}], 
    products=[{'name': 'Z'}] 
)

my_grn.plot_network()


sequence = [
    (0), 
    (100), 
    (0),
    (0),
    (0),
    (0),
]

T, Y = simulator.simulate_sequence(my_grn, sequence, t_single = 20)