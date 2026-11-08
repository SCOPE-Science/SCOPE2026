"""Reproduce the integral homotopy and full rational homology character of the folded five-cube independence complex.
Python 3 standard library only; no input data files required.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import permutations

DIRECTIONS = (1, 2, 4, 8, 15)
N = 16
NEIGH = [sum(1 << (v ^ d) for d in DIRECTIONS) for v in range(N)]
EDGES = {(v, v ^ d) for v in range(N) for d in DIRECTIONS if v < (v ^ d)}
assert len(EDGES) == 40
assert len(set(DIRECTIONS)) == 5
assert all(len({v ^ d for d in DIRECTIONS}) == 5 for v in range(N))

FACES = {mask for mask in range(1, 1 << N)
         if all(not (mask & NEIGH[v]) for v in range(N) if mask & (1 << v))}
F_VECTOR = tuple(sum(m.bit_count() == k for m in FACES) for k in range(1, 6))
assert len(FACES) == 392 and F_VECTOR == (16, 80, 160, 120, 16)

# The same mathematical matching is specified entirely by the integer mask and a pivot order.
remaining = set(FACES)
pairs = []
for v in range(N):
    for lower in sorted(remaining):
        upper = lower | (1 << v)
        if not (lower & (1 << v)) and upper in remaining:
            pairs.append((lower, upper))
            remaining.remove(lower)
            remaining.remove(upper)
critical = sorted(remaining)
assert len(pairs) == 190 and len(critical) == 12
assert Counter(m.bit_count()-1 for m in critical) == {0:1, 2:1, 3:10}
assert 1 in critical

# Orient every Hasse cover down except matched covers which are reversed.
pair_upper = {upper: lower for lower, upper in pairs}
out = defaultdict(list)
indegree = {m: 0 for m in FACES}
hasse = 0
for upper in FACES:
    for v in range(N):
        if not (upper & (1 << v)):
            continue
        lower = upper ^ (1 << v)
        if lower not in FACES:
            continue
        a, b = (lower, upper) if pair_upper.get(upper) == lower else (upper, lower)
        out[a].append(b)
        indegree[b] += 1
        hasse += 1
queue = deque(v for v in sorted(FACES) if indegree[v] == 0)
visited = 0
while queue:
    a = queue.popleft()
    visited += 1
    for b in out[a]:
        indegree[b] -= 1
        if indegree[b] == 0:
            queue.append(b)
assert visited == len(FACES) and hasse == 1200

# Integral algebraic-Morse reduction using the unit coefficients in the paired boundaries.
pivot = dict(pairs)
def boundary(mask):
    vs = [v for v in range(N) if mask & (1 << v)]
    return {mask ^ (1 << v): (-1)**i for i, v in enumerate(vs)}

@lru_cache(None)
def expand(mask):
    if mask not in pivot:
        return {mask: 1}
    upper = pivot[mask]
    b = boundary(upper)
    unit = b.pop(mask)
    assert abs(unit) == 1
    reduced = defaultdict(int)
    for other, coef in b.items():
        for critical_face, weight in expand(other).items():
            reduced[critical_face] -= (coef // unit) * weight
    return {v: w for v, w in reduced.items() if w}

critical2 = [m for m in critical if m.bit_count() == 3]
critical3 = [m for m in critical if m.bit_count() == 4]
assert critical2 == [1048]
assert critical3 == [1680,2400,10370,18564,24720,26880,33320,33864,36960,38400]
degree_vector = []
for b in critical3:
    red = defaultdict(int)
    for lower, weight in boundary(b).items():
        for c, coef in expand(lower).items():
            red[c] += weight * coef
    degree_vector.append(red[critical2[0]])
assert degree_vector == [1,1,0,0,-1,-1,0,0,-1,-1]
# As a gcd-one vector, the attaching map is surjective with primitive kernel Z^9.

# Independent mod-2 simplicial-boundary rank check.
def rank_mod2(k):
    low = sorted(m for m in FACES if m.bit_count() == k)
    high = sorted(m for m in FACES if m.bit_count() == k+1)
    row_index = {m:i for i,m in enumerate(low)}
    pivots={}
    for face in high:
        col=0
        for subface in boundary(face):
            col ^= 1 << row_index[subface]
        while col:
            h=col.bit_length()-1
            if h not in pivots:
                pivots[h]=col
                break
            col^=pivots[h]
    return len(pivots)
RANKS = [rank_mod2(i) for i in range(1,5)]
assert RANKS == [15,65,95,16]

# The full group is the 16 translations semi-direct S5 permuting the five directions.
def parity_of_permutation(seq):
    return (-1)**sum(seq[i] > seq[j] for i in range(len(seq)) for j in range(i+1, len(seq)))

def lefschetz_character(perm):
    ordinary_L = 0
    for mask in FACES:
        vs = [i for i in range(N) if mask & (1 << i)]
        images = [perm[i] for i in vs]
        if sum(1 << x for x in images) != mask:
            continue
        ordinary_L += (-1)**(len(vs)-1) * parity_of_permutation(images)
    return 1 - ordinary_L

all_vertex_actions = set()
char_counts=Counter()
char_sum=0
s5_classes=defaultdict(set)
translation_counts=Counter()
for sig in permutations(range(5)):
    # Binary-linear automorphism determined by images of the first four generators.
    images = [DIRECTIONS[sig[i]] for i in range(4)]
    lin = [0]*N
    for vertex in range(N):
        lin[vertex] = 0
        for j in range(4):
            if vertex & (1 << j):
                lin[vertex] ^= images[j]
    assert len(set(lin)) == N
    sign=parity_of_permutation(sig)
    fixed_dirs=[i for i in range(5) if sig[i] == i]
    seen=set()
    cycle_lengths=[]
    for j in range(5):
        if j not in seen:
            count=0;k=j
            while k not in seen:
                seen.add(k);count+=1;k=sig[k]
            cycle_lengths.append(count)
    cycletype=tuple(sorted(cycle_lengths,reverse=True))
    for t in range(16):
        perm=tuple(v ^ t for v in lin)
        assert perm not in all_vertex_actions
        all_vertex_actions.add(perm)
        assert all(tuple(sorted((perm[u],perm[v]))) in EDGES for u,v in EDGES)
        actual=lefschetz_character(perm)
        rep=[(t >> j) & 1 for j in range(4)] + [0]
        common_parity=sum(rep)&1
        predicted=sign*(len(fixed_dirs)-1+sum((-1)**(common_parity ^ rep[j]) for j in fixed_dirs))
        assert actual==predicted, (sig,t,actual,predicted)
        char_counts[actual]+=1
        char_sum+=actual
        if t==0:s5_classes[cycletype].add(actual)
        if sig==tuple(range(5)):translation_counts[actual]+=1
assert len(all_vertex_actions) == 1920
assert char_counts == {9:1,5:10,3:80,1:865,-1:884,-3:60,-5:20}
assert translation_counts == {9:1,5:10,1:5}
assert char_sum == 0
assert s5_classes == {(1,1,1,1,1):{9},(2,1,1,1):{-5},(2,2,1):{1},(3,1,1):{3},(3,2):{1},(4,1):{-1},(5,):{-1}}
print('CLEBSCH_INDEPENDENCE_FULL_EQUIVARIANT_H3_PASS')
print('graph_vertices=16 edges=40 automorphisms=1920')
print('independence_faces=392 f_vector='+str(F_VECTOR))
print('Hasse_covers=1200 matched_pairs=190 acyclic=True')
print('critical_cells='+str(dict(sorted(Counter(m.bit_count()-1 for m in critical).items()))))
print('integral_Morse_degree_vector='+str(degree_vector))
print('boundary_ranks_mod_2='+str(RANKS))
print('integral_homotopy_type=wedge_of_9_three_spheres')
print('full_character_formula_verified_all_1920=True')
print('character_values_multiplicities='+str(sorted(char_counts.items())))
print('S5_cycle_types='+str(sorted((k,next(iter(v))) for k,v in s5_classes.items())))
print('full_group_invariants=0')
print('rational_modules=sign_twist_standard_S5_dim4_plus_sign_twist_signed_direction_dim5')
