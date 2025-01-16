import grn
import simulator
import numpy as np

my_grn = grn.grn()

my_grn.add_input_species("S")
my_grn.add_species("X", 0.1) 
my_grn.add_species("Y", 0.1)  



my_grn.add_gene(
    40,  
    regulators=[{'name': 'X', 'type': 1, 'Kd': 30, 'n': 2.5}], 
    products=[{'name': 'Y'}]
)


my_grn.add_gene(
    40, 
    regulators=[{'name': 'Y', 'type': -1, 'Kd': 30, 'n': 2.5}], 
    products=[{'name': 'X'}]
)


my_grn.plot_network()

input_sequence = [
    (0),  
    (0),
    (0),
    (0),
    (0),
    (0)     
]


T, Y = simulator.simulate_sequence(my_grn, input_sequence, t_single=100)


