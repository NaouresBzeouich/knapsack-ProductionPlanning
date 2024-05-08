import gurobipy as gp
from gurobipy import GRB

def solve_production_planning(products, profit, production_time,production_capacity, demand=None):
    # Create a new model
    model = gp.Model("Production_Planning")
    print(products, profit, production_time,production_capacity, demand)
    # Decision variables
    production = {}
    print(1111111111111111)
    for product in products:
        production[product] = model.addVar(vtype=GRB.CONTINUOUS, name=f"production_{product}")
    print(222222222222222222)
    # Objective function: maximize total profit
    model.setObjective(sum(production[product] * profit[product] for product in products), GRB.MAXIMIZE)
    
    # Capacity constraint: total production time must not exceed production capacity
    model.addConstr(sum(production[product] * production_time[product] for product in products) <= production_capacity)

    # Demand constraints (if available)
    print(products)
    for product in products:
        if (product in demand.keys())  : 
            model.addConstr(production[product] >= demand[product])
    print(3333333333333333333)
    # Optimize the model
    model.optimize()

    result = ""

    # Print solution
    if model.status == GRB.OPTIMAL:
        result = "la solution de Félix etait : \n  planter les produits :\n"
        for product in products:
            result += "product "+ str(product) +" : "+ str (production[product].x) + " fois "

        max = 0
        for product in products:
            max += production[product].x * profit[product]
        result += "le benefice total est :"+ str(max)
    else:
        result += "pas de solution ! "
    return result