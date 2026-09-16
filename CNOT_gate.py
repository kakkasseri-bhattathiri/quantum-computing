from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
qc = QuantumCircuit(2,2)# now we are having a 2 bit system. hence we are constructing two classical bits
qc.x(0) # to switch the input
#qc.x(1)
qc.cx(0,1)
qc.measure(1,1)
#qc.measure(0,0)
simualator = AerSimulator()
result = simualator.run(qc, shots = 1000).result().get_counts()
print("the result is:" , result)
