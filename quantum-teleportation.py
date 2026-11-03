from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.quantum_info import random_statevector
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import numpy as np
qc = QuantumCircuit(3,3)
print("choose an initial state for the qubit")
print("for |0>, type 0")
print("for |1>, type 1")
print("for |+>, type +")
print("for |->, type -") 
print ("for a genreal qubit, press any other key.")
choice = input("Enter your choice: ").strip()
if choice == "0":   
    prob_0, prob_1 = 1.0, 0.0
elif choice == "1":
    qc.x(0)
    prob_0, prob_1 = 0.0, 1.0
elif choice == "+":
    qc.h(0)
    prob_0, prob_1 = 0.5, 0.5
elif choice == "-":
    qc.x(0)
    qc.h(0)
    prob_0, prob_1 = 0.5, 0.5
else:
    rand_state = random_statevector(2)
    qc.initialize(rand_state, 0)
    prob_0 = np.abs(rand_state.data[0])**2 #returs the data as an array, 0 is for the first elemetn adn 1 is the second elemetn
    prob_1 = np.abs(rand_state.data[1])**2
trials = 1000
theoretical = {}
for top_bits in ['00','01','10','11']:
    theoretical[f'0{top_bits}'] = trials * 0.25 * prob_0
    theoretical[f'1{top_bits}'] = trials * 0.25 * prob_1
his_theo = plot_histogram(theoretical, title='theoretical', color='red')
qc.barrier()
qc.h(1)
qc.cx(1,2)
qc.barrier()
qc.cx(0,1)
qc.h(0)
qc.barrier()
qc.measure(0,0)
qc.measure(1,1)
qc.barrier()
qc.cx(1,2)
qc.cz(0,2)
qc.measure(2,2)
print("the quantum teleportation circuit is")
print(qc.draw())
simulator = AerSimulator()
result = simulator.run(qc, shots = 1000).result().get_counts()
print("Alex's bit is ", result)
fig =  plot_histogram(result, title='Teleportation result', color= 'black')
plt.show()
