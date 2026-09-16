from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
qc = QuantumCircuit(1,1) #what the circuit contains 1 qubit and 1 classical bit
qc.x(0) #does the NOT operation on the initial state
qc.measure(0,0) #measures the state (index= 0) after the NOT operation is completed, and stores it in the classical bit with an  index 0
simulator = AerSimulator() # aavahikkal of the simualtor
job = simulator.run(qc,shots = 1000) #aavahichenu shesham what do we have to do? we have to make it do work
result = job.result()
counts = result.get_counts()
print("Measurement counts :", counts)
