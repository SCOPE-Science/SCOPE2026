#!/usr/bin/env python3
"""Stand-alone exhaustive proof checks for the Möbius–Kantor dominance complex.
Run: python3 mk_dominance_verify.py
Only Python 3 standard library is needed.
"""
from collections import Counter, deque

N = 16
FULL = (1 << N) - 1
# Generalized Petersen G(8,3): outer vertices 0..7, inner vertices 8..15.
EDGES = set()
for i in range(8):
    for a,b in ((i,(i+1)%8),(i,8+i),(8+i,8+(i+3)%8)):
        EDGES.add(tuple(sorted((a,b))))
assert len(EDGES) == 24
NEIGH = [0]*N
for a,b in EDGES:
    NEIGH[a] |= 1 << b
    NEIGH[b] |= 1 << a
CLOSED = [(1 << i) | NEIGH[i] for i in range(N)]
assert all(m.bit_count()==4 for m in CLOSED)

# Test A: the hypergraph independence condition (closed neighborhoods are nonfaces).
faces_a = [mask for mask in range(1 << N)
           if all((mask & c) != c for c in CLOSED)]
# Test B: the complementary set is a dominating set.
faces_b = []
for mask in range(1 << N):
    remainder = FULL ^ mask
    covered = remainder
    for v in range(N):
        if remainder & (1 << v):
            covered |= NEIGH[v]
    if covered == FULL:
        faces_b.append(mask)
assert faces_a == faces_b
assert 0 in faces_a
FACES = set(faces_a)
F_NONEMPTY = FACES - {0}
assert len(F_NONEMPTY) == 32390
fvec = Counter(m.bit_count()-1 for m in F_NONEMPTY)
facets = [m for m in F_NONEMPTY if all((m|(1<<v)) not in FACES for v in range(N) if not m & (1<<v))]

# A canonical staged toggle matching.  Only nonempty faces participate.
# At each pivot, match every remaining face avoiding it with its upper face,
# then remove both.  The complete reversed-Hasse check below independently
# verifies the acyclicity needed by Forman's discrete Morse theorem.
def match_order(order):
    remaining = set(F_NONEMPTY)
    matched_upper = {}
    counts=[]
    for v in order:
        bit = 1 << v
        pairs = [(a,a|bit) for a in sorted(remaining)
                 if not (a & bit) and (a|bit) in remaining]
        for a,b in pairs:
            remaining.remove(a)
            remaining.remove(b)
            matched_upper[a] = b
        counts.append(len(pairs))
    assert sum(counts)*2 + len(remaining) == len(F_NONEMPTY)
    return remaining, matched_upper, counts


def check_directed_hasse(matching):
    # For an unmatched incidence upper -> lower, for a matched pair lower -> upper.
    indegree = {f:0 for f in F_NONEMPTY}
    adjacency = {f:[] for f in F_NONEMPTY}
    ninc = 0
    nmatches = 0
    for upper in F_NONEMPTY:
        bits = upper
        while bits:
            lowbit = bits & -bits
            lower = upper ^ lowbit
            bits ^= lowbit
            if not lower:
                continue
            ninc += 1
            if matching.get(lower) == upper:
                a,b=lower,upper
                nmatches += 1
            else:
                a,b=upper,lower
            adjacency[a].append(b)
            indegree[b] += 1
    assert nmatches == len(matching)
    queue=deque(f for f in F_NONEMPTY if indegree[f]==0)
    visited=0
    while queue:
        a=queue.popleft()
        visited += 1
        for b in adjacency[a]:
            indegree[b] -= 1
            if indegree[b]==0:
                queue.append(b)
    assert visited == len(F_NONEMPTY), (visited,len(F_NONEMPTY))
    return ninc,visited

crit, pairs, staged = match_order(range(N))
assert Counter(m.bit_count()-1 for m in crit) == {0:1,7:7}
inc,vis = check_directed_hasse(pairs)
crit2,pairs2,staged2=match_order(reversed(range(N)))
inc2,vis2=check_directed_hasse(pairs2)
assert inc==inc2
assert Counter(m.bit_count()-1 for m in crit2) == {0:1,7:7}
assert len(pairs)==len(pairs2)==16191
assert sum((-1)**(m.bit_count()-1) for m in F_NONEMPTY) == -6

# The natural order-eight rotation is a graph automorphism, hence a cellular
# action on the dominance complex; its degree-seven rational character is
# obtained from the alternating signed trace on simplicial chains.
def orientation_sign(sequence):
    inv=0
    for i,v in enumerate(sequence):
        for w in sequence[i+1:]:
            inv += v>w
    return -1 if inv&1 else 1

def rotation_character(k):
    action = [(i+k)%8 for i in range(8)] + [8+(i+k)%8 for i in range(8)]
    assert all(tuple(sorted((action[a],action[b]))) in EDGES for a,b in EDGES)
    lefschetz=0
    for face in F_NONEMPTY:
        indices=[v for v in range(N) if face&(1<<v)]
        image=[action[v] for v in indices]
        if sorted(image)==indices:
            lefschetz += (-1)**(len(indices)-1)*orientation_sign(image)
    # For a connected wedge of seven 7-spheres, L(g)=1-tr(H_7(g)).
    return 1-lefschetz
chars = [rotation_character(k) for k in range(8)]
assert chars == [7,-1,3,-1,7,-1,3,-1]
# Rational irreducibles of C8 factoring through C4:
# 2 trivial + 3 sign + one 2D representation by quarter-turns.
assert all(chars[k] == 2 + 3*((-1)**k) + ([2,0,-2,0][k%4]) for k in range(8))
assert sum(chars)//8 == 2
# Bipartite graph with a perfect matching (spokes) has min vertex cover 8.
color = [(i%2) for i in range(8)] + [1-(i%2) for i in range(8)]
assert all(color[a]!=color[b] for a,b in EDGES)
assert all(tuple(sorted((i,8+i))) in EDGES for i in range(8))
# No triangle or square, and at least one 6-cycle.
assert all(not(NEIGH[a] & NEIGH[b]) for a,b in EDGES)
for a in range(N):
    for b in range(a+1,N):
        if not (NEIGH[a] & (1<<b)):
            assert (NEIGH[a] & NEIGH[b]).bit_count() <= 1
# A 6-cycle exists by straightforward enumerative DFS.
def has_six_cycle():
    def dfs(path):
        if len(path)==6:
            return bool(NEIGH[path[-1]]&(1<<path[0]))
        for v in range(N):
            if (NEIGH[path[-1]]&(1<<v)) and v not in path:
                if dfs(path+[v]):return True
        return False
    return any(dfs([v]) for v in range(N))
assert has_six_cycle()
print('GRAPH vertices=16 edges=24 regular_degree=3 girth=6 vertex_cover=8')
print('FACES nonempty=',len(F_NONEMPTY),'facets=',len(facets),'fvector=',sorted(fvec.items()))
print('MORSE_FORWARD pairs=',len(pairs),'critical=',sorted(Counter(m.bit_count()-1 for m in crit).items()),'hasse=',inc,'acyclic_vertices=',vis)
print('MORSE_REVERSE pairs=',len(pairs2),'critical=',sorted(Counter(m.bit_count()-1 for m in crit2).items()),'hasse=',inc2,'acyclic_vertices=',vis2)
print('HOMOTOPY wedge_of_7_spheres_dimension_7; integral_H7=Z^7; lower_reduced=0')
print('SYMMETRY C8_degree7_character=',chars,'rational_module=2*trivial+3*sign+one_quarter_turn_dim2')
print('DUAL vertex_cover_connectivity_bound 6+2=8')
print('VERIFY_OK')
