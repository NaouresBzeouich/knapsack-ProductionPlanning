import gurobipy as gp
from gurobipy import GRB

def solve_production_planning(products, profit, production_time,production_capacity, demand=None) :
    # Create a new model
    model = gp.Model("Production_Planning")

    # Decision variables
    production = {}
    for product in products:
        production[product] = model.addVar(vtype=GRB.CONTINUOUS, name=f"production_{product}")

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

    result = ""

    # Print solution
    if model.status == GRB.OPTIMAL:
        result = "La solution optimale est la suivante :\n  Plan de production :\n"
        for product in products:
            result += f"Produit {product}: {production[product].x} unités\n"

        total_profit = sum(production[product].x * profit[product] for product in products)
        result += f"Le bénéfice total est : {total_profit}"
    else:
        result = "Pas de solution trouvée."

    print(result)

    return result