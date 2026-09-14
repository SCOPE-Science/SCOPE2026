from petersen_core import BASE, EDGES, all_minimal_covers
from collections import Counter
covers = all_minimal_covers()
print("covers (sorted vertex lists):")
for i, m in enumerate(covers):
    S = sorted(v for v in range(10) if (m >> v) & 1)
    print(i, "size", len(S), S, ["".join(str(x) for x in BASE[v]) for v in S])
# count vertex incidences
inc = [sum(1 for m in covers if (m >> v) & 1) for v in range(10)]
print("incidences per vertex over all 15:", inc)
# size-6 covers
six = [m for m in covers if bin(m).count('1') == 6]
print("num size-6:", len(six))
inc6 = [sum(1 for m in six if (m >> v) & 1) for v in range(10)]
print("incidences over 5 six-covers:", inc6)
# check each vertex in exactly 3 of the five?
# complements of six-covers = 4-sets; check independent
from itertools import combinations
eset = set()
for u, v in EDGES:
    eset.add((u, v)); eset.add((v, u))
for m in six:
    comp = [v for v in range(10) if not ((m >> v) & 1)]
    indep = all((u, v) not in eset for u in comp for v in comp if u != v)
    print("complement", sorted(comp), "independent?", indep)
# independent 4-sets count
n4 = 0
for S in combinations(range(10), 4):
    ms = set(S)
    if all(not (u in ms and v in ms) for u, v in EDGES):
        n4 += 1
print("independent 4-sets:", n4)
