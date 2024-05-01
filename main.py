import gurobipy as gp
from gurobipy import GRB


def knapsack_solver(keys, values, capacity):
    weights = {
        "pomme": 100,
        "bouteilleDEeau": 500,
        "couverture": 1000,
        "lampe": 200,
        "carte": 200,
        "kitSecours": 500,
        "telephone": 200,
        "livre": 500,
        "sacDeCouchage": 1500,
        "tente": 2000,
        "corde": 500}
    print(len(weights))
    model = gp.Model("knapsack")

    # Decision variables
    x = model.addVars(keys, vtype=GRB.BINARY, name="x")

    # Objective function
    model.setObjective(sum(values[key] * x[key] for key in keys), GRB.MAXIMIZE)

    # Constraint: capacity
    model.addConstr(sum(weights[key] * x[key] for key in keys) <= capacity)

    # Solve
    model.optimize()

    # Extract solution
    selected_items = [key for key in keys if x[key].x > 0.5]
    total_value = sum(values[key] for key in selected_items)
    total_weight = sum(weights[key] for key in selected_items)

    return selected_items, total_value, total_weight


# Example usage
keys = ["livre", "sacDeCouchage", "tente"]
values = {"livre": 500,
        "sacDeCouchage": 1500,
        "tente": 2000,
        "corde": 500}

capacity = 0

#first we must check that every key has a value
test = True
for key in keys:
    if key not in values:
        test = False
        break

if test:
    selected_items, total_value, total_weight = knapsack_solver(keys, values, capacity)
    print("Selected items:", selected_items)
    print("Total value:", total_value)
    print("Total weight:", total_weight)
else:
    print("there's keys without value ! ")
