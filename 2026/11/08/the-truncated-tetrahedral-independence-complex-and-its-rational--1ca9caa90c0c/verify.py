#!/usr/bin/env python3
"""Reproduce the independence-complex homotopy and symmetry calculation.

Standard-library only. A face is a bit mask on the twelve ordered pairs (a,b).
All loops are finite and exhaustive; no probabilistic or floating-point steps.
"""
from collections import Counter, defaultdict, deque
from itertools import permutations, combinations

VERTICES = list(permutations(range(4),2))
N = len(VERTICES)
assert N == 12

# Two independent adjacency descriptions: truncated-tetrahedron edges
# and the once-subdivided K4 incidence construction.
adj = [set() for _ in range(N)]
for i, (a,b) in enumerate(VERTICES):
    for j, (c,d) in enumerate(VERTICES):
        if i != j and (a == c or (a == d and b == c)):
            adj[i].add(j)
assert all(i in adj[j] for i in range(N) for j in adj[i])
edges = {tuple(sorted((i,j))) for i in range(N) for j in adj[i]}
assert len(edges) == 18
K4 = {tuple(sorted((a,b))) for a in range(4) for b in range(a+1,4)}
ends = [{('old',a), ('edge',min(a,b),max(a,b))} for a,b in VERTICES]
for i,j in combinations(range(N),2):
    assert ((i,j) in edges) == bool(ends[i] & ends[j])

# Method A: direct all-2^12 test.
def independent(mask):
    ids = [i for i in range(N) if mask & (1 << i)]
    return all(j not in adj[i] for i,j in combinations(ids,2))
faces = {mask for mask in range(1,1 << N) if independent(mask)}
# Method B: ascending recursive generation from an independent prefix.
recursive = set()
def extend(chosen, start):
    if chosen:
        recursive.add(chosen)
    for i in range(start,N):
        if all(j not in adj[i] for j in range(N) if chosen & (1 << j)):
            extend(chosen | (1 << i), i + 1)
extend(0,0)
assert faces == recursive
f = Counter(mask.bit_count()-1 for mask in faces)
assert [f[i] for i in range(4)] == [12,48,72,30]
assert len(faces) == 162
assert sum((-1)**d*f[d] for d in f)==6
print('graph_vertices', N, 'graph_edges', len(edges))
print('face_vector', [f[i] for i in range(4)], 'nonempty_faces', len(faces))

# Ascending greedy matching on the nonempty face poset, as in explicit
# sequential coordinate-toggle matchings.
unmatched = set(faces)
matched = set()
for v in range(N):
    for lo in sorted(tuple(unmatched),key=lambda x:(x.bit_count(),x)):
        hi = lo | (1 << v)
        if lo in unmatched and not (lo & (1 << v)) and hi in unmatched:
            assert hi.bit_count() == lo.bit_count()+1
            matched.add((lo,hi))
            unmatched.remove(lo)
            unmatched.remove(hi)
assert len(matched) == 78
assert Counter(x.bit_count()-1 for x in unmatched) == {0:1, 2:5}

# Verify gradient acyclicity of the entire directed Hasse diagram:
# unmatched incidences descend, matched incidences ascend.
arrows = defaultdict(list)
indeg = {x:0 for x in faces}
for hi in faces:
    for v in range(N):
        if not (hi & (1 << v)): continue
        lo=hi^(1<<v)
        if not lo: continue
        assert lo in faces
        src,dst = (lo,hi) if (lo,hi) in matched else (hi,lo)
        arrows[src].append(dst)
        indeg[dst] += 1
assert sum(map(len,arrows.values())) == 432
q=deque(x for x in faces if indeg[x]==0)
seen=0
while q:
    x=q.popleft();seen+=1
    for y in arrows[x]:
        indeg[y]-=1
        if indeg[y]==0:q.append(y)
assert seen==len(faces), f'gradient cycle: only {seen} sorted'
print('morse_pairs',len(matched),'critical_by_dim',sorted(Counter(x.bit_count()-1 for x in unmatched).items()))
print('gradient_hasse_edges',sum(map(len,arrows.values())),'toposorted',seen)

# Independent rank computation over F2 on the original simplicial chain complex.
# This is an independent check, not used to infer the integral homotopy type.
rank={}
for d in range(1,4):
    low=sorted(m for m in faces if m.bit_count()==d)
    high=sorted(m for m in faces if m.bit_count()==d+1)
    idx={m:j for j,m in enumerate(low)}
    pivots={}
    for hi in high:
        x=0
        for v in range(N):
            if hi & (1<<v):x ^= 1<<idx[hi^(1<<v)]
        while x:
            p=x.bit_length()-1
            if p not in pivots:
                pivots[p]=x
                break
            x ^= pivots[p]
    rank[d]=len(pivots)
assert rank=={1:11,2:37,3:30}
assert [12-1-rank[1],48-rank[1]-rank[2],72-rank[2]-rank[3],30-rank[3]]==[0,0,5,0]
print('mod2_boundary_ranks',rank,'reduced_betti',[0,0,5,0])

# Complete full S4 action: finite oriented face-trace formula. Classes are
# indexed by cycle-type partitions of 4.
def cycle_type(p):
    seen=set(); lens=[]
    for start in range(4):
        if start in seen: continue
        x=start; count=0
        while x not in seen:
            seen.add(x);count+=1;x=p[x]
        lens.append(count)
    return tuple(sorted(lens,reverse=True))

def perm_sign(p):
    return (-1) ** sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))

chars=defaultdict(set)
counts=Counter()
for p in permutations(range(4)):
    typ=cycle_type(p)
    counts[typ]+=1
    vertex_perm=[VERTICES.index((p[a],p[b])) for a,b in VERTICES]
    assert set(vertex_perm)==set(range(N))
    assert all(tuple(sorted((vertex_perm[i],vertex_perm[j]))) in edges for i,j in edges)
    # reduced Lefschetz character of H_2, since only H_2 is nonzero:
    # sum_{nonempty fixed faces} (-1)^(size-1)*orientation_sign - 1.
    tr=-1
    for face in faces:
        ids=[i for i in range(N) if face & (1<<i)]
        image=[vertex_perm[i] for i in ids]
        if set(image)==set(ids):
            tr+=(-1)**(len(ids)-1)*perm_sign(image)
    chars[typ].add(tr)
order=[(1,1,1,1),(2,1,1),(2,2),(3,1),(4,)]
assert [counts[t] for t in order]==[1,6,3,8,6]
assert [chars[t] for t in order]==[{5},{-1},{1},{2},{1}]
# Expected rational constituents: trivial + sign + (sign-twisted
# 3-dimensional standard representation). Compute their characters from
# cycle counts and fixed-point permutation character, not a lookup table.
for typ in order:
    sign=(-1)**(4-len(typ))
    fixed=typ.count(1)
    rhs=1+sign+sign*(fixed-1)
    assert chars[typ]=={rhs}
assert sum(counts[t]*next(iter(chars[t])) for t in order)==24
print('S4_conjugacy_sizes',[counts[t] for t in order])
print('H2_character',[next(iter(chars[t])) for t in order])
print('rational_decomposition','trivial + sign + (sign times standard_3)')
print('quotient_reduced_rational_betti2',1)
print('ALL_CHECKS_PASS')
