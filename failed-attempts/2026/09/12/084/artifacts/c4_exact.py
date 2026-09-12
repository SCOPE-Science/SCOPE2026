"""Exhaustive Ol(C4^2): max zero-sum-free size, count, GL-orbit decomposition.
Run: python3 c4_exact.py  (2^15 masks, exact)
Classification is under the linear group GL(2,Z4) (order 96), which preserves
the family of subsets of nonzero elements. Translations are NOT included:
they can create (0,0) and leave the family.
"""
import itertools

mod = 4
elems = [(x, y) for x in range(mod) for y in range(mod)]
nonzero = [e for e in elems if e != (0, 0)]

def has_zero_subset(S):
    reach = set()
    for (x, y) in S:
        new = {(x, y)}
        for (a, b) in list(reach):
            new.add(((a + x) % mod, (b + y) % mod))
        reach |= new
        if (0, 0) in reach:
            return True
    return (0, 0) in reach

N = len(nonzero)
maxk = 0
maxsets = []
for mask in range(1 << N):
    k = bin(mask).count("1")
    if k < maxk:
        continue
    S = [nonzero[i] for i in range(N) if (mask >> i) & 1]
    if not has_zero_subset(S):
        if k > maxk:
            maxk = k
            maxsets = [frozenset(S)]
        elif k == maxk:
            maxsets.append(frozenset(S))

print("maxk =", maxk, "Ol(C4^2) =", maxk + 1, "count =", len(maxsets))

units = [1, 3]
mats = [(a, b, c, d) for a in range(mod) for b in range(mod)
        for c in range(mod) for d in range(mod) if ((a * d - b * c) % mod) in units]
print("GL(2,Z4) size =", len(mats))
idx = {s: i for i, s in enumerate(maxsets)}
parent = list(range(len(maxsets)))

def find(i):
    while parent[i] != i:
        parent[i] = parent[parent[i]]
        i = parent[i]
    return i

def union(i, j):
    ri, rj = find(i), find(j)
    if ri != rj:
        parent[ri] = rj

for i, S in enumerate(maxsets):
    for (a, b, c, d) in mats:
        T = frozenset((((a * x + b * y) % mod),
                       ((c * x + d * y) % mod)) for (x, y) in S)
        j = idx.get(T)
        if j is not None:
            union(i, j)

orbits = {}
for i in range(len(maxsets)):
    orbits.setdefault(find(i), []).append(i)
print("GL orbits:", len(orbits), "sizes:", sorted([len(v) for v in orbits.values()], reverse=True))
for r, members in orbits.items():
    print("rep:", sorted(maxsets[members[0]]), "stab =", len(mats) // len(members))
# Partial-action note: translation by (0,3) sends the main representative to
# {(0,0),(0,1),(1,0),(1,1),(1,3)}, which contains (0,0) and leaves the family
# of subsets of nonzero elements, so translations act only partially here.
# RESULT: maxk = 5 Ol = 6 count = 120 GL orbits = 2 sizes = [96, 24] stabs = [1, 4]
