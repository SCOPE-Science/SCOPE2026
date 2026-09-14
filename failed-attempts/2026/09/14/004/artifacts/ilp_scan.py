"""Fast ILP scan: for extremal symbolic monomials, determine max failing ratio contributions.
For s in 1..6 get several ILP minimizers (via exclusion cuts), and for each compute
ord = max r with a in I^r (ILP feasibility), recording m/r failures. Also random C5-power-like vectors."""
import pulp, sys
sys.path.insert(0, '/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-1804/output/artifacts')
from petersen_core import EDGES, all_minimal_covers
covers = all_minimal_covers()
Cmat = [[(m >> v) & 1 for v in range(10)] for m in covers]
E = EDGES
def in_ordinary(a, r):
    prob = pulp.LpProblem("ord")
    zs = [pulp.LpVariable(f"z{e}", lowBound=0, cat='Integer') for e in range(len(E))]
    prob += 0
    prob += pulp.lpSum(zs) == r
    for v in range(10):
        prob += pulp.lpSum(zs[e] for e in range(len(E)) if v in E[e]) <= a[v]
    prob.solve(pulp.PULP_CBC_CMD(msg=0))
    return pulp.LpStatus[prob.status] == 'Optimal'
def ord_max(a, rhi=6):
    best = 0
    for r in range(1, rhi+1):
        if in_ordinary(a, r): best = r
        else: break
    return best
# C5 monomial powers
cyc = [1,2,4,6,9]
for k in (1,2,3):
    a = [k if v in cyc else 0 for v in range(10)]
    mn = min(sum(Cmat[c][v]*a[v] for v in range(10)) for c in range(15))
    o = ord_max(a, 8)
    print(f"C5^{k}: deg={5*k} symb-ord>={mn} ord={o}", flush=True)
