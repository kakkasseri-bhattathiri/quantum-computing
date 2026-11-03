from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator 
from qiskit.quantum_info import Operator, random_statevector, Statevector
from qiskit.circuit.library import UnitaryGate
from qiskit import transpile
import numpy as np
import matplotlib.pyplot as plt
import math
def matrix(k):
    M = [
        [1,0],
        [0,np.exp(np.pi*1j/(2**(k-1)))]
    ]
    return Operator(M)
#circuit 
N = int(input("Enter the number of qubits for the QFT: "))
#qc = QuantumCircuit(5,5)
#k = 5
#R = matrix(k)
dim =  2**N
rand_state = random_statevector(dim)
qc = QuantumCircuit(N,N)
qc.initialize(rand_state, range(N))
for i in range(N):
    qc.h(i)
    qc.barrier()
    for j in range(2,N+1-i):
        R = matrix(j)
        CR = UnitaryGate(R, label=f'R({j})').control(1)
        qc.append(CR,[j+i-1,i])
        # SWAP gates to reverse the qubit order
for i in range(N // 2):
    qc.swap(i, N-1-i)
exact_state = Statevector(qc)
theo_probs = exact_state.probabilities_dict()
for t in range(N):
    qc.measure(t,t)
simulator = AerSimulator()
qc_transpiled =  transpile(qc, simulator)
shots = 1000
result = simulator.run(qc_transpiled, shots = shots).result().get_counts()
labels = [format(i, f'0{N}b') for i in range(dim)]
exp_counts = [result.get(key,0) for key in labels]
theo_counts = [theo_probs.get(key,0)*shots for key in labels]
x = np.arange(len(labels))
width = 0.6
plt.figure(figsize=(14,6))
plt.bar(x, exp_counts,width,color='black')
plt.ylabel('Raw counts')
plt.title(f'{N}- Experiment result')
plt.xticks(x, labels, rotation=90)
plt.tight_layout()
plt.figure(figsize=(14, 6))
plt.bar(x, theo_counts, width, color='red')
plt.ylabel('Raw Counts')
plt.title(f'{N}-Qubit QFT - Theoretical Results')
plt.xticks(x, labels, rotation=90)
plt.tight_layout()
print(qc.draw())
print(result)
plt.show()

