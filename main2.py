import gurobipy as gp
from gurobipy import GRB

def solve_production_planning(products, profit, production_time,production_capacity, demand=None):
    # Create a new model
    model = gp.Model("Production_Planning")

    # Decision variables
    production = {}
    for product in products:
        production[product] = model.addVar(vtype=GRB.INTEGER, name=f"production_{product}")

    # Objective function: maximize total profit
    model.setObjective(gp.quicksum(production[product] * profit[product] for product in products), GRB.MAXIMIZE)

    # Capacity constraint: total production time must not exceed production capacity
    model.addConstr(gp.quicksum(production[product] * production_time[product] for product in products) <= production_capacity)

    # Demand constraints (if available)
    if demand:
        for product in products:
            if product in demand:
                model.addConstr(production[product] >= demand[product])

    # Optimize the model
    model.optimize()

    # Print solution
    if model.status == GRB.OPTIMAL:
        print("Optimal production plan:")
        for product in products:
            print(f"Product {product}: {production[product].x} units")

        max = 0
        for product in products:
            max += production[product].x * profit[product]
        print(max)
    else:
        print("No solution found.")


# Example data
products = ["Product_A", "Product_B", "Product_C"]
profit = {"Product_A": 10, "Product_B": 8, "Product_C": 6}
production_time = {"Product_A": 1, "Product_B": 2, "Product_C": 1}
production_capacity = 10
demand = {"Product_A": 3, "Product_C": 2}  # Demand for Product_A and Product_C, Product_B is optional

# Solve the production planning problem
production = solve_production_planning(products,profit, production_time,production_capacity, demand)

