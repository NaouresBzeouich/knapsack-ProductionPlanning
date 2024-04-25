import gurobipy as gp
from gurobipy import GRB


def knapsack_solver(values, weights, capacity):
    n = len(values)
    model = gp.Model("knapsack")

    # Decision variables
    x = model.addVars(n, vtype=GRB.BINARY, name="x")

    # Objective function
    model.setObjective(sum(values[i] * x[i] for i in range(n)), GRB.MAXIMIZE)

    # Constraint: capacity
    model.addConstr(sum(weights[i] * x[i] for i in range(n)) <= capacity)

    # Solve
    model.optimize()

    # Extract solution
    selected_items = [i for i in range(n) if x[i].x > 0.5]  # Choose items with x[i] > 0.5
    total_value = sum(values[i] for i in selected_items)
    total_weight = sum(weights[i] for i in selected_items)

    return selected_items, total_value, total_weight


# Example usage
values = [60, 100, 120]
weights = [10, 20, 200]
capacity = 50

selected_items, total_value, total_weight = knapsack_solver(values, weights, capacity)
print("Selected items:", selected_items)
print("Total value:", total_value)
print("Total weight:", total_weight)

