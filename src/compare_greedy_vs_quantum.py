
import json
import numpy as np
import cirq
import networkx as nx

# Load generated test data
with open("test_dependencies.json", "r") as f:
    data = json.load(f)

tests = data["tests"]
dependencies = data["dependencies"]

# Run greedy algorithm
selected_tests_greedy = greedy_test_selection(tests, dependencies)


def run_quantum_approach(tests, dependencies):
    """Run Cirq-based quantum approach.

    :param tests: _description_
    :type tests: _type_
    :param dependencies: _description_
    :type dependencies: _type_
    :return: _description_
    :rtype: _type_
    """

    # Build dependency graph
    graph = nx.Graph()
    graph.add_nodes_from(range(len(tests)))
    graph.add_edges_from([(tests.index(a), tests.index(b)) for a, b in dependencies])

    # Map nodes to qubits
    qubits = [cirq.GridQubit(0, i) for i in range(len(graph.nodes))]

    # Simulate QAOA
    simulator = cirq.Simulator()
    params = {"gamma": np.pi / 4, "beta": np.pi / 4}
    qaoa_circuit = create_qaoa_circuit(graph, qubits, params)
    result = simulator.simulate(qaoa_circuit)

    # Interpret results
    return interpret_results(result.final_state_vector, tests)

selected_tests_quantum = run_quantum_approach(tests, dependencies)

# Print results
print("Selected tests (Greedy):", selected_tests_greedy)
print("Selected tests (Quantum):", selected_tests_quantum)
