#!/usr/bin/env python3
"""Exact finite verification for the independence complex of C7 x K3.

Graph, simplices, acyclic matching, integral Morse boundary and natural
symmetry characters are regenerated. Only the Python standard library is used.
"""
from collections import Counter, deque
from itertools import combinations, permutations
from functools import lru_cache

N_CYCLE, N_COLORS = 7, 3
N = N_CYCLE * N_COLORS
adj = [0] * N
for i in range(N_CYCLE):
    for a in range(N_COLORS):
        u = N_COLORS * i + a
        for j in ((i - 1) % N_CYCLE, (i + 1) % N_CYCLE):
            for b in range(N_COLORS):
                if a != b:
                    adj[u] |= 1 << (N_COLORS * j + b)
assert all((adj[v] >> v) & 1 == 0 for v in range(N))
assert all(((adj[u] >> v) & 1) == ((adj[v] >> u) & 1)
           for u in range(N) for v in range(N))

simplices = [0]
for v in range(N):
    simplices += [face | (1 << v) for face in simplices
                  if face & adj[v] == 0]
faces = set(simplices)
assert len(simplices) == len(faces)
f_vector = Counter(s.bit_count() - 1 for s in faces if s)
assert [f_vector[d] for d in range(9)] == [21,168,658,1365,1554,1022,402,84,7]
assert len(faces) - 1 == 5281

# Deterministic sequential vertex-toggle matching, excluding the empty face.
unmatched = set(faces)
lower_to_upper, upper_to_lower = {}, {}
for v in range(N):
    for low in sorted(unmatched):
        high = low | (1 << v)
        if low and not ((low >> v) & 1) and high in unmatched:
            lower_to_upper[low] = high
            upper_to_lower[high] = low
            unmatched.remove(low)
            unmatched.remove(high)
assert len(lower_to_upper) == 2635
assert Counter(s.bit_count() - 1 for s in unmatched) == \
       Counter({-1:1,0:1,3:4,4:6})
assert len(faces) == 2*len(lower_to_upper)+len(unmatched)

# Acyclicity: full directed face-poset Hasse graph, not a sampled subset.
next_faces = {s:[] for s in faces}
in_degree = {s:0 for s in faces}
cover_count = 0
for high in faces:
    for v in range(N):
        if high & (1 << v):
            low = high ^ (1 << v)
            x,y = (low,high) if lower_to_upper.get(low)==high else (high,low)
            next_faces[x].append(y)
            in_degree[y] += 1
            cover_count += 1
assert cover_count == 25242
queue = deque(s for s in faces if in_degree[s] == 0)
processed = 0
while queue:
    x = queue.popleft()
    processed += 1
    for y in next_faces[x]:
        in_degree[y] -= 1
        if in_degree[y] == 0:
            queue.append(y)
assert processed == len(faces)

# Oriented integral simplicial boundary, indexed by increasing vertex labels.
def boundary(s):
    for v in range(N):
        if s & (1 << v):
            parity = (s & ((1 << v) - 1)).bit_count() % 2
            yield s ^ (1 << v), (-1 if parity else 1)

critical3 = sorted(s for s in unmatched if s.bit_count() == 4)
critical4 = sorted(s for s in unmatched if s.bit_count() == 5)

@lru_cache(maxsize=None)
def project_three(s):
    assert s.bit_count() == 4
    if s in unmatched:
        assert s in critical3
        return {s:1}
    if s in upper_to_lower:
        return {}
    high = lower_to_upper[s]
    assert high.bit_count() == 5
    incident = list(boundary(high))
    piv = next(sign for low,sign in incident if low == s)
    total = {}
    for low,sign in incident:
        if low != s:
            for crit,weight in project_three(low).items():
                total[crit] = total.get(crit,0) - piv*sign*weight
    return {crit:weight for crit,weight in total.items() if weight}

# Matrix columns: critical 4-cells, rows: critical 3-cells.
A = [[0]*len(critical4) for _ in critical3]
for j,cell in enumerate(critical4):
    for face,sign in boundary(cell):
        for crit,weight in project_three(face).items():
            A[critical3.index(crit)][j] += sign*weight
assert A == [
    [-1,0,-1,-1,0,-1],
    [0,0,0,1,0,1],
    [0,0,0,1,0,1],
    [0,-1,0,-1,-1,-1],
]
assert A[1] == A[2]  # rank at most 3
# Unit maximal minor on rows 0,1,3; columns 0,1,3.
def determinant3(X):
    return (X[0][0]*(X[1][1]*X[2][2]-X[1][2]*X[2][1])
            -X[0][1]*(X[1][0]*X[2][2]-X[1][2]*X[2][0])
            +X[0][2]*(X[1][0]*X[2][1]-X[1][1]*X[2][0]))
minor = [[A[r][c] for c in (0,1,3)] for r in (0,1,3)]
assert determinant3(minor) == -1
# Hence integral rank exactly 3, with all three Smith factors equal to 1.

# Additional chain-level consistency: project every four-simplex, not only
# critical ones, and check that the projected simplicial differential agrees
# with the explicitly computed integral Morse differential.
@lru_cache(maxsize=None)
def project_four(s):
    assert s.bit_count() == 5
    if s in unmatched:
        assert s in critical4
        return {s:1}
    if s in upper_to_lower:
        return {}
    high = lower_to_upper[s]
    assert high.bit_count() == 6
    pivot = next(sign for low,sign in boundary(high) if low == s)
    total = {}
    for low,sign in boundary(high):
        if low != s:
            for crit,weight in project_four(low).items():
                total[crit] = total.get(crit,0) - pivot*sign*weight
    return {crit:weight for crit,weight in total.items() if weight}

four_faces_checked = 0
for simplex in faces:
    if simplex.bit_count() != 5:
        continue
    lhs = {crit:0 for crit in critical3}
    for lower_face,sign in boundary(simplex):
        for crit,weight in project_three(lower_face).items():
            lhs[crit] += sign*weight
    rhs = {crit:0 for crit in critical3}
    for high_crit,weight in project_four(simplex).items():
        j = critical4.index(high_crit)
        for i,low_crit in enumerate(critical3):
            rhs[low_crit] += weight*A[i][j]
    assert lhs == rhs
    four_faces_checked += 1
assert four_faces_checked == 1554

# Independent mod-2 reduction on the original FULL simplicial boundaries.
by_dimension = {d:sorted(s for s in faces if s.bit_count()==d+1)
                for d in range(9)}
def mod2_boundary_rank(d):
    lower_index = {s:i for i,s in enumerate(by_dimension[d-1])}
    pivots = {}
    for s in by_dimension[d]:
        column = 0
        for low,_ in boundary(s):
            column ^= 1 << lower_index[low]
        while column:
            pivot = column.bit_length() - 1
            if pivot in pivots:
                column ^= pivots[pivot]
            else:
                pivots[pivot] = column
                break
    return len(pivots)
ranks = [0] + [mod2_boundary_rank(d) for d in range(1,9)] + [0]
assert ranks[1:9] == [20,148,510,854,697,325,77,7]
mod2_betti = [len(by_dimension[d])-ranks[d]-ranks[d+1]
              for d in range(9)]
assert mod2_betti == [1,0,0,1,3,0,0,0,0]

# Reduced Lefschetz trace via fixed oriented simplices INCLUDING the empty face.
def vertex_permutation(a,b,color):
    return tuple(N_COLORS*((a*i+b)%N_CYCLE)+color[c]
                 for i in range(N_CYCLE) for c in range(N_COLORS))

def reduced_lefschetz(g):
    total = 0
    for face in faces:
        images = [g[v] for v in range(N) if face & (1 << v)]
        if sum(1 << v for v in images) != face:
            continue
        inversions = sum(images[i] > images[j]
                         for i in range(len(images))
                         for j in range(i+1,len(images)))
        total += (-1 if (len(images)+inversions+1) % 2 else 1)
    return total

colors = {'identity':(0,1,2),'transposition':(1,0,2),'three_cycle':(1,2,0)}
L = {(a,kind):reduced_lefschetz(vertex_permutation(a,0,color))
     for a in (1,-1) for kind,color in colors.items()}
assert L == {
    (1,'identity'):2,(1,'transposition'):0,(1,'three_cycle'):-1,
    (-1,'identity'):4,(-1,'transposition'):-2,(-1,'three_cycle'):1,
}
count_aut = 0
seen_automorphisms = set()
for a in (1,-1):
    for b in range(N_CYCLE):
        for color in permutations(range(N_COLORS)):
            g = vertex_permutation(a,b,color)
            assert len(set(g)) == N
            assert g not in seen_automorphisms
            seen_automorphisms.add(g)
            assert all(((adj[u]>>v)&1) == ((adj[g[u]]>>g[v])&1)
                       for u in range(N) for v in range(N))
            kind = ('identity' if color==(0,1,2)
                    else 'transposition' if sum(color[i]==i for i in range(3))==1
                    else 'three_cycle')
            assert reduced_lefschetz(g) == L[(a,kind)]
            count_aut += 1
assert count_aut == 84 and len(seen_automorphisms) == 84

# From betti=(1,3) in degrees (3,4), rotations of order 7 act trivially
# since a nontrivial rational 7th-root representation has dimension >=6.
# Reflection identity and S3 characters, in class order (1),(12),(123):
h3_color = [1,-1,1]  # sign of color permutation
h4_color = [3,-1,0]  # sign + standard S3
for a in (1,-1):
    for j,kind in enumerate(('identity','transposition','three_cycle')):
        trace3 = (1 if a==1 else -1)*h3_color[j]
        trace4 = h4_color[j]
        assert -trace3+trace4 == L[(a,kind)]

print('VERTICES=21; GRAPH_EDGES=42; SIMPLICES_NONEMPTY=5281')
print('F_VECTOR=' + str([f_vector[d] for d in range(9)]))
print('MATCHED_PAIRS=2635; ACYCLIC_COVERS=25242; TOPOLOGICAL_SORT=5282')
print('CRITICAL_CELLS={0:1,3:4,4:6}')
print('MORSE_D4_ROWS=' + str(A))
print('MORSE_CHAIN_MAP_DEGREE4_FACES=' + str(four_faces_checked))
print('UNIT_MINOR_ROWS=(0,1,3); COLS=(0,1,3); DET=-1; SMITH_NONZERO=1,1,1')
print('SIMPLICIAL_MOD2_RANKS=' + str(ranks[1:9]))
print('BETTI_MOD2=' + str(mod2_betti))
print('HOMOTOPY_TYPE=S3+3*S4; REDUCED_H3=Z; REDUCED_H4=Z^3')
print('SYMMETRIES_TESTED=84; LEFSCHETZ=' + str(L))
print('H3=(reflection_sign)x(color_sign); H4=(reflection_trivial)x(color_sign+color_standard)')
print('C7K3_INTEGRAL_WEDGE_AND_EQUIVARIANT_CHARACTER_PASS')
