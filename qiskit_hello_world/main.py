from qiskit import QuantumCircuit, transpile
from qiskit.providers.aer import QasmSimulator
from qiskit.visualization import plot_histogram

# Use Aer's qasm_simulator
simulator = QasmSimulator()

# Create a Quantum Circuit acting on the q register.
#  Initializing with 2 qubits in the zero state and  2 classical bits set to zero
circuit = QuantumCircuit(2, 2)

# Add a Hadamard gate  on qubit 0, which puts it into a superposition state.
circuit.h(0)

# Add a CX (CNOT) gate on control qubit 0 and target qubit 1, putting the qubits in an entangled state.
circuit.cx(0, 1)

# If you pass the entire quantum and classical registers to measure,
# the ith qubit’s measurement result will be stored in the ith classical bit.
circuit.measure([0, 1], [0, 1])

# compile the circuit down to low-level QASM instructions
# supported by the backend (not needed for simple circuits)
compiled_circuit = transpile(circuit, simulator)

# Execute the circuit on the qasm simulator
job = simulator.run(compiled_circuit, shots=1000)

# Grab results from the job
result = job.result()

# Returns counts
counts = result.get_counts(compiled_circuit)
print("\nTotal count for 00 and 11 are:", counts)

# Draw the circuit
circuit.draw(output='mpl', filename='my_circuit.png')
print(circuit)

# Plot a histogram
plot_histogram(counts)
