import pulp
from petersen_core import all_minimal_covers
covers = all_minimal_covers()
Cmat = [[(m >> v) & 1 for v in range(10)] for m in covers]

def alpha_sym(s):
    prob = pulp.LpProblem("a", pulp.LpMinimize)
    xs = [pulp.LpVariable(f"x{v}", lowBound=0, cat='Integer') for v in range(10)]
    prob += pulp.lpSum(xs)
    for row in Cmat:
        prob += pulp.lpSum(row[v]*xs[v] for v in range(10)) >= s
    prob.solve(pulp.PULP_CBC_CMD(msg=0))
    return int(round(pulp.value(prob.objective))), [int(round(x.value())) for x in xs]

for s in range(1, 7):
    val, vec = alpha_sym(s)
    print(f"alpha(I^({s})) = {val}  e.g. {vec}")
