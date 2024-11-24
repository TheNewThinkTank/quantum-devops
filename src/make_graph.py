
import json
import networkx as nx


def make_graph():
    graph = nx.Graph()

    # For example, we have 4 tests with dependencies:
    # Test 1 depends on Test 2 and Test 3, Test 4 depends on Test 3
    # graph.add_edges_from([(1, 2), (1, 3), (4, 3)])

    # Load test dependencies
    with open('test_dependencies.json', 'r') as f:
        data = json.load(f)

    tests = data['tests']
    dependencies = data['dependencies']

    # Build the graph
    graph.add_nodes_from(range(len(tests)))  # Add nodes for each test
    graph.add_edges_from([(tests.index(a), tests.index(b)) for a, b in dependencies])
    return tests, graph
