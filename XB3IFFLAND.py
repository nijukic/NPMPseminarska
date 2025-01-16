import grn
import simulator
import numpy as np

my_grn = grn.grn()


my_grn.add_input_species("X")
my_grn.add_species("Y", 0.08)
my_grn.add_species("Z", 0.14)


my_grn.add_gene(
    10,
    regulators=[{'name': 'X', 'type': -1, 'Kd': 40, 'n': 2}], 
    products=[{'name': 'Y'}] 
)


my_grn.add_gene(
    22.8, 
    regulators=[{'name': 'X', 'type': 1, 'Kd': 20, 'n': 1},
                {'name': 'Y', 'type': 1, 'Kd': 50, 'n': 20}],  
    products=[{'name': 'Z'}] 
)

my_grn.plot_network()


sequence = [  
    (0), 
    (0),   
    (100),
    (100),
    (100),
    (100),
]

T, Y = simulator.simulate_sequence(my_grn, sequence, t_single = 10)