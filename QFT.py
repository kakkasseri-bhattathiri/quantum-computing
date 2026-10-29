from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator 
from qiskit.quantum_info import Operator
import numpy as np
import math
def matrix(k):
    M = [
        [1,0],
        [0,np.exp(np.pi*1j/(2**(k-1)))]
    ]
    return Operator(M)
#circuit 
qc = QuantumCircuit(5,5)
k = 5
#R = matrix(k)
for i in range(5):
    qc.h(i)
    qc.barrier()
    for j in range(2,6-i):
        R = matrix(j)
        qc.unitary(R,[i],label=f'R({j})')
for t in range(5):
    qc.measure(t,t)
simulator = AerSimulator()
result = simulator.run(qc, shots = 1000).result().get_counts()

