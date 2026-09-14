import pulp
from petersen_core import BASE, EDGES, all_minimal_covers
covers = all_minimal_covers()
print("num covers:", len(covers))
Cmat = [[(m >> v) & 1 for v in range(10)] for m in covers]

# Fractional: minimize sum x s.t. C x >= 1, x>=0
prob = pulp.LpProblem("wald", pulp.LpMinimize)
xs = [pulp.LpVariable(f"x{v}", lowBound=0) for v in range(10)]
prob += pulp.lpSum(xs)
for row in Cmat:
    prob += pulp.lpSum(row[v]*xs[v] for v in range(10)) >= 1
prob.solve(pulp.PULP_CBC_CMD(msg=0))
print("LP status:", pulp.LpStatus[prob.status])
print("LP optimum:", pulp.value(prob.objective))
print("solution:", [round(x.value(), 6) for x in xs])

# Dual: maximize sum y_C s.t. for each v: sum_{C ni v} y_C <= 1, y>=0
dprob = pulp.LpProblem("dual", pulp.LpMaximize)
ys = [pulp.LpVariable(f"y{c}", lowBound=0) for c in range(len(covers))]
dprob += pulp.lpSum(ys)
for v in range(10):
    dprob += pulp.lpSum(Cmat[c][v]*ys[c] for c in range(len(covers))) <= 1
dprob.solve(pulp.PULP_CBC_CMD(msg=0))
print("Dual optimum:", pulp.value(dprob.objective))
print("dual sol:", [round(y.value(), 6) for y in ys])
