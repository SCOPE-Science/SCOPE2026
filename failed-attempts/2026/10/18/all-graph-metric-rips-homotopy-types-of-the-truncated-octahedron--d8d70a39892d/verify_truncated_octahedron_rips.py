#!/usr/bin/env python3
"""Reproduce the truncated-octahedral graph-metric Rips homotopy calculation.

Only the Python standard library is required. Simplices are nonzero bitmasks;
all complexes below use inclusive graph-distance thresholds.
"""
from collections import Counter, deque
from functools import lru_cache
from itertools import permutations, product

V = tuple(sorted({p for a,b in product((-1,1), repeat=2)
                  for p in permutations((0,a,2*b))}))
N = len(V)
assert N == 24
EDGES = {(i,j) for i in range(N) for j in range(i+1,N)
         if sum((V[i][k]-V[j][k])**2 for k in range(3)) == 2}
assert len(EDGES) == 36
ADJ = [set() for _ in range(N)]
for i,j in EDGES:
    ADJ[i].add(j)
    ADJ[j].add(i)
assert set(map(len, ADJ)) == {3}
D = []
for s in range(N):
    d = [-1]*N
    d[s] = 0
    q = deque([s])
    while q:
        u = q.popleft()
        for w in ADJ[u]:
            if d[w] < 0:
                d[w] = d[u] + 1
                q.append(w)
    assert all(x >= 0 for x in d)
    D.append(d)
DISTANCE_COUNTS = Counter(D[i][j] for i in range(N) for j in range(i+1,N))
assert DISTANCE_COUNTS == {1:36,2:60,3:72,4:60,5:36,6:12}
assert all([j for j in range(N) if D[i][j] == 6] == [V.index(tuple(-a for a in V[i]))]
           for i in range(N))

def ones(mask):
    while mask:
        b = mask & -mask
        yield b.bit_length()-1
        mask -= b

def all_faces(r):
    neighbors = [sum(1<<j for j in range(N) if j != i and D[i][j] <= r)
                 for i in range(N)]
    result = set()
    def extend(prefix, options):
        for offset, vertex in enumerate(options):
            face = prefix | (1<<vertex)
            result.add(face)
            extend(face, [v for v in options[offset+1:]
                          if (neighbors[vertex] >> v) & 1])
    extend(0, list(range(N)))
    return result

def pivot_matching(faces, order):
    free = set(faces)
    pairs = {}
    for vertex in order:
        b = 1<<vertex
        for lower in sorted(free):
            upper = lower|b
            if lower in free and not lower&b and upper in free:
                assert upper.bit_count() == lower.bit_count()+1
                pairs[lower] = upper
                free.remove(lower)
                free.remove(upper)
    assert len(faces) == 2*len(pairs)+len(free)
    return pairs,free

def check_acyclic(faces, pairs):
    """Check every oriented Hasse arrow, not just a sample of gradient paths."""
    following = {f:[] for f in faces}
    indegree = {f:0 for f in faces}
    edges = 0
    for upper in faces:
        for v in ones(upper):
            lower = upper^(1<<v)
            if not lower:
                continue
            assert lower in faces
            source,target = (lower,upper) if pairs.get(lower) == upper else (upper,lower)
            following[source].append(target)
            indegree[target] += 1
            edges += 1
    queue = deque(k for k in faces if indegree[k] == 0)
    processed = 0
    while queue:
        u = queue.popleft()
        processed += 1
        for v in following[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
    assert processed == len(faces), 'cyclic discrete Morse matching'
    return edges

def dim_profile(faces):
    return dict(sorted(Counter(f.bit_count()-1 for f in faces).items()))

PIVOT_ORDER = [4,18,2,8,3,15,14,22,12,16,19,1,7,0,6,9,10,5,13,21,17,23,11,20]
assert sorted(PIVOT_ORDER) == list(range(N))
COMPLEXES = {}
MATCHINGS = {}
for r,order,expected_faces,expected_critical in (
    (2,PIVOT_ORDER,{0:24,1:96,2:112,3:30},{0:1,2:9}),
    (3,PIVOT_ORDER,{0:24,1:168,2:472,3:618,4:384,5:92},{0:1,2:1}),
    (4,list(range(N)),{0:24,1:228,2:1112,3:3042,4:4848,5:4592,
                       6:2592,7:822,8:112},{0:1,4:6,5:3})):
    faces = all_faces(r)
    assert dim_profile(faces) == expected_faces, (r,dim_profile(faces))
    pairs,critical = pivot_matching(faces,order)
    assert dim_profile(critical) == expected_critical, (r,dim_profile(critical))
    hasse_edges = check_acyclic(faces,pairs)
    COMPLEXES[r] = faces
    MATCHINGS[r] = (pairs,critical)
    print('MORSE',r,'faces',len(faces),'pairs',len(pairs),
          'critical',dim_profile(critical),'Hasse_arrows',hasse_edges)

# Exact integral Morse differential between the r=4 critical 5- and 4-cells.
# The orientation of a face is increasing vertex order; R follows every
# dimension-4/5 gradient path, with its integral incidence sign.
pairs,critical = MATCHINGS[4]
crit4 = sorted(s for s in critical if s.bit_count()==5)
crit5 = sorted(s for s in critical if s.bit_count()==6)
crit_index = {face:i for i,face in enumerate(crit4)}
low45 = {a:b for a,b in pairs.items() if a.bit_count()==5}

def boundary(face):
    return [(face^(1<<v), -1 if k&1 else 1)
            for k,v in enumerate(ones(face))]

@lru_cache(maxsize=None)
def project4(face):
    if face in crit_index:
        return {crit_index[face]:1}
    if face not in low45:
        return {}
    upper = low45[face]
    own_sign = next(s for t,s in boundary(upper) if t==face)
    out = Counter()
    for other,sign in boundary(upper):
        if other == face:
            continue
        for index,coeff in project4(other).items():
            out[index] -= own_sign*sign*coeff
    return {k:v for k,v in out.items() if v}

M = [[0]*len(crit5) for _ in crit4]
for j,upper in enumerate(crit5):
    for lower,sign in boundary(upper):
        for i,coeff in project4(lower).items():
            M[i][j] += sign*coeff
assert M == [[-1,-1,0],[0,0,0],[1,1,0],[0,0,0],[1,1,0],[1,1,0]], M
# Nonzero entries are units; rank=1, and the image is primitive.
assert M[0][0]==-1 and all(M[i][0] == M[i][1] and M[i][2]==0 for i in range(6))
print('INTEGRAL_MORSE_BOUNDARY_4x5',M, 'rank',1,'smith_nonzero',[1])

# Independent exact mod-2 simplicial boundary ranks: no Morse paths used.
def mod_two_betti(faces):
    by_degree = {}
    for f in faces:
        by_degree.setdefault(f.bit_count()-1,[]).append(f)
    for cells in by_degree.values():cells.sort()
    rank = {}
    for k in sorted(by_degree):
        if k==0:
            continue
        index = {f:i for i,f in enumerate(by_degree[k-1])}
        pivots = {}
        for upper in by_degree[k]:
            column=0
            for vertex in ones(upper):
                column ^= 1<<index[upper^(1<<vertex)]
            while column:
                p=column.bit_length()-1
                if p in pivots:
                    column ^= pivots[p]
                else:
                    pivots[p]=column
                    break
        rank[k]=len(pivots)
    betti = {k:len(cells)-rank.get(k,0)-rank.get(k+1,0)
             for k,cells in by_degree.items()}
    betti[0] -= 1
    return {k:v for k,v in betti.items() if v},rank
for r,expected in ((2,{2:9}),(3,{2:1}),(4,{4:5,5:2})):
    actual,ranks = mod_two_betti(COMPLEXES[r])
    assert actual == expected, (r,actual)
    print('MOD2',r,'betti',actual,'ranks',ranks)

assert not any(all(D[i][j]<=1 for i,j in __import__('itertools').combinations(s,2))
               for s in __import__('itertools').combinations(range(N),3))
assert len(all_faces(1)) == 24+36
# Distances 6 are exclusively antipodal pairs, so the r=5 complex is
# the join of twelve two-point sets: the boundary of the 12-crosspolytope.
# At r=6 it is the full simplex on 24 vertices.
print('VERIFY_OK vertices=24 graph_edges=36 diameter=6 rips_faces_r4=17372')
