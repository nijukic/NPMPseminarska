import simulator
import grn
import numpy as np


my_grn = grn.grn()


my_grn.add_input_species("X")
my_grn.add_species("Y", 0.396) 
my_grn.add_species("Z", 0.265) 

my_grn.add_gene(
    40, 
    regulators=[{'name': 'X', 'type': 1, 'Kd': 8, 'n': 2}],
    products=[{'name': 'Y'}]
)


my_grn.add_gene(
    15, 
    regulators=[{'name': 'Y', 'type': 1, 'Kd': 50, 'n': 3}], 
    products=[{'name': 'Z'}]
)


my_grn.add_gene(
    15,
    regulators=[{'name': 'X', 'type': 1, 'Kd': 50, 'n': 3}],
    products=[{'name': 'Z'}]
)

my_grn.plot_network()


sequence = [
    (0,),       
    (100,),     
    (0,)       
]


T, Y = simulator.simulate_sequence(my_grn, sequence, t_single=20)
