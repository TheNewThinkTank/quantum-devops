
import numpy as np
import cirq
from make_graph import make_graph

tests, graph = make_graph()

qubits = [cirq.GridQubit(0, i) for i in range(len(graph.nodes))]


# def maxcut_cost(graph, qubits):
#     circuit = cirq.Circuit()
#     for edge in graph.edges:
#         i, j = edge
#         # Add ZZ interaction to represent edge contribution to the cost
#         circuit.append(cirq.ZZ(qubits[i - 1], qubits[j - 1]))
#     return circuit


def create_qaoa_circuit(graph, qubits, params):
    circuit = cirq.Circuit()
    # Apply initial Hadamard gates
    circuit.append(cirq.H.on_each(qubits))
    # Apply cost function
    gamma = params['gamma']
    for edge in graph.edges:
        i, j = edge
        circuit.append(cirq.ZZ(qubits[i], qubits[j]) ** gamma)
    # Apply mixing gates
    beta = params['beta']
    circuit.append(cirq.rx(beta).on_each(qubits))

    return circuit


# Simulate and evaluate
simulator = cirq.Simulator()

# Define QAOA parameters
params = {'gamma': np.pi / 4, 'beta': np.pi / 4}
qaoa_circuit = create_qaoa_circuit(graph, qubits, params)

print("QAOA Circuit:")
print(qaoa_circuit)

# Run the simulation
result = simulator.simulate(qaoa_circuit)
print("\nFinal State Vector:")
print(result.final_state_vector)


def interpret_results(state_vector, tests):
    probabilities = np.abs(state_vector) ** 2
    best_state = np.argmax(probabilities)
    binary_state = format(best_state, f'0{len(tests)}b')
    selected_tests = [tests[i] for i, bit in enumerate(binary_state) if bit == '1']
    return selected_tests


selected_tests = interpret_results(result.final_state_vector, tests)
print("Tests to run:", selected_tests)
