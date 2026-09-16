from qiskit import QuantumCircuit
from qiskit_aer import  AerSimulator
qc = QuantumCircuit(1,1) #define a circuit that hs one qubit and an additionnal classical bit for measurement purposes
qc.h(0) #do the hadamard operation on the qubit with index zero
qc.measure(0,0) # measure the result and then store it in the classical bit that we had constructed earlier
#to find out the result we will have to simulate the quantum computer
simulate = AerSimulator() #simulatorine aavahikka
result  = simulate.run(qc, shots = 1000).result().get_counts() # do the previous steps in one line
print("the result will be :", result)

