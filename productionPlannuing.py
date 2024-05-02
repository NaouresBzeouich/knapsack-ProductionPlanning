import gurobipy as gp
from gurobipy import GRB

def solve_production_planning(products, profit, production_time,production_capacity, demand=None):
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
        result = "la solution de Félix etait : \n  planter les produits :\n"
        for product in products:
            result += "product "+product+" : "+production[product].x + " fois "

        max = 0
        for product in products:
            max += production[product].x * profit[product]
        result += "le benefice total est :"+max
    else:
        result += "pas de solution ! "
    return result