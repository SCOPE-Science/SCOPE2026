from petersen_core import BASE, EDGES, all_minimal_covers
from itertools import combinations_with_replacement
covers = all_minimal_covers()
Cmat = [[(m >> v) & 1 for v in range(10)] for m in covers]
# generators of I^2: pairs of edges (with repetition) as exponent vectors
E = EDGES
gens2 = []
for i, j in combinations_with_replacement(range(len(E)), 2):
    g = [0]*10
    for e in (E[i], E[j]):
        g[e[0]] += 1; g[e[1]] += 1
    gens2.append(tuple(g))
print("num I^2 gens (with dup):", len(gens2))

def in_I2(a):
    return any(all(g[v] <= a[v] for v in range(10)) for g in gens2)

# enumerate box {0..3}^10, keep feasible (cover sums >=3)
import itertools
count_feas = 0
count_min = 0
counterex = []
# iterate product; 4^10 = 1048576, fine
for a in itertools.product(range(4), repeat=10):
    # quick degree prune? need full check
    feas = True
    for row in Cmat:
        s = 0
        for v in range(10):
            s += row[v]*a[v]
        if s < 3:
            feas = False; break
    if not feas:
        continue
    count_feas += 1
    # minimality: for each v with a[v]>0, a-e_v infeasible
    minimal = True
    for v in range(10):
        if a[v] == 0:
            continue
        still = True
        for row in Cmat:
            if row[v] == 0:
                continue
            s = 0
            for w in range(10):
                s += row[w]*a[w]
            if s - 1 < 3:
                still = False; break
        # careful: a-e_v feasible iff all covers containing v still >=3 i.e. s-1>=3, and covers not containing v unaffected (were >=3)
        if still:
            minimal = False; break
    if not minimal:
        continue
    count_min += 1
    if not in_I2(a):
        counterex.append(a)
print("feasible in box:", count_feas)
print("minimal feasible:", count_min)
print("counterexamples:", len(counterex))
for a in counterex[:10]:
    print("  ", a, "deg", sum(a))
