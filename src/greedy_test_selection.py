"""
Greedy Algorithm for Test Selection.
A greedy algorithm will select tests to cover all dependencies step by step,
always choosing the test that covers the most uncovered dependencies.
"""


def greedy_test_selection(tests, dependencies):
    """
    Selects the minimal number of tests to cover all dependencies using a greedy approach.
    
    :param tests: List of test names.
    :param dependencies: List of (test1, test2) tuples representing dependencies.
    :return: List of selected test names.
    """
    # Initialize variables
    selected_tests = []
    uncovered_dependencies = set(dependencies)

    while uncovered_dependencies:
        # Find the test that covers the most uncovered dependencies
        test_coverage = {
            test: sum(1 for dep in uncovered_dependencies if test in dep)
            for test in tests
        }
        best_test = max(test_coverage, key=test_coverage.get)

        # Add the best test to the selected list
        selected_tests.append(best_test)

        # Remove dependencies covered by the selected test
        uncovered_dependencies = {
            dep for dep in uncovered_dependencies if best_test not in dep
        }

    return selected_tests


# Example usage
tests = ["test1", "test2", "test3", "test4"]
dependencies = [("test1", "test2"), ("test1", "test3"), ("test3", "test4")]

selected_tests_greedy = greedy_test_selection(tests, dependencies)
print("Greedy-selected tests:", selected_tests_greedy)
