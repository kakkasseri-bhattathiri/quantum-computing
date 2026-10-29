from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator 
from qiskit.quantum_info import Operator
from  qiskit.circuit.library import UnitaryGate
from qiskit import transpile
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
        CR = UnitaryGate(R, label=f'R({j})').control(1)
        qc.append(CR,[j+i-1,i])
        # SWAP gates to reverse the qubit order
for i in range(5 // 2):
    qc.swap(i, 4 - i)
for t in range(5):
    qc.measure(t,t)
simulator = AerSimulator()
qc_transpiled =  transpile(qc, simulator)
result = simulator.run(qc_transpiled, shots = 1000).result().get_counts()
print(result)
