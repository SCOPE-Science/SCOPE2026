from petersen_core import BASE, EDGES, all_minimal_covers
from itertools import combinations_with_replacement
from collections import Counter
covers = all_minimal_covers()
Cmat = [[(m >> v) & 1 for v in range(10)] for m in covers]
E = EDGES
gens2 = []
for i, j in combinations_with_replacement(range(len(E)), 2):
    g = [0]*10
    for e in (E[i], E[j]):
        g[e[0]] += 1; g[e[1]] += 1
    gens2.append(tuple(g))
def witness(a):
    for g in gens2:
        if all(g[v] <= a[v] for v in range(10)):
            return g
    return None
import itertools
degs = Counter()
shapes = []
for a in itertools.product(range(4), repeat=10):
    feas = all(sum(row[v]*a[v] for v in range(10)) >= 3 for row in Cmat)
    if not feas: continue
    # minimality
    mins = True
    for v in range(10):
        if a[v] == 0: continue
        still = all(sum(row[w]*a[w] for w in range(10)) - row[v] >= 3 for row in Cmat)
        if still:
            mins = False; break
    if not mins: continue
    degs[sum(a)] += 1
    w = witness(a)
    assert w is not None
    r = tuple(sorted([a[v] - w[v] for v in range(10)], reverse=True))
    shapes.append((a, w))
print("minimal degree distribution:", sorted(degs.items()))
# max coordinate check
mx = max(max(a) for a, w in shapes)
print("max coordinate among minimal:", mx)
# squarefree-minimal (0/1) count? and sample witnesses
n01 = sum(1 for a, w in shapes if max(a) <= 1)
print("0/1 minimals:", n01)
import random
for a, w in shapes[:15]:
    print(a, "deg", sum(a), "<- I^2 gen", w)
