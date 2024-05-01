import knapSac

keys = ["livre", "sacDeCouchage", "tente"]
values = {"livre": 500,
        "sacDeCouchage": 1500,
        "tente": 2000,
        "corde": 500}

print(knapSac.knapsack_solver(keys,values,1000))