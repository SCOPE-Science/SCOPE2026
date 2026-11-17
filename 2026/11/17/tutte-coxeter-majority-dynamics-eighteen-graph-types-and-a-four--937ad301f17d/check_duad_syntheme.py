"""Exact 15-bit majority certificate for the Tutte--Coxeter graph.
Run with Python 3 (standard library only). All 32,768 possibilities are checked.
"""
from collections import Counter
from itertools import combinations, permutations

pairs = tuple(combinations(range(6), 2))
pi = {edge: i for i, edge in enumerate(pairs)}

def matchings(vertices):
    if not vertices:
        yield ()
        return
    u = vertices[0]
    for v in vertices[1:]:
        rem = tuple(x for x in vertices[1:] if x != v)
        for rest in matchings(rem):
            yield ((u, v),) + rest

matching = tuple(matchings(tuple(range(6))))
assert len(matching) == 15 and len(set(matching)) == 15
line_masks = tuple(sum(1 << pi[e] for e in m) for m in matching)
point_masks = tuple(sum(1 << j for j, m in enumerate(matching) if e in m)
                    for e in pairs)
assert all(x.bit_count() == 3 for x in line_masks + point_masks)


def majority(v, masks):
    return sum((1 << j) for j, m in enumerate(masks)
               if (v & m).bit_count() >= 2)

N = 1 << 15
L = [majority(s, line_masks) for s in range(N)]  # edge shore -> matching shore
P = [majority(s, point_masks) for s in range(N)]  # matching shore -> edge shore
G = [P[L[s]] for s in range(N)]
J = [L[P[s]] for s in range(N)]
assert all(G[G[G[s]]] == G[G[s]] for s in range(N))
assert all(J[J[J[s]]] == J[J[s]] for s in range(N))
assert any(G[G[s]] != G[s] for s in range(N))
A = {s for s in range(N) if G[s] == s}
B = {s for s in range(N) if J[s] == s}
assert len(A) == len(B) == 2386
assert all(P[L[s]] == s for s in A)
assert all(L[P[s]] == s for s in B)
assert {L[s] for s in A} == B

# For each time t the two original shores evolve independently; membership
# in the fixed set of the appropriate two-step map characterizes recurrence.
trackA = list(range(N))
trackB = list(range(N))
ctA, ctB = [], []
for t in range(5):
    ctA.append(sum(s in (A if t % 2 == 0 else B) for s in trackA))
    ctB.append(sum(s in (B if t % 2 == 0 else A) for s in trackB))
    trackA = [(L if t % 2 == 0 else P)[s] for s in trackA]
    trackB = [(P if t % 2 == 0 else L)[s] for s in trackB]
assert ctA == ctB == [2386, 16808, 25208, 28568, 32768]

# Period-resolved entrance counts use the terminal projections G^2 and J^2.
terminalA = [G[G[s]] for s in range(N)]
terminalB = [J[J[s]] for s in range(N)]
seqA = list(range(N)); seqB = list(range(N))
fixed_before = []
for t in range(5):
    accA = Counter(terminalA[s] for s in range(N)
                   if seqA[s] in (A if t%2 == 0 else B))
    accB = Counter(terminalB[s] for s in range(N)
                   if seqB[s] in (B if t%2 == 0 else A))
    fixed_before.append(sum(accA[u]*accB[L[u]] for u in A))
    seqA = [(L if t%2 == 0 else P)[v] for v in seqA]
    seqB = [(P if t%2 == 0 else L)[v] for v in seqB]
assert fixed_before == [2386, 264032, 1372112, 11129552, 39202352]

# Independent global-count algebra: the period-two state space is A x B.
fixed = len(A)
period2_states = len(A) * len(B)
primitive2 = (period2_states - fixed) // 2
entry_cumulative = [a*b for a,b in zip(ctA, ctB)]
entry_first = [entry_cumulative[0]] + [entry_cumulative[t]-entry_cumulative[t-1]
                                         for t in range(1,5)]
assert (fixed, primitive2) == (2386, 2845305)
assert entry_first == [5692996, 276815868, 352934400, 180687360, 257611200]
assert sum(entry_first) == 1 << 30
fixed_first=[fixed_before[0]]+[fixed_before[t]-fixed_before[t-1] for t in range(1,5)]
two_first=[v-w for v,w in zip(entry_first,fixed_first)]
assert fixed_first == [2386,261646,1108080,9757440,28072800]
assert two_first == [5690610,276554222,351826320,170929920,229538400]

# A complete, independent check of the 6-vertex relabelling-orbit structure
# of the edge-shore fixed states: all 156 unlabeled graph types on 6 vertices.
edge_rename = [[pi[tuple(sorted((perm[u], perm[v])))] for u, v in pairs]
               for perm in permutations(range(6))]
seen = bytearray(N)
orbit_info=[]
for s in range(N):
    if seen[s]:
        continue
    orbit=set()
    for perm in edge_rename:
        rem=s
        out=0
        while rem:
            one=rem & -rem
            bit=one.bit_length()-1
            out |= 1 << perm[bit]
            rem ^= one
        orbit.add(out)
    assert not any(seen[x] for x in orbit)
    assert all((x in A) == (s in A) for x in orbit)
    for x in orbit:seen[x]=1
    orbit_info.append((s, len(orbit), s in A))
assert len(orbit_info) == 156
assert sum(z for _,z,v in orbit_info if v) == 2386
assert sum(v for _,z,v in orbit_info) == 18
assert sorted(Counter(z for _,z,v in orbit_info if v).items()) == [
    (1,2),(10,2),(60,4),(72,2),(90,2),(180,2),(360,4)]
assert sorted(Counter(s.bit_count() for s in A).items()) == [
    (0,1),(4,90),(5,132),(6,430),(7,540),
    (8,540),(9,430),(10,132),(11,90),(15,1)]
print('geometry: 15 duads, 15 synthemes, 45 incidences')
print('projection identity: G^3=G^2, J^3=J^2; G^2 != G')
print('fixed points:',fixed)
print('primitive two-cycles:',primitive2)
print('eligible-one-shore-by-update:',ctA)
print('first-periodic-entry-by-update:',entry_first)
print('entry-time and eventual period-one:',fixed_first)
print('entry-time and eventual period-two:',two_first)
print('6-vertex graph isomorphism classes: 156; recurrent types: 18')
print('recurrent types by orbit size:',sorted(Counter(z for _,z,v in orbit_info if v).items()))
print('all exact assertions passed')
