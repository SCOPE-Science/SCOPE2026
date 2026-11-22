"""Exhaustive finite checker for the Cayley digraph's directed-forest complex and rotation quotient.
Requires Python 3.9+ standard library only. All indexing and matrices are generated afresh.
"""
from collections import defaultdict, Counter, deque
from itertools import combinations

N = 7
ARCS = tuple(sorted((i, (i+s) % N) for i in range(N) for s in (1, 2)))
assert len(ARCS) == 14 and len(set(ARCS)) == 14
INDEX = {a: j for j, a in enumerate(ARCS)}
PIVOTS = [INDEX[(i, (i+1)%N)] for i in range(N)] + [INDEX[(i,(i+2)%N)] for i in range(N)]

def is_face(mask):
    parents = {}
    for j, (source,target) in enumerate(ARCS):
        if mask & (1 << j):
            if target in parents:
                return False
            parents[target] = source
    for x in parents:
        seen=set(); y=x
        while y in parents:
            if y in seen:
                return False
            seen.add(y); y=parents[y]
    return True

FACES = frozenset(mask for mask in range(1 << len(ARCS)) if is_face(mask))
BY_SIZE = {k: sorted(m for m in FACES if m.bit_count()==k) for k in range(8)}
assert len(FACES)==1849
assert [len(BY_SIZE[k]) for k in range(8)] == [1,14,84,280,553,616,301,0]

# Stagewise vertex-toggle discrete Morse matching. Include empty face for a reduced matching.
unmatched = set(FACES)
matched_pairs = []
for v in PIVOTS:
    bit = 1 << v
    eligible = sorted(m for m in unmatched if not m & bit and m | bit in unmatched)
    for m in eligible:
        assert m in unmatched and m | bit in unmatched
        unmatched.remove(m)
        unmatched.remove(m | bit)
        matched_pairs.append((m,m | bit))
assert len(matched_pairs)==910
assert len(unmatched)==29 and all(m.bit_count()==6 for m in unmatched)
matched_edges = set(matched_pairs)
assert len({v for pair in matched_pairs for v in pair})==2*len(matched_pairs)

# Acyclicity of Forman matching: unmatched incidences point from higher to lower;
# matched incidences point from lower to higher. Test the ENTIRE directed Hasse diagram.
adj = {m: [] for m in FACES}
indeg = {m: 0 for m in FACES}
for hi in FACES:
    sub = hi
    while sub:
        bit = sub & -sub; sub -= bit
        lo = hi ^ bit
        if (lo,hi) in matched_edges:
            u,v = lo,hi
        else:
            u,v = hi,lo
        adj[u].append(v)
        indeg[v] += 1
queue = deque(m for m in FACES if indeg[m]==0)
processed = 0
while queue:
    u=queue.popleft(); processed+=1
    for v in adj[u]:
        indeg[v]-=1
        if indeg[v]==0: queue.append(v)
assert processed==len(FACES), (processed,len(FACES))

# Rotation of underlying Cayley graph on arcs and induced action on simplex orientations.
ROT = []
for shift in range(N):
    ROT.append(tuple(INDEX[((s+shift)%N,(t+shift)%N)] for s,t in ARCS))
def rotated(mask, shift):
    return sum(1 << ROT[shift][j] for j in range(14) if (mask >> j)&1)
def orbitrep(mask):
    return min(rotated(mask,k) for k in range(N))
assert all(rotated(m,k) != m for m in FACES if m for k in range(1,N))
ORBIT_REPS = {k: sorted(set(orbitrep(m) for m in BY_SIZE[k])) for k in range(1,7)}
assert [len(ORBIT_REPS[k]) for k in range(1,7)]==[2,12,40,79,88,43]

# Integer cellular boundary of the free cyclic quotient. Each orbit representative
# is oriented by its ascending arc-index ordering.
def orientation_sign(original, shift):
    ids=[ROT[shift][j] for j in range(14) if original>>j&1]
    return -1 if sum(ids[i]>ids[j] for i in range(len(ids)) for j in range(i+1,len(ids)))%2 else 1

def quotient_boundary(k):
    lo = {m:i for i,m in enumerate(ORBIT_REPS[k-1])}
    mat = [[0]*len(ORBIT_REPS[k]) for _ in range(len(lo))]
    for c,top in enumerate(ORBIT_REPS[k]):
        ids=[j for j in range(14) if top>>j&1]
        for i,j in enumerate(ids):
            f=top^(1<<j)
            for shift in range(N):
                if rotated(f,shift)==orbitrep(f):break
            else: raise AssertionError('orbit lookup failed')
            r=lo[orbitrep(f)]
            mat[r][c] += (-1 if i%2 else 1)*orientation_sign(f,shift)
    return mat
B={k:quotient_boundary(k) for k in range(2,7)}
for k in range(3,7):
    left=B[k-1];right=B[k]
    for i in range(len(left)):
        for j in range(len(right[0])):
            assert sum(left[i][h]*right[h][j] for h in range(len(right)))==0, (k,i,j)
def rank_mod(matrix, p):
    if not matrix:return 0
    rows=[list(map(lambda v: v%p, row)) for row in matrix]
    h=len(rows);w=len(rows[0]);rank=0
    for col in range(w):
        pivot=next((r for r in range(rank,h) if rows[r][col]),None)
        if pivot is None:continue
        rows[rank],rows[pivot]=rows[pivot],rows[rank]
        inv=pow(rows[rank][col],-1,p)
        for r in range(rank+1,h):
            if rows[r][col]:
                mul=rows[r][col]*inv %p
                for j in range(col,w):rows[r][j]=(rows[r][j]-mul*rows[rank][j])%p
        rank+=1
        if rank==h:break
    return rank

def quotient_betti(p):
    ranks={k:rank_mod(mat,p) for k,mat in B.items()}
    dimensions=[len(ORBIT_REPS[k]) for k in range(1,7)]
    return [dimensions[k]-ranks.get(k+1,0)-ranks.get(k+2,0) for k in range(6)]

assert quotient_betti(2) == [1,0,0,0,0,5]
assert quotient_betti(3) == [1,0,0,0,0,5]
assert quotient_betti(7) == [1,1,1,1,1,5]
assert sum((-1)**k*len(ORBIT_REPS[k+1]) for k in range(6)) == -4
print('PASS', 'faces',len(FACES),'morse_pairs',len(matched_pairs),'critical_5',len(unmatched),
      'free_C7',True,'quotient_orbit_cells',sum(len(v) for v in ORBIT_REPS.values()),
      'quotient_betti_mod2',quotient_betti(2),'quotient_betti_mod7',quotient_betti(7))
