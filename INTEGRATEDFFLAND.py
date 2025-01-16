import grn
import simulator
import numpy as np


my_grn = grn.grn()


my_grn.add_input_species("X1") 
my_grn.add_species("X2", 0.12)
my_grn.add_species("Y1", 0.1)
my_grn.add_species("Y2", 0.1)  
my_grn.add_species("Z1", 0.1)  
my_grn.add_species("Z2", 0.1)  
my_grn.add_species("Z3", 0.1)  


my_grn.add_gene(
    13,
    regulators=[{'name': 'X1', 'type': 1, 'Kd': 10, 'n': 4}], 
    products=[{'name': 'Y1'}] 
)


my_grn.add_gene(
    29, 
    regulators=[
        {'name': 'X1', 'type': 1, 'Kd': 50, 'n': 8}, 
        {'name': 'Y1', 'type': -1, 'Kd': 50, 'n': 8} 
    ],
    products=[{'name': 'Z1'}]  
)

my_grn.add_gene(
    10,  
    regulators=[{'name': 'X1', 'type': 1, 'Kd': 30, 'n': 4},
                {'name': 'Y1', 'type': 1, 'Kd': 30, 'n': 4}], 
    products=[{'name': 'X2'}]
)

my_grn.add_gene(
    10, 
    regulators=[{'name': 'X2', 'type': 1, 'Kd': 80, 'n': 2}], 
    products=[{'name': 'Y2'}]
)


my_grn.add_gene(
    17.3,  
    regulators=[
        {'name': 'X2', 'type': 1, 'Kd': 15, 'n': 10}, 
        {'name': 'Y2', 'type': -1, 'Kd': 15, 'n': 10} 
    ],
    products=[{'name': 'Z2'}] 
)

my_grn.add_gene(
    10.3, 
    regulators=[{'name': 'X2', 'type': 1, 'Kd': 20, 'n': 40},
                {'name': 'Y2', 'type': 1, 'Kd': 20, 'n': 40}],  
    products=[{'name': 'Z3'}]
)

my_grn.plot_network()

sequence = [
    (0),    
    (100),   
    (100),
    (100),
    (100),
    (100),
]

T, Y = simulator.simulate_sequence(my_grn, sequence, t_single = 10)
