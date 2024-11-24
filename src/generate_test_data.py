"""
generates random test dependencies,
to simulate real-world test setups.
"""

import random
import json


def generate_test_data(num_tests, max_dependencies):
    """
    Generates random test dependency data.
    
    :param num_tests: Total number of tests.
    :param max_dependencies: Maximum number of dependencies per test.
    :return: Dictionary with test names and dependencies.
    """
    tests = [f"test{i+1}" for i in range(num_tests)]
    dependencies = []

    for test in tests:
        # Randomly select dependencies for each test
        num_deps = random.randint(1, max_dependencies)
        deps = random.sample(tests, num_deps)
        for dep in deps:
            if test != dep and (dep, test) not in dependencies:
                dependencies.append((test, dep))

    return {"tests": tests, "dependencies": dependencies}


# Generate and save test data
test_data = generate_test_data(num_tests=10, max_dependencies=3)
with open("test_dependencies.json", "w") as f:
    json.dump(test_data, f, indent=2)

print("Generated test data saved to test_dependencies.json")
