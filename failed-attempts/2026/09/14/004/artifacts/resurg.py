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

# symbolic extremal monomials: ord vector a; check m/r failures
from itertools import combinations_with_replacement
from petersen_core import EDGES
E = EDGES
# build membership in I^r: a >= some sum of r edges (exponent-wise). BFS/gen all sums is huge for large r; use ILP instead.
def in_ordinary(a, r):
    # ILP: choose multiset of edges: variables z_e >=0 integers, sum z_e = r, for each v: sum_{e ni v} z_e <= a_v
    prob = pulp.LpProblem("ord", pulp.LpMaximize)
    zs = [pulp.LpVariable(f"z{e}", lowBound=0, cat='Integer') for e in range(len(E))]
    prob += 0  # feasibility
    prob += pulp.lpSum(zs) == r
    for v in range(10):
        prob += pulp.lpSum(zs[e] for e in range(len(E)) if v in E[e]) <= a[v]
    prob.solve(pulp.PULP_CBC_CMD(msg=0))
    return pulp.LpStatus[prob.status] == 'Optimal'

for s in range(1, 7):
    val, vec = alpha_sym(s)
    print(f"s={s} alpha={val} vec={vec}")
# failure candidates: take ILP extremals, test small r
# Also direct LP-based search for ratios using fractional data:
# brute-force: enumerate minimal feasible vectors for s up to 6? use ILP minimizers + C5 powers
# C5 monomial: vertices of an induced 5-cycle, exponent 1 each
# find induced 5-cycles
from petersen_core import NBR
cycles = set()
import itertools
for S in itertools.combinations(range(10), 5):
    ms = set(S)
    degs = {v: len([w for w in NBR[v] if w in ms]) for v in S}
    if all(d == 2 for d in degs.values()):
        cycles.add(tuple(sorted(S)))
print("induced 5-cycles:", len(cycles))
c0 = list(cycles)[0]
print("example:", c0, ["".join(map(str, __import__('petersen_core').BASE[v])) for v in c0])
for k in (1, 2, 3):
    a = [0]*10
    for v in c0: a[v] = k
    # check cover sums
    print(f"k={k} cover sums:", sorted(sum(Cmat[c][v]*a[v] for v in range(10)) for c in range(len(covers))))
    for r in range(1, 2*k+1):
        print(f"   in I^{r}?", in_ordinary(a, r))
