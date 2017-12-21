# taken from Siraj Raval

# Using IBM's quantum computing API in python 3

from qiskit import QuantumProgram
import Qconfig

# initialize our quantum program
qp = QuantumProgram()
# number of bits
n = 3

# create quantum register
quantumRegister = qp.create_quantum_register("quantumRegister", n)
# create classical register
classicalRegister = qp.create_classical_register("classicalRegister", n)

# create a quantum circuit now
quantumCircuit = qp.create_circuit("quantumCircuit", [quantumRegister], [classicalRegister])


# apply the hadamard gates to every qubit we have
# we're putting our qubits into a superposition so that each state is equalily as likely to be observed
for index in range(n):
    quantumCircuit.h(quantumRegister[index])

# With every possible state, we're going to apply the Oracle*. In this case,
# the oracle is a balenced function f(x) = x0 XOR x1x2
# *an oracle is a analogous to calling a function in a classical computer. For every different function, a new oracle needs to be built

quantumCircuit.z(quantumRegister[0])
quantumCircuit.cz(quantumRegister[1], quantumRegister[2])

# we're going to apply the H-gate to all the qubits again

for index in range(n):
    quantumCircuit.h(quantumRegister[index])



## this algorithm can evaluate the function in one call, which is exponentially faster than a classical approach
# classical approach: O(2^(n-1) + 1)
# quantum approach: O(1)



# we're going to measure the values
quantumCircuit.measure(quantumRegister[0], classicalRegister[0])
quantumCircuit.measure(quantumRegister[1], classicalRegister[1])
quantumCircuit.measure(quantumRegister[2], classicalRegister[2])

circuits = ["quantumCircuit"]
qp.compile(circuits, "local_qasm_simulator")

result = qp.execute("quantumCircuit")

print(result.get_counts("qCircuit"))




# from qiskit import QuantumProgram
# qp = QuantumProgram()
# qr = qp.create_quantum_register('qr',2)
# cr = qp.create_classical_register('cr',2)
# qc = qp.create_circuit('Bell',[qr],[cr])
# qc.h(qr[0])
# qc.cx(qr[0], qr[1])
# qc.measure(qr[0], cr[0])
# qc.measure(qr[1], cr[1])
# result = qp.execute('Bell')
# print(result.get_counts('Bell'))
