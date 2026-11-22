"""Exact majority-dynamics basin computation on the Petersen and Desargues graphs.

This verification uses a 10-vertex enumeration, an explicit 20-vertex
edge-isomorphism witness, and integer convolution of attractor basins.
Run: python3 verify_lift.py
"""
from collections import Counter

P = [(0,1),(0,4),(0,5),(1,2),(1,6),(2,3),(2,7),(3,4),(3,8),(4,9),
     (5,7),(5,8),(6,8),(6,9),(7,9)]
D = [(0,1),(0,19),(0,5),(1,2),(1,16),(2,3),(2,11),(3,4),(3,14),
     (4,5),(4,9),(5,6),(6,7),(6,15),(7,8),(7,18),(8,9),(8,13),
     (9,10),(10,11),(10,19),(11,12),(12,13),(12,17),(13,14),
     (14,15),(15,16),(16,17),(17,18),(18,19)]
# Labels of the two Petersen-lift layers for Desargues vertex labels 0...19.
PHI = (0,11,6,19,7,15,8,16,1,12,3,18,5,10,4,13,2,17,9,14)

def normedges(edges):
    return {tuple(sorted(edge)) for edge in edges}

lift_edges = [(a, b+10) for a,b in P] + [(a+10,b) for a,b in P]
assert len(set(PHI)) == 20
assert normedges([(PHI[a],PHI[b]) for a,b in D]) == normedges(lift_edges)

def neighbor_masks(n, edges):
    masks = [0]*n
    for a,b in edges:
        assert 0 <= a < n and 0 <= b < n and a != b
        masks[a] |= 1 << b
        masks[b] |= 1 << a
    assert all(v.bit_count() == 3 for v in masks)
    return masks

masks = neighbor_masks(10,P)
def f(x):
    return sum(1 << i for i,m in enumerate(masks) if (x&m).bit_count() >= 2)

F = [f(x) for x in range(1024)]
assert all(F[F[F[F[F[F[x]]]]]] == F[F[F[F[x]]]] for x in range(1024))
# Each state stabilizes to a period at most 2; six double steps are safe.
def phase(x):
    for _ in range(6):
        x = F[F[x]]
    assert F[F[x]] == x
    return x

B = Counter(phase(x) for x in range(1024))
R = sorted(B)
assert len(R) == 124 and sum(B.values()) == 1024
assert Counter(B.values()) == {1:72,10:50,226:2}
# Number of initial states entering an attractor by exactly time t.
base_entry = Counter()
for x in range(1024):
    y=x
    for t in range(100):
        if F[F[y]] == y:
            base_entry[t] += 1
            break
        y=F[y]
    else:
        raise AssertionError("no period-two entry")
assert [base_entry[i] for i in range(5)] == [124,260,400,120,120]

lift_fixed = Counter()
for r in R:
    lift_fixed[B[r]*B[F[r]]] += 1

lift_two = Counter()
seen=set()
for r in R:
    for s in R:
        if s == F[r] or (r,s) in seen:
            continue
        partner = (F[s], F[r])
        seen.add((r,s));seen.add(partner)
        basin = B[r]*B[s] + B[F[s]]*B[F[r]]
        lift_two[basin] += 1
assert len(seen) == len(R)**2-len(R)

assert lift_fixed == {1:72,100:50,51076:2}
assert lift_two == {2:2556,20:3600,200:1225,452:144,4520:100,102152:1}
assert sum(k*v for k,v in lift_fixed.items()) == 107224
assert sum(k*v for k,v in lift_two.items()) == 941352
assert sum(k*v for k,v in (lift_fixed+lift_two).items()) == 1048576
assert sum(lift_fixed.values()) == 124
assert sum(lift_two.values()) == 7626
c=0; prev=0; lift_entry=[]
for t in range(5):
    c += base_entry[t]
    lift_entry.append(c*c-prev)
    prev=c*c
assert lift_entry == [15376,132080,467200,202560,231360]
print("Petersen phase-basin histogram:",sorted(Counter(B.values()).items()))
print("Desargues fixed-orbit basin histogram:",sorted(lift_fixed.items()))
print("Desargues two-orbit basin histogram:",sorted(lift_two.items()))
print("Desargues exact entry-time profile:",lift_entry)
print("Desargues orbit counts:",sum(lift_fixed.values()),sum(lift_two.values()))
print("Desargues state totals:",sum(k*v for k,v in lift_fixed.items()),
      sum(k*v for k,v in lift_two.items()))
print("PASS")
